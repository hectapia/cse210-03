from game.casting.actor import Actor
from game.casting.player import Player
from game.casting.cast import Cast

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, cast, keyboard_service, video_service, player1, player2):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
            keyboard_service (KeyboardService): For getting directional input.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._player1 = player1
        self._player2 = player2
        self._velocity1 = cast._actors["player1"][0].get_velocity()
        self._velocity2 = cast._actors["player2"][0].get_velocity()
        self._game_over = False
        
    def start_game(self, cast, cell_size):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        x = 0
        while self._video_service.is_window_open():
            self.get_inputs(cast)
            self.do_updates(cast, cell_size)
            x+=1
            if x % 20 == 0 and len(cast._actors["player1"])<= 50 and self._game_over ==False:
                self._player1.grow_tail(cast)
                self._player2.grow_tail(cast)
            self.do_outputs(cast)
        self._video_service.close_window()

    def get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the players.
        
        Args:
            cast (Cast): The cast of actors.
        """
        if self._keyboard_service.get_direction1().get_x()!=0 or self._keyboard_service.get_direction1().get_y()!=0:
            self._velocity1 = self._keyboard_service.get_direction1()

        elif self._keyboard_service.get_direction2().get_x()!=0 or self._keyboard_service.get_direction2().get_y()!=0:
            self._velocity2 = self._keyboard_service.get_direction2()

        self._player1.set_velocity(cast, self._velocity1)
        self._player2.set_velocity(cast, self._velocity2)

    def do_updates(self, cast, cell_size):
        """Updates the players' position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        self._player1.move_next(cast, max_x, max_y)
        self._player2.move_next(cast, max_x, max_y)

        def game_over(player1_state, player2_state):
            self._game_over = True
            WHITE = Color(255, 255, 255)
            banner1 = cast.get_actor("banners",1)
            banner2 = cast.get_actor("banners",2)
            banner1.set_text(f"Player 1 : {player1_state}")
            banner2.set_text(f"Player 2 : {player2_state}")
            #create the game over banner
            banner3 = Actor()            
            banner3.set_text("GAME OVER")
            banner3.set_color(WHITE)
            banner3.set_font_size(banner1.get_font_size()*3)
            position = Point((max_x/2) - banner1.get_font_size()*9, (max_y/2)-banner1.get_font_size()*3)
            banner3.set_position(position)
            banner3 = cast.add_actor("banners", banner3)

            self._player1.set_color(cast, WHITE,WHITE)
            self._player2.set_color(cast, WHITE,WHITE)

        #compute if collision
        if self._game_over == False:
            if cast._actors["player1"][0].get_position().equals(cast._actors["player2"][0].get_position()):
                game_over("DRAW","DRAW")
            
            for tail in cast._actors["player2"]:
                if tail == cast._actors["player2"][0]:
                    continue

                elif cast._actors["player1"][0].get_position().equals(tail.get_position()):
                    game_over("LOSE","WIN")

            for tail in cast._actors["player1"]:
                if tail == cast._actors["player1"][0]:
                    continue

                elif cast._actors["player2"][0].get_position().equals(tail.get_position()):
                    game_over("WIN","LOSE")


    def do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
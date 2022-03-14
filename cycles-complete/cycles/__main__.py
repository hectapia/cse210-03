from game.casting.actor import Actor
from game.casting.player import Player
from game.casting.cast import Cast
from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
CAPTION = "Cycles"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
SNAKE_LENGTH = 8
cast = Cast()

def main():
    
    # create the banners
	banner1 = Actor()
	banner1.set_text("Player 1 : 0")
	banner1.set_font_size(FONT_SIZE)
	banner1.set_color(WHITE)
	banner1.set_position(Point(CELL_SIZE,0))
	cast.add_actor("banners", banner1)

	banner2 = Actor()
	banner2.set_text("Player 2 : 0")
	banner2.set_font_size(FONT_SIZE)
	banner2.set_color(WHITE)
	banner2.set_position(Point(MAX_X - 10*CELL_SIZE,0))
	cast.add_actor("banners", banner2)

    # create the player (a group of actors)
	cast.add_group ("player1")
	player1 = Player(cast, "player1", CELL_SIZE)
	player1.set_text(cast, "@", "#", SNAKE_LENGTH)
	player1.set_color(cast, RED, YELLOW)
	player1.set_font_size(cast, FONT_SIZE)
	position1 = Point((3*MAX_X)/4 , ((MAX_Y/2)-(len(cast._actors["player1"])//2)))
	player1.set_position(cast, position1)
	player1.set_initial_velocity(cast, Point(0, -CELL_SIZE))
	
	cast.add_group ("player2")
	player2 = Player(cast, "player2", CELL_SIZE)
	player2.set_text(cast, "@", "#", SNAKE_LENGTH)
	player2.set_color(cast, GREEN, RED)
	player2.set_font_size(cast, FONT_SIZE)
	position2 = Point(MAX_X/4, ((MAX_Y/2)-(len(cast._actors["player2"])//2)))
	player2.set_position(cast, position2)
	player2.set_initial_velocity(cast, Point(0, -CELL_SIZE))

    # start the game, parameters for the classes
	keyboard_service = KeyboardService(CELL_SIZE)
	video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
	director = Director(cast, keyboard_service, video_service, player1, player2)
	director.start_game(cast, CELL_SIZE)

if __name__ == "__main__":
    main()
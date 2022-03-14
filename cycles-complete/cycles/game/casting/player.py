from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Player(Actor):
    """
        The player is a little different than a standard actor because it composes a lot of actors,
        Therefore the polymorphism and the inheritance occur in the functions
    """
    def __init__(self, cast, player_name, cell_size):
        """create the constructors"""
        self._player_name = player_name
        self._cell_size = cell_size

    def set_text(self, cast, head ="@", segment = "#", number_of_segments = 5):
        """Updates the head text and the segment text to the given ones, and based on the number of the segments(tails).
        
        Args:
            the head text
            the segment text
            The number of the segments
        """
        Head = Actor()
        Head.set_text(head)
        cast.add_actor(self._player_name, Head)
        for i in range(number_of_segments):
            Segment = Actor()
            Segment.set_text(segment)
            cast.add_actor(self._player_name, Segment)

        #self._head = cast._actors[self._player_name][0]
    
    def set_color(self, cast, head_color, segment_color):
        """Updates the head color and the segment color to the given ones.
        
        Args:
            head_color
            segment_color
        """
        for x in cast._actors[self._player_name]:
            if x == cast._actors[self._player_name][0]:
                x.set_color(head_color)
            else:
                x.set_color(segment_color)

    def set_font_size(self, cast, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        for x in cast._actors[self._player_name]:
            x.set_font_size(font_size) 

    def move_next(self, cast, MAX_X, MAX_Y):
        """Updates the player's position."""
        
        #move all the segments
        for segment in cast._actors[self._player_name]:
            segment.move_next(MAX_X, MAX_Y)
        
        #update velocity
        #issue last
        for i in range(len(cast._actors[self._player_name]) - 1, 0, -1):
            trailing = cast._actors[self._player_name][i]
            previous = cast._actors[self._player_name][i-1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)


    def set_velocity(self, cast, velocity):
        cast._actors[self._player_name][0].set_velocity(velocity)
                
    def set_position(self, cast, position):
        """set the position of the player, based on the player's head position"""    
        for i in range(len(cast._actors[self._player_name])):
            #set the head's position to the given position, the tails will follow the head's position in a vertical way
            if i == 0:
                x = position.get_x()
                y = position.get_y()
            else:
                x = position.get_x()
                y = position.get_y() + i       
            position1 = Point(x, y)
            position1 = position1.scale(15)
            cast._actors[self._player_name][i].set_position(position1)

    def set_initial_velocity(self, cast, velocity):
        for actor in cast._actors[self._player_name]:
            actor.set_velocity(velocity)
        
    def grow_tail(self, cast):
        """this method allows the player to grow one tail as a new actor to contribute in the player's segments""" 
        last_actor = cast._actors[self._player_name][len(cast._actors[self._player_name])-1]
        new_tail = Actor()
        new_tail.set_text("#")
        new_tail.set_color(last_actor.get_color())
        new_tail.set_font_size(last_actor.get_font_size())
        velocity = last_actor.get_velocity()
        offset = velocity.reverse()
        new_tail.set_velocity(velocity)
        position = last_actor.get_position().add(offset)
        new_tail.set_position(position)
        cast.add_actor(self._player_name, new_tail)

    
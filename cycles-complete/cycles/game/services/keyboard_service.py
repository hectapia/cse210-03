import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)

    def get_direction1(self):
        """Gets the selected direction based on the currently pressed keys. for player 1

        Returns:
            Point: The selected direction from the key w, a, s, d
        """
        dx = 0
        dy = 0

        if self.is_key_down("a"):
            dx = -1
        
        elif self.is_key_down("d"):
            dx = 1
        
        elif self.is_key_down("w"):
            dy = -1
        
        elif self.is_key_down("s"):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction

    def get_direction2(self):
        """Gets the selected direction based on the currently pressed keys, for player 2

        Returns:
            Point: The selected direction from the key i, k, j, l
        """
        dx = 0
        dy = 0

        if self.is_key_down("j"):
            dx = -1
        
        if self.is_key_down("l"):
            dx = 1
        
        if self.is_key_down("i"):
            dy = -1
        
        if self.is_key_down("k"):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction


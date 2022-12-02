from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made by player 1. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, x):
        super().__init__()
        self._points1 = 0
        self.add_points_snake1(0)
        self._position = Point(x, 0)

    def add_points_snake1(self, points):
        """Adds the given points to player 1'a total points.
        
        Args:
            points1 (int): The points to add.
        """
        self._points1 += points
        self.set_text(f"Player 1: {self._points1}")

class Score2(Actor):
    """
    A record of points made by player 2. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, x):
        super().__init__()
        self._points2 = 0
        self.add_points_snake2(0)
        self._position = Point(x, 0)
        
    def add_points_snake2(self, points):
        """Adds the given points to player 2's total points.
        
        Args:
            points2 (int): The points to add.
        """
        self._points2 += points
        self.set_text(f"Player 2: {self._points2}")
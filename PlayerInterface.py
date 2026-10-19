'''Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define an abstract class named Player that inherits from the abc.ABC class.

The Player class should have an __init__ method that sets:

The moves attribute to an empty list.
The position attribute to (0, 0).
The path attribute to a list containing the initial position.
The Player class should have a method named make_move that:

Uses random.choice to get a random move from the moves attribute (defined in the concrete class).
Adds the values from the selected move to the current position and updates the position attribute.
Appends the new position tuple to the path attribute.
Returns the new position.
The Player class should have an abstract method named level_up to be implemented in concrete classes.

You should define a Pawn class that inherits from the Player class.

The Pawn class should use super() to call the parent's __init__ method and then set the moves attribute to a list of tuples representing x, y coordinates.

Each coordinate tuple should represent a movement of 1 unit in the following directions: up, down, left, right.

The Pawn class should implement a concrete level_up method by adding more moves to the moves attribute. The added moves should represent the four diagonal 
 (for example, 1 unit down plus 1 unit left).'''





# Import the ABC class and abstractmethod decorator from the Python built-in 'abc' module
# ABC stands for Abstract Base Class
from abc import ABC, abstractmethod
# Import the random module to handle randomized selections
import random


class Player(ABC):
    """
    An abstract base class representing a generic player.
    It cannot be instantiated on its own; child classes must inherit from it.
    """
    def __init__(self):
        # Initialize an empty list that child classes will fill with valid movement offsets
        self.moves = []
        
        # Track the player's current (x, y) coordinates, starting at the origin (0, 0)
        self.position = (0, 0)
        
        # Track the movement history, starting with the initial position
        self.path = [self.position]

    def make_move(self):
        """
        Selects a random move from self.moves, updates the position, 
        logs it to self.path, and returns the new position.
        """
        # Pick one random movement tuple from the self.moves list, e.g., (0, 1)
        move = random.choice(self.moves)
        
        # Add the horizontal offset (x) to current x-coordinate
        new_x = self.position[0] + move[0]
        
        # Add the vertical offset (y) to current y-coordinate
        new_y = self.position[1] + move[1]
        
        # Update self.position with the new coordinate tuple
        self.position = (new_x, new_y)
        
        # Append the new position tuple to the path list to keep track of history
        self.path.append(self.position)
        
        # Return the updated position tuple
        return self.position

    @abstractmethod
    def level_up(self):
        """
        Abstract method declaration.
        Every concrete subclass (like Pawn) MUST define its own implementation of this method.
        """
        pass


class Pawn(Player):
    """
    A concrete subclass extending Player.
    Implements standard orthogonal movement and adds diagonal moves when leveling up.
    """
    def __init__(self):
        # Run the __init__ constructor of the parent Player class first
        # This sets up self.position = (0, 0) and self.path = [(0, 0)]
        super().__init__()
        
        # Define 1-unit orthogonal movement coordinates: up, down, left, right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        """
        Concrete implementation of the required level_up method.
        Extends self.moves by adding 4 diagonal movement offsets.
        """
        # Define the 4 diagonal 1-unit coordinate offsets
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        # Add the new diagonal tuples to the existing self.moves list
        self.moves.extend(diagonal_moves)
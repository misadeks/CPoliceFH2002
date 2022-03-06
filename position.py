

class Position:
    """This class represents a position on the turtle canvas"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get(self) :
        """returns a tuple representation of the position"""
        return self.x, self.y

    @staticmethod
    def midpoint(pos1, pos2):
        """This method calculates the midpoint between two positions"""
        return Position((pos1.x + pos2.x) // 2, (pos1.y + pos2.y) // 2)

    @staticmethod
    def origin_position(size):
        """This method returns the place where the main drawing should be placed"""
        return Position(0, -size // 8)




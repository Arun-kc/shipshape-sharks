from typing import Any


class Rectangle():
    """Rectangle component"""

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __sizeof__(self) -> tuple:
        return self.width, self.height

    def isOverlapping(self, Other: Any) -> bool:
        """
        Method for calculating if two rectangles overlap according to DeMorgan's law

        :param Rectangle Other
        :returns bool
        """
        if(self.width == 0 or self.height == 0 or Other.width == 0 or Other.height == 0):
            return False

        return not ((self.x > (Other.x+Other.width)) or ((self.x+self.width) < Other.x)
                    or (self.y > (Other.y+Other.height)) or ((self.y+self.height) < Other.height))

    def isContainingPoint(self, point: tuple) -> bool:
        """
        Method for checking if one point lies inside itself

        :param Point(int, int)
        :returns bool
        """
        x, y = point
        return x in range(self.x + self.width) and y in range(self.y + self.height)

    def isContaining(self, Other: Any) -> bool:
        """
        Method for calculating if one rectangle is completely inside other

        :param Rectangle Other
        :returns bool

        """
        return (Other.x >= self.x and (Other.x+Other.width) <= (self.x+self.width) and Other.y >= self.y
                and (Other.y+Other.height) <= (self.y+self.height))


class Perception(Rectangle):
    """Square"""

    def __init__(self, center: tuple, perc_range: int):
        offset = center[0] - perc_range, center[1] - perc_range
        size = 2 * perc_range
        super().__init__(*offset, size, size)

    def update(self, center: tuple) -> None:
        """Update perception"""
        x, y = center[0] - self.perc_range, center[1] - self.perc_range
        self.x = x
        self.y = y

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

    def isContaining(self, Other: Any) -> bool:
        """
        Method for calculating if one rectangle is completely inside other

        :param Rectangle Other
        :returns bool

        """
        return (Other.x >= self.x and (Other.x+Other.width) <= (self.x+self.width) and Other.y >= self.y
                and (Other.y+Other.height) <= (self.y+self.height))

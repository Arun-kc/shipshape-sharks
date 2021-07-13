from typing import overload


class Rectangle:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __sizeof__(self) -> int:
        return tuple(self.width, self.height)

    def isOverlapping(self, Other) -> bool:
        if(self.width == 0 or self.height == 0 or Other.width == 0 or Other.height == 0):
            return False

        return not ((self.x > (Other.x+Other.width)) or ((self.x+self.width) < Other.x) or (self.y > (Other.y+Other.height)) or ((self.y+self.height) < Other.height))

    def isContaining(self, Other):
        return Other.x >= self.x and (Other.x+Other.width) <= (self.x+self.width) and Other.y >= self.y and (Other.y+Other.height) <= (self.y+self.height)

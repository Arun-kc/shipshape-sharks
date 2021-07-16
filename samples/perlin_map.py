import random
from typing import Any

from blessed import Terminal
from blocks import Blocks
from perlin_noise import PerlinNoise

term = Terminal()


def random_seeds() -> int:
    """Returns random seeds"""
    return random.randint(1, 10**9)


def distance(x: int, y: int, a: int, b: int) -> float:
    """Distance between two points"""
    return ((x - a) ** 2 + (y - b) ** 2) ** .5


class PerlinMap:
    """Creates Perlin map"""

    def __init__(self, width: int, height: int, octaves: int = 10, seed: int = random_seeds()):
        self.width = width
        self.height = height

        noise = PerlinNoise(octaves=octaves, seed=seed)

        noise_map = [[0]*width for j in range(height)]
        for j in range(height):
            for i in range(width):
                map_pattern_value = self.pattern_generator(i, j)
                noise_map[j][i] = noise(map_pattern_value) * 100

        self.noise_map = noise_map

        self.MAP_string = ''
        self.MAP_matrix = []

    def __str__(self):
        return self.MAP_string

    # Find most suitable color/ variant of same type of block
    def _closest(self, noise: float, mapping: dict) -> Any:
        return min(mapping, key=lambda x: abs(noise - mapping[x]))

    def _find_corners(self) -> list:
        """Find corners of rectangle"""
        width, height = self.width, self.height
        return [(0, 0), (width, 0), (0, height), (width, height)]

    # Used in creating mapping between noise and coordinates
    def distance_from_corners(self, x: int, y: int) -> float:
        """Find distance of point from corners"""
        corners = self._find_corners()
        dis = sum([distance(x, y, a, b) for a, b in corners])
        return dis

    # Used in creating mapping between noise and coordinates
    def distance_from_center(self, x: int, y: int) -> float:
        """Finds distance of points from center"""
        width, height = self.width, self.height
        dis = distance(x, y, width/2, height/2)
        return dis

    def pattern_generator(self, x: int, y: int) -> float:
        """Return value defines how noise values will change regards to coordinates"""
        dis_corners = self.distance_from_corners(x, y)
        dis_center = self.distance_from_center(x, y)
        key = (dis_corners - dis_center)
        return [x / key, y / key]

    def generate_map(self, blocks: list) -> None:
        """Generates Maps according to information in blocks: list"""
        width, height = self.width, self.height
        tmp = [[0] * width for j in range(height)]
        profile_name = random.choices(['desert', 'normal'], weights=[10, 90])[0]
        for j in range(height):
            for i in range(width):

                noise = self.noise_map[j][i]

                for block in blocks:
                    profile = block.settings['profiles'][profile_name]
                    if noise >= profile['noise_value']:
                        color = self._closest(noise, profile['color_options'])
                        bg_color = self._closest(noise, profile['bg_color_options'])
                        spirite = self._closest(noise, profile['spirite_options'])
                        break

                tmp[j][i] = block(spirite, color=color, bg_color=bg_color)

        self.MAP_matrix = tmp
        self.MAP_string = '\n'.join([''.join(str(col) for col in row) for row in tmp])


if __name__ == '__main__':
    width, height = term.width, term.height
    perlin_map = PerlinMap(width, height, seed=50)
    perlin_map.generate_map(Blocks)

    print(perlin_map, end='')

import random

from perlin_noise import PerlinNoise
from blessed import Terminal

rand_seed = int(10**5*random.random())
term = Terminal()
noise = PerlinNoise(octaves=10, seed=rand_seed)

green = {
    0:term.on_chartreuse,
    -6:term.on_chartreuse2,
    -12:term.on_chartreuse3,
}

trees = {
    0: '🌲',
    -25: '🌳',
    95: '🌴'
}

grass = {
    0: ' ',
    # -5: '▓' 
}


print(term.home+term.clear, end='')
w, h = term.width, term.height

pic = [[noise([i/w , j/h]) for j in range(h)] for i in range(w)]
s = ''
for j in range(h):
    for i in range(w):
        ns = pic[i][j]
        closest = lambda y:min(y, key=lambda x: abs(ns*100 - x))
        if ns > -0.25:
            ch = green[closest(green)](term.chartreuse3(grass[closest(grass)]))
        else:
            ch = term.steelblue4_on_steelblue2(random.choice(' '))
        print(ch, end='')
    print()
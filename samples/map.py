import random

from blessed import Terminal

term = Terminal()


def grass() -> str:
    """Returns random Grass Unicode character"""
    return getattr(term, 'on_'+random.choice(green))(term.chartreuse3('▓'))


def tree() -> str:
    """Returns random tree Unicode character"""
    return getattr(term, 'on_'+random.choice(green))(random.choice('🌲🌳🌴'))


def water() -> str:
    """Returns ranodm water Unicode character"""
    return term.steelblue4_on_steelblue2(random.choice(' '))


green = [
    'chartreuse',
    'chartreuse2',
    'chartreuse3',
]

d = {
    'grass': grass,
    'tree': tree,
    'water': water
}

freq_weights = {
    'grass': 3,
    'tree': 2,
    'water': 1
}

print(term.home+term.clear, end='')
w, h = term.width, term.height
s = ''

for j in range(1, h, 3):
    for i in range(1, w, 3):
        typ, obj = random.choices(list(d.items()), weights=(90, 8, 2))[0]

        s += term.move_xy(i, j) + obj()
        chances = [(96, 3, 1), (75, 21, 4)]
        ix = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

        for x, y in ix:
            p, q = i + x, j + y
            st = set(d.keys())
            st.discard(typ)
            ls = obj(), *map(lambda x: d[x](), sorted(st, key=lambda x: freq_weights[x], reverse=True))
            if p in range(w) and q in range(h-1):
                s += term.move_xy(p, q) + random.choices(ls, weights=chances[0])[0]

if __name__ == '__main__':
    print(s, end='')
'''
For reference only

▓ 	▒ 	░

░▒▓█▇▆▅▄▃▂

▂▃▅▇█▓▒░۩۞۩ ۩۞۩░▒▓█▇▅▃▂

▂ ▃ ▄ ▅ ▆ ▇ █▓▒░ ░▒▓█▇▆▅ ▄▃▂ ▂ ▃ ▄ ▅ ▆ ▇ █▓▒░ ░▒
'''

# 🌲
# evergreen tree

# U+1F332

# 🌳
# deciduous tree

# U+1F333

# 🌴
# palm tree

# U+1F334

# 🍁
# maple leaf

# U+1F341

# 🎄
# christmas tree

# U+1F384

# 🎋
# tanabata tree

# U+1F38B

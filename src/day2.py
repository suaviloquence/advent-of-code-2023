s = open("in/day2.in").read()

def part1():
    n = 0
    for l in s.split('\n'):
        if len(l.split(': ')) < 2: continue
        g, games = tuple(l.split(': '))
        id = int(g.split(' ')[1])
        flag = True
        for game in games.split('; '):
            for color in game.split(', '):
                num, typ = tuple(color.split(' '))
                num = int(num)
                if num > {"red": 12, "blue": 14, "green": 13}[typ]:
                    flag = False
        if flag:
            n += id
    print(n)

def part2():
    n = 0
    for l in s.split('\n'):
        if len(l.split(': ')) < 2: continue
        g, games = tuple(l.split(': '))
        id = int(g.split(' ')[1])
        flag = True
        mins = {"blue": 0, "red": 0, "green": 0}
        for game in games.split('; '):
            for color in game.split(', '):
                num, typ = tuple(color.split(' '))
                num = int(num)
                mins[typ] = max(num, mins[typ])
        n += mins["blue"] * mins["red"] * mins["green"]
    print(n)

part1()
part2()
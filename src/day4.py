import queue
s = open('day4.in').read().split('\n')

def p1():
    N = 0
    for l in s:
        pts = 0.5
        if ':' not in l: continue
        winning, mine = l.split(':')[1].split(' | ')
        w = set()
        for n in winning.split():
            w.add(int(n))

        for n in mine.split():
            if int(n) in w:
                pts *= 2

        N += int(pts)
    
    print(N)


s_ = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')
def p2():
    q = queue.Queue()
    N = 0

    cards = dict()

    for i, l in enumerate(s, 1):
        x = 0
        if ':' not in l: continue
        winning, mine = l.split(':')[1].split(' | ')
        w = set()
        m = set()
        for n in winning.split():
            w.add(int(n))



        for n in mine.split():
            if int(n) in w:
                x += 1

        if x > 0:
            cards[i] = list(range(i + 1, max(i + x + 1, i + 1)))
        else: cards[i] = []

    qq = {}
    for i, l in enumerate(s, 1):
        if not ':' in l: continue
        qq[i] = 1
    
    for i in qq:
        N += qq[i]
        for z in cards[i]:
            qq[z] += qq[i]

    print(N)


p1()
p2()

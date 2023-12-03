s = open('day3.in').read().split('\n')

def p1():
    sum = 0
    for i, l in enumerate(s):
        num = 0
        add = False
        for j, c in enumerate(l):
            if c.isdigit():
                num *= 10
                num += int(c)
                if i > 0:
                    add = add or any([x not in ".0123456789" for x in s[i-1][j-1:j+2]])
                add = add or any([x not in ".0123456789" for x in s[i][j-1:j+2]])
                if i + 1 < len(l):
                    add = add or any([x not in ".0123456789" for x in s[i + 1][j-1:j+2]])
            else:
                if add:
                    sum += num
                num = 0
                add = False
        if add:
            sum += num
        num = 0
        add = False

    print(sum)




j = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')

def p2():
    sum = 0
    from collections import defaultdict
    gears = defaultdict(list)
    for i, l in enumerate(s):
        num = 0
        grs = set()
        for j, c in enumerate(l):
            if c.isdigit():
                num *= 10
                num += int(c)
                if i > 0:
                    for k in range(max(j - 1, 0), min(len(s[i - 1]), j + 2)):
                        if s[i-1][k] == '*':
                            grs.add((i - 1, k))
                for k in range(max(0, j - 1), min(len(s[i]), j + 2)):
                    if s[i][k] == '*': grs.add((i, k))
                if i + 1 < len(l):
                    for k in range(max(0, j - 1), min(len(s[i + 1]), j + 2)):
                        if s[i+1][k]== '*': grs.add((i + 1, k))
            else:
                for gr in grs:
                    gears[gr].append(num)
                num = 0
                grs = set()
        for gr in grs:
            gears[gr].append(num)
        num = 0
        grs = set()


    for gr in gears:
        lst = gears[gr]
        print(lst)
        if len(lst) == 2:
            sum += lst[0] * lst[1]
    
    print(sum)

p1()
p2()

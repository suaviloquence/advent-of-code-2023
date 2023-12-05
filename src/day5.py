s = open("day5.in").read().split('\n')

def nxt(it):
    try:
        l = next(it)
        return l
    except: return None

sx = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".split('\n')

def p1():
    sp = iter(s)
    now = [ int(n) for n in next(sp).partition(": ")[2].split()]
    later = now.copy()
    next(sp)

    while _ := nxt(sp):
        
        mapped = [False for _ in now]
        while l := next(sp):
            dest, src, length = [int(n) for n in l.split()]
            for i, n in enumerate(now):
                if mapped[i]: continue
                if src <= n < src + length:
                    later[i] = n + dest - src
                    mapped[i] = True
            
            now = later
            later = now.copy()
    
    print(now)
    
        



def p2():
    sp = iter(s)
    a = [ int(n) for n in next(sp).partition(": ")[2].split()]
    now = [[a[i], a[i] + a[i + 1]] for i in range(0, len(a), 2)]
    later = now.copy()
    
    next(sp)
    while tttttt := nxt(sp):
        now = later

        mapped = [False for _ in now]
        while l := next(sp):
            dest, src, length = [int(n) for n in l.split()]
            i=0
            while(i < len(later)):
                n = later[i]
                if mapped[i]: 
                    i += 1
                    continue
                if src <= n[0] < src + length:
                    if n[1] <= src + length:
                        later[i][0] = n[0] + dest - src
                        later[i][1] = n[1] + dest - src
                        mapped[i] = True
                    else:
                        later.append([src + length, n[1]])
                        mapped.append(False) 
                        later[i][0] = n[0] + dest - src
                        later[i][1] = dest + length
                        mapped[i] = True
                elif n[0] <= src < n[1]:
                    if src + length <= n[1]:
                        later.append([dest, dest + length])
                        mapped.append(True)
                        later.append([src + length, n[1]])
                        mapped.append(False)
                    else:
                        later.append([dest, n[1] + dest - src])
                        mapped.append(True)
                    later[i][1] = src
                elif n[0] < src + length <= n[1]:
                    later[i][0] = n[0] + dest - src
                    later[i][1] = dest + length            
                    mapped[i] = True
                    
                    later.append([src + length, n[1]])
                    mapped.append(False)
                i += 1
            now = later
            later = now.copy()
    
    print(min([n[0] for n in now if n[1] > n[0]]))
    

p1()
p2()
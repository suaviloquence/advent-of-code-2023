file_in = open("day6.in").read().split('\n')
testcase_in = """Time:      7  15   30
Distance:  9  40  200""".split('\n')

sp = file_in

def p1():
    times = [int(x) for x in sp[0].split(':')[1].split()]
    distances = [int(x) for x in sp[1].split(':')[1].split()]
    ways = [0 for _ in times]
    for i, t in enumerate(times):
        d = distances[i]
        for j in range(0, t):
            distance = (t - j) * (j)
            if distance > d: ways[i] += 1
    
    prod = 1
    for n in ways:
        if n > 0:
            prod *= n
    
    return prod

def p2():
    time = int(''.join(sp[0].split(':')[1].split()))
    distance = int(''.join(sp[1].split(':')[1].split()))
    ways = 0
    for i in range(0, time):
        d = (time - i) * i
        if d > distance: ways += 1
        
    return ways



print(p1())
print(p2())
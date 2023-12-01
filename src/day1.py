a = open('in/day1.in').read()
# part 1
# s = 0
# for l in a.split('\n'):
#     n = 0
#     for c in l:
#         if c in "0123456789":
#             n = int(c) * 10
#             break
#     for c in l[::-1]:
#         if c in "0123456789":
#             n += int(c)
#             break
    
#     s += n

s = 0
for l in a.split('\n'):
    n = 0
    for (i, c) in enumerate(l):

        flag = False
        for (j, x) in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if l[i:].startswith(x):
                n = j * 10
                flag = True
                break
        if flag: break
        if c in "0123456789":
            n = int(c) * 10
            break
    for (i, c) in enumerate(l[::-1]):

        flag = False
        for (j, x) in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            if l[len(l) - i:].startswith(x):
                flag = True
                n += j
                break
        if flag: break
        if c in "0123456789":
            n += int(c)
            break
    s += n
print(s)

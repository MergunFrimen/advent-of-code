from copy import deepcopy
import sys
import math

sys.setrecursionlimit(10**4)

trans = {
         'A' : 2,
         'B' : 4,
         'C' : 6,
         'D' : 8
        }
score = {
         'A' : 1,
         'B' : 10,
         'C' : 100,
         'D' : 1000
        }

result = [[], math.inf]

def can_get_there(m, f, t):
    offset = 1 if f <= t else -1
    for i in range(f+offset, t+offset, offset):
        if isinstance(m[i], str) and m[i] != '':
            return False
    return True

def finished(m):
    return m == ['','',['A0','A0','A0','A0'],'',['B0','B0','B0','B0'],'',['C0','C0','C0','C0'],'',['D0','D0','D0','D0'],'','']

def rec(m, r, s):
    if finished(m):
        if s < result[1]:
            result[0] = r
            result[1] = s
            print(result)
        return

    # out
    for i in range(len(m)):
        if isinstance(m[i], list) and m[i] and m[i][-1][1] == '1':
            for j in range(len(m)):
                if isinstance(m[j], str) and m[j] == '' and can_get_there(m, i, j):
                    new = deepcopy(m)
                    distance = abs(i - j) + 1 + 4 - len(m[i])
                    new[j] = new[i].pop()[0] + '0'
                    rec(new, r + [(i, j)], s + distance * score[new[j][0]])
    # in
    for i in range(len(m)):
        if isinstance(m[i], str) and m[i] != '':
            j = trans[m[i][0]]
            if m[j] in [k*[m[i]] for k in range(4)] and can_get_there(m, i, j):
                new = deepcopy(m)
                distance = (abs(i - j) + 4 - len(m[i])) * score[new[i][0]]
                new[j].append(new[i])
                new[i] = ''
                rec(new, r + [(i, j)], s + distance)

def part1():
    # m = ['','',['A1','D1','D1','B1'],'',['D1','B1','C1','C1'],'',['C1','A1','B1','B1'],'',['A1','C1','A1','D1'],'','']
    m = ['','',['B1','D1','D1','C1'],'',['A1','B1','C1','A1'],'',['B1','A1','B1','D1'],'',['C1','C1','A1','D1'],'','']
    rec(m, [], 0)

part1()

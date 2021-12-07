m = list(x.split() for x in open("input/04.txt").read().rstrip().split('\n'))
print(sum(map(lambda x : len(x) == len(set(x)), m)))
print(sum(map(lambda x : len(x) == len(set(x)) and len(set(map(''.join, map(sorted, x)))) == len(set(x)), m)))

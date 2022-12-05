with open("input/01.txt") as f:
    m = [int(x) for x in f.read().split('\n')[:-1]]
print(sum(1 for i in range(len(m) - 1) if m[i] < m[i+1]))
print(sum( 1 for i in range(len(m) - 3) if sum(m[i:i+3]) < sum(m[i+1:i+4])))

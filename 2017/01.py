with open("input/01.txt") as f:
    m = f.read().rstrip()
print(sum(int(m[i]) for i in range(len(m)) if m[i] == m[(i+1) % len(m)]))
print(sum(int(m[i]) for i in range(len(m)) if m[i] == m[(i+len(m)//2) % len(m)]))

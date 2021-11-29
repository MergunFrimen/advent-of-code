x = 13
i = 1
l = []

while x > 0:
    if x % i == 0:
        l.append(i)
        x -= 1*i
    i += 1

print(l)
print(sum(map(lambda x : 1*x, l)))

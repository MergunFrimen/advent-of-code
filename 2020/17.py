from itertools import product

for p in [1, 2]:
  g = {(x,y) + (0,) * p for x,l in enumerate(open('input.txt'))
                        for y,c in enumerate(l) if c == '#'}
    
  def a(c):
    n = len(g & set(product(*[range(a-1, a+2) for a in c])))
    return c in g and n == 4 or n == 3
    
  for r in range(6):
    g = set(filter(a, product(range(-r-1, r+8), repeat=2+p)))

  print(len(g))

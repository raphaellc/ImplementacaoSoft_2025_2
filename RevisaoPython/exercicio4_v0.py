import random

def f():
    v = []
    for _ in range(10):
        v.append(random.randint(20, 50))
    
    s = sum(v)
    
    print(v)
    print(s)

f()
def f(x):
    return x + 10

def g(x):
    return x + 2

def h(x):
    return g(f(x))

print(h(2))



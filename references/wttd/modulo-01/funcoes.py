def f(a, b, c="dC", *args, **kwargs):
    print(a, b, c, args, kwargs)

def g():
    pass

print(g())

f("A", "B", "C", "D", "E", "F", z="Z", w="W", g="G")
f(b="B", a="A", c="C")
f("A", "B")

t = "D", "E", "F"
d = {"l" : "L", "m" : "M", "n" : "N"}

f("A", "B", "C", *t, **d)

def filter(**lookups):
    for k, v in lookups.items():
        print(k.split("__"), v)

filter(name__startswith="Hen", age__lt=30,
       city__endswith="rói")


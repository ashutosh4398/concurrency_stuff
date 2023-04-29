
# BASIC EXAMPLE
def gen1(n):
    for i in range(n):
        yield i

def gen2(n):
    yield 1100
    yield from gen1(n)
    yield 200

def basic_example():
    gen = gen2(5)
    for i in gen:
        print(i)

# BASIC EXAMPLE ENDS
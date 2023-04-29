
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

# ADVANCED EXAMPLE
def writer():
    while True:
        try:
            w = (yield)
        except Exception as e:
            print(e)
        print(">>>", w)

def writer_wrapper():
    w = writer()
    w.send(None)
    while True:
        text = (yield)
        w.send(text)

def writer_wrapper_advance():
    """
        yield from does the same work as writer_wrapper()
    """
    yield from writer()

wrap = writer_wrapper_advance()
wrap.send(None) # prime the coroutine
texts = ["Ashutosh is a software developer", "He has 3 years of experience", "spam"]
for text in texts:
    if text == "spam":
        wrap.throw(Exception("Spam text"))
    else:
        wrap.send(text)
    


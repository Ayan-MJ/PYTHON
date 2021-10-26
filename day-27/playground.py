def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 4, 5, 6, 7, 8))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)




def test(*args):
    print(type(args))


test(1, 2, 3, 5)

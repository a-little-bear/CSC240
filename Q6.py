from math import floor

def foo(i):
    if i == 0:
        raise ValueError
    if i == 1:
        return 5
    
    return 8 * foo(floor(i/3)) + i ** 2

for i in range(1, 20):
    try:
        print(i, foo(i), i**2)
    except ValueError:
        continue


# ex. 1 -----------------------------------------------
def sum(*args, **kwargs):
    sum = 0
    for arg in args:
       if (type(arg) is int) or (type(arg) is float):
           sum += arg

    return sum

def sum_exceptie(*args, **kwargs):
    sum = 0
    for arg in args:
        try:
           sum += arg
        except TypeError as e:
           continue

    return sum

print('Test functie sum:')
print(sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum())
print(sum(2, 4, 'abc', param_1=2))

print('Test functie sum_exceptie:')
print(sum_exceptie(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_exceptie())
print(sum_exceptie(2, 4, 'abc', param_1=2))

# ex. 2 -----------------------------------------------

def readInteger():
    my_var = input('Introduceti un numar interg:')
    try:
        my_int = int(my_var)
    except ValueError as e:
        return 0
    else:
        return my_int

print(readInteger())

# ex. 3 -----------------------------------------------

from recursive_module import sum_all, sum_even, sum_odd

print(sum_all(4))

print(sum_even(4))

print(sum_odd(4))

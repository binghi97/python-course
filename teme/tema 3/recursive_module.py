
def sum_all(_number):
    try:
        number = int(_number)
    except ValueError as e:
        print('Eroare! Introduceti un numar intreg ...')
    else:
        if number == 0:
            return 0

        return number + sum_all(number-1)

def sum_even(_number):
    try:
        number = int(_number)
    except ValueError as e:
        print('Eroare! Introduceti un numar intreg ...')
    else:
        if number % 2 != 0:
            number -= 1
        if number == 0:
            return 0

        return number + sum_even(number-2)

def sum_odd(_number):
    try:
        number = int(_number)
    except ValueError as e:
        print('Eroare! Introduceti un numar intreg ...')
    else:
        if number % 2 == 0:
            number -= 1
        if number == 1:
            return 1

        return number + sum_odd(number-2)
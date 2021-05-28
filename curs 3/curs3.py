import random


elements = [x for x in range(11)]
print(elements)

while True:
    random_choise = random.choice(elements)
    if random_choise % 3 == 0:
        break
    print(f'Exit random choise is: {random_choise}')

print(f'Exit random choise is: {random_choise}')

for i in range(11):
    if i % 2 == 0:
        continue
    else:
        pass    # pass este un placeholder, tine locul unei instructiuni fara sa faca nimic
    print(i)

print('\n\n') # ---------------------------------------------------------------------------

my_sum = 0

def get_sum(a,b):
    global my_sum
    my_sum = a + b
    print(my_sum)

get_sum(1, 2)
print(my_sum)

l1 = [1, 2, 3, 4]
l2 = l1 # l1 is passed by reference
l3 = list(l1) # l1 is passed by value == l1.copy() == [x for x in l1]

l2[0] = 0

print(l1)
print(l3)

def my_function(nume, prenume, *args, **kwargs):
    print(f'Nume: {nume}')
    print(f'Prenume: {prenume}')

    for arg in args:
        print(f'arg is {arg}')

    for key in kwargs.keys():
        print(f'For key {key}, we have the value {kwargs[key]}')


my_function('popescu', 'ana', 'are', 2, 'mere', job='developer', age=22)


# recursivitate
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(4))
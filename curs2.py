print('Acesta este cursul al doilea !')

name = 'Ana'
if name:
    print(name)  # this is a inline comment
    print(type(name))
else:
    print('Nu avem niciun nume!')

first_person = {'Name': 'John'}
second_person = {'Name': 'John'}

if first_person is second_person:
    print('sunt la aceleasi adresa')
else:
    print('nu sunt aceleasi adresa')

if first_person == second_person:
    print('sunt aceleasi')
else:
    print('nu sunt aceleasi')

my_str = r'Owner\'s \r\n\tmanual.'
print(my_str)

print("""Somnoroase pasarele
Pe la cuiburi se aduna""")

def my_function():
    """"this function does something"""
    print("My first function !")

my_function()

msg = "{name} has {age} years.".format(name="Ion",age="18")
print(msg)

name = 'Ion'
age = 18
msg_2 = f"{name} has {age} years."
print(msg_2)

l = [1, 2, 3, 'Ana are mere', True, False, None, [3, 4, 5]]
print(l[-1])

inventar =  ["faina", "drojdie", "apa"]
for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f'{index}. {value}')

#doua chestiuni echivalente
print(inventar[-1])
print(inventar[len(inventar)-1])

l1 = [0,-2, 7, 5]
l2 = [13, 19, [12, 10]]

l1.extend(l2)
print(l1)

#tuplu si string sunt imutabile

my_dict = {1: "Home", 2: "Office", 3: "Restaurant"}
for key, val in my_dict.items():
    print(f'{key} => {val}')

print(my_dict.get(2, "Nu exista cheia"))
print(my_dict.get(4, "Nu exista cheia"))

#folosim set atunci cand vrem sa scoatem duplicatele dintr-o lista
l = [1, 2, 2, 3]
print(l)

s = set(l)
print(s)

print(list(s))

l1 = [1, 2, 2, 3]
l2 = [1, 9, 0]

s1 = set(l1)
s2 = set(l2)

print(list(s1.intersection(l2))) #doar elem comune
print(list(l1 - l2)) #ce e in l1 si nu e l2


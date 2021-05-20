
lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista)

lista_ordonata_ascendent = lista.copy()
lista_ordonata_ascendent.sort()
print(lista_ordonata_ascendent)

lista_ordonata_descendent = lista.copy()
lista_ordonata_descendent.sort(reverse=True)
print(lista_ordonata_descendent)

print(lista_ordonata_ascendent[1::2])

print(lista_ordonata_ascendent[0::2],'\n')

for number in lista:
    if number > 3 and number % 3 == 0:
        print(number)

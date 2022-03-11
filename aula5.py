

#manejo de Lista en Py

lista = [1, 3, 5, 7]
lista_animal = ['perro', 'gato', 'dinosauro']
print(lista_animal[1])

# soma = 0
# for x in lista:
#     soma += x
#     print(soma)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista_animal))
# nueva_lista = lista_animal * 3
# print(nueva_lista)
#
# if 'lobo' in lista_animal:
#     print('existe gato en la lista')
# else:
#     print('no existe gato en la lista')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
#     lista_animal.pop(0) #remueve depende del numero en la lista
#     print(lista_animal)
#
#     lista_animal.remove('gato') # Remueve por el mombre
#     print(lista_animal)

#ordenando listas con .sort()
    # lista.sort()
    # lista_animal.sort()
    # print(lista)
    # print(lista_animal)

#ordenara en reverse con .reverse()


# Las Tuplas son inalterables en comparacion con las listas no puede
lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(tupla)
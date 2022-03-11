
#Organizar con juntos y subconjuntos en Python
# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

#union de conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 =  {5, 6, 7, 8}

conjunto_union = conjunto.union(conjunto2)
print('union: {}'.format(conjunto_union))

#conjunto interseccion
conjunto_interseccion = conjunto.intersection(conjunto2)
print('Interseccion:{}'.format (conjunto_interseccion))

#conjunto difference
conjunto_diferente1 = conjunto.difference(conjunto2)
conjunto_diferente2 = conjunto2.difference(conjunto)
print('Diferencia entre 1 y 2: {}'.format(conjunto_diferente1))
print('Diferencia entre 2 y 1: {}'.format(conjunto_diferente2))

#Diferencia Simetrica
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferencia simetrica: {}'.format(conjunto_diff_simetrica))
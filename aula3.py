#pedir informacion para usario
# a = int (input('primer valor:'))
# b = int (input('segundo valor:'))
# c = int( input('tercer valor:'))
#
# if a > b and a > c:
#     print('el mayor numero es {}'. format(a))
# elif b > a and b > c:
#     print('el mayor numero es {}'.format(b))
# else:
#     print('el mayor numero es {}'.format(c))
#     print('fin')

#uso de or
# a = int(input('primer ingresa valor:'))
# b = int(input('segundo ingresa valor:'))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or  not resto_b > 0:
#     print('existe un numero es par')
# else:
#     print(' no hay numero par')

a = int(input('primer bimestre:'))
if a > 10:
    a= int(input('error con el primer bimestre:'))
b = int(input('segundo bimestre:'))
if b > 10:
    b= int(input('error con el segundo bimestre:'))
c = int(input('tercer bimestre:'))
if c > 10:
    c= int(input('error con el tercero bimestre:'))
d = int(input('cuarto bimestre:'))
if d > 10:
    d= int(input('error con el cuarto bimestre:'))
media = (a + b +c +d) / 4
print('media: {}'.format(media))
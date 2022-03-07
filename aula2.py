#input valor pedido a usuario
a = int (input('primer valor'))
b = int (input('segundo valor'))
suma = a + b
resta = a - b
multip = a * b
resto = a % b
divi = a / b
#print( 'suma: ' + str(suma), 'resta: ' + str(resta), multip, resto, divi)
# print( 'suma: {suma}. resta: {resta}'.format(suma = suma, resta = resta))
resultado = ('suma: {suma} .\nresta: {resta}'.format(suma = suma, resta= resta) )
print(resultado)
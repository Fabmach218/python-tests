def validar(cadena):

    for x in cadena:
        if x != '0' and x != '1' : return False

    return True

cadena = input('Ingrese una cadena de 0s y 1s: ')

while(validar(cadena) == False):
    cadena = input('Ingrese una cadena de 0s y 1s: ')

inicio = 1
aceptado = 1
estado = inicio
fin = False
contador = 0

while fin == False:
    
    if contador > len(cadena) - 1:
        fin = True
        break

    if estado == 1:
        if cadena[contador] == '1' : estado = 1
        if cadena[contador] == '0' : estado = 2
        contador += 1
        continue
    
    if estado == 2:
        if cadena[contador] == '1' : estado = 2
        if cadena[contador] == '0' : estado = 1
        contador += 1
        continue

if estado == aceptado :
    print('La cadena ' + cadena + ' es aceptada!!!')
else:
    print('La cadena ' + cadena + ' es rechazada!!!')
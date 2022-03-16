class Alumno:

	def __init__(self, nombre, edad, nota):
		
		self.nombre = nombre
		self.edad = edad
		self.nota = nota


tam = int(input('Ingrese la cantidad de alumnos: '))
indice = 1

lista = []

while(indice <= tam):
	print('Alumno ' + str(indice))
	nombre = input('Ingrese el nombre: ')
	edad = int(input('Ingrese la edad: '))
	nota = int(input('Ingrese la nota: '))
	lista.append(Alumno(nombre, edad, nota))
	indice += 1

def ordenarDesc():
	
	for i in range(0, tam-1):
		for j in range(i+1, tam):
			if(lista[i].nota < lista[j].nota):
				aux = lista[i]
				lista[i] = lista[j]
				lista[j] = aux

ordenarDesc()

print('Nombre\tEdad\tNota')

for alumno in lista:
	print(alumno.nombre + '\t' + str(alumno.edad) + '\t' + str(alumno.nota))

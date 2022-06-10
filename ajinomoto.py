class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Usuario:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

class Carrito:
    def __init__(self, producto, cantidad, importe):
        self.producto = producto
        self.cantidad = cantidad
        self.importe = importe

usuarios = []
productos = []
carritoItems = []

productos.append(Producto(1,'ADEREZO AJINOMOTO',5))
productos.append(Producto(3,'MEZCLA PARA APANAR ',1.3))
productos.append(Producto(12,'SAZONADOR UMAMI',4))
productos.append(Producto(13,'MISKÍSIMO',2))
productos.append(Producto(14,'SAZONADOR UNAMI PEQUEÑO',4))
productos.append(Producto(15,'TALLARÍN ROJO',2))
productos.append(Producto(16,'SOPA ORIENTAL',1))
productos.append(Producto(17,'SOPA DE CARNE',1.5))
productos.append(Producto(18,'SOPA DE GALLINA',1.5))
productos.append(Producto(19,'SOPA DE POLLO',1.5))
productos.append(Producto(20,'DOÑA GUSTA CARNE',0.5))
productos.append(Producto(21,'DOÑA GUSTA POLLO',0.5))
productos.append(Producto(22,'DOÑA GUSTA TOCINO',0.5))
productos.append(Producto(23,'DOÑA GUSTA GALLINA',0.5))
productos.append(Producto(24,'AJINO-SILLAO',3))
productos.append(Producto(28,'AJISAL AJINOMOTO',20))

print('Productos')

for producto in productos:
    print(str(producto.id) + ', ' + producto.nombre + ', S/. ' + str(producto.precio))

def getProductoById(id):

    for producto in productos:
        if producto.id == id:
            return producto

carritoItems.append(Carrito(getProductoById(13),4,0))
carritoItems.append(Carrito(getProductoById(21),6,0))

total = 0

print('Carrito')

for item in carritoItems:
    item.importe = item.producto.precio * item.cantidad
    total += item.importe

for item in carritoItems:
    print(str(item.producto.id) + ', ' + item.producto.nombre + ', S/. ' + str(item.producto.precio) + ', ' + str(item.cantidad) + ', S/. ' + str(item.importe))

print('Total a pagar: S/. ' + str(total))
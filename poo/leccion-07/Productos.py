class Producto:
    contador_productos = 0
    
    def __init__(self, nombre: str, precio: float):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
        
    @property
    def id_producto(self):
        return self._id_producto
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio: float):
        self. precio = precio
    
    def __str__(self) -> str:
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio:.2f}'
    

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalón', 150.00)
    print(producto2)
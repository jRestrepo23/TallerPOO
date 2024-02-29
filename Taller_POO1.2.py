class factura:
    
    def __init__(self, num_pieza, desc_pieza, cantidad, precio):
        self.num_pieza = num_pieza #string
        self.desc_pieza = desc_pieza #string
        self.cantidad = cantidad #int
        self.precio = precio #int

        if self.cantidad < 0 :
            self.cantidad = 0
        else:
            self.cantidad
    
    def getNum_pieza(self):
        return print(self.num_pieza)
    
    def getDesc_pieza(self):
        return print(self.desc_pieza)
    
    def getCantidad(self):
        return print(self.cantidad)
    
    def getPrecio(self):
        return print(self.precio)
    
    def set_Num_pieza(self, num_pieza):
        self.num_pieza = num_pieza
        
    def set_Desc_pieza(self, desc_pieza):
        self.desc_pieza = desc_pieza
    
    def set_Cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def set_Precio(self, precio):
        self.precio = precio
        
    def obtenerMontoFactura(self):
        resultado = int(self.cantidad * self.precio)
        if resultado > 0 :
            print(" el monto de la factura es: " ,resultado)
        else:
            resultado = 0
            print(" el monto de la factura es: " ,resultado)
    pass

objeto1 = factura("2029","amarilla",2,5)
objeto1.getCantidad()
objeto1.obtenerMontoFactura()


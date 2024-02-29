class cuenta:
    
    def __init__(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial
        
        if self.saldo_inicial > 0 : 
            self.saldo_inicial = saldo_inicial
        else:
            self.saldo_inicial = 0
            return print("Saldo inicial invalido")
        
    def miembroCredit(self, cantidad_ingresada):

        self.cantidad_ingresada = cantidad_ingresada
        self.saldo_inicial = self.cantidad_ingresada + self.saldo_inicial
    
    def miembroCargar(self, cantidad_retiro):
        self.cantidad_retiro = cantidad_retiro
        if self.cantidad_retiro > self.saldo_inicial :
            return print("El monto a cargar excede el saldo inicial de la cuenta ")
        else:
            self.saldo_inicial = self.saldo_inicial - self.cantidad_retiro
    
    def obtenerSaldo(self):
        print("Su saldo inicial es de: " +  str(self.saldo_inicial))
              
    pass
        
print("°°°°°°°°°°°°°°°°°°°°°°°°") 
print(" ")

cuenta_1 = cuenta(0)
cuenta_1.obtenerSaldo()

print(" ")
print("°°°°°°°°°°°°°°°°°°°°°°°°") 
print(" ")
print("°°°°°°°°°°°°°°°°°°°°°°°°") 
print(" ")

cuenta_2 = cuenta(2000)
cuenta_2.miembroCargar(3000)
cuenta_2.obtenerSaldo()
print(" ")

print("°°°°°°°°°°°°°°°°°°°°°°°°") 






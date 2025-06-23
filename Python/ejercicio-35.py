""" 
35. Crea la clase UsuarioBanco:
- Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
- Métodos: retirar_dinero, transferir_dinero, agregar_dinero.

Código a seguir:
- Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
- Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
- Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
- Implementar agregar_dinero para aumentar el saldo del usuario.

Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades al saldo de Bob.
3. Transferir 80 unidades de Bob a Alicia.
4. Retirar 50 unidades del saldo de Alicia.
"""

class UsuarioBanco():

    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, retirada):
        try:
            if self.saldo - retirada >= 0:
                self.saldo -= retirada
                print(f"Has retirado {retirada}€. Saldo en cuenta {self.saldo}€")
            else: 
                print(f"Su saldo es de {self.saldo}, no puede retirar {retirada}")
        except TypeError:
            print("No has introducido un numero")

    def transferir_dinero(self, receptor, dinero):
        self.retirar_dinero(dinero)
        receptor.ingresar_dinero(dinero)

    def ingresar_dinero(self, ingreso):
        try: 
            self.saldo += ingreso
            print(f"Ingreso realzado. Saldo total: {self.saldo}€")
        except TypeError:
            print("Ingrese solo numeros")

alicia = UsuarioBanco("Alici", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.ingresar_dinero(20)
bob.transferir_dinero(alicia, 80)
bob.transferir_dinero(alicia, 50)
alicia.retirar_dinero(50)
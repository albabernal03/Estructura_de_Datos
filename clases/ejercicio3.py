import time
class Productos:
    def __init__(self, alimentaria, servicio, precio_inicial, precio_final) :
        self.alimentaria = alimentaria
        self.servicio = servicio
        self.precio_inicial = precio_inicial
        self.precio_final = precio_final
    def comprar(self):
        print('Entrando a la página web...')
        time.sleep(2)
        print('Tiene 100€, que quiere comprar? (1) Alimentaria o (2) Servicio')
        opcion = int(input())
        if opcion == 1:
            print('Ha elegido alimentaria')
            precio_inicial = 100
            precio_final = precio_inicial*1.05
            print('Calculando...')
            time.sleep(2)
            print(f'La compra ha sido realizada con éxito, el precio final es {precio_final}€')
        elif opcion == 2:
            print('Ha elegido servicio')
            precio_inicial = 100
            precio_final = precio_inicial*1.20
            print('Calculando...')
            time.sleep(2)
            print(f'La compra ha sido realizada con éxito, el precio final es {precio_final}€')
        else:
            print('Ha elegido una opción incorrecta')
            return

Productos.comprar('opcion')



            







import time

class MVC:
    def __init__(self, linea1, linea2):
        self.linea1 = linea1
        self.linea2 = linea2

        if isinstance(linea1, str) and isinstance(linea2, str): #Comprobamos que las lineas son cadeas de caracteres con isinstance el cual devuelve un booleano
            linea1 = linea1.upper()
            linea2 = linea2.upper()
        else:
            print('No es una cadena de caracteres')
            return

    def fichero(self):
        #A continuacion creamos el fichero
        fichero = open('ejercicio2.txt', 'w')
        #A continuacion escribimos en el fichero
        fichero.write(self.linea1)
        fichero.write('\n')
        fichero.write(self.linea2)
        #Cerramos el archivo en 10 segundos
        time.sleep(10)
        fichero.close()

#Ejectuamos la clase, esto luego va en el main
mvc = MVC(input('Introduzca una frase:'), input('Introduzca otra frase:'))
mvc.fichero()

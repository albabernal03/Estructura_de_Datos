from clases.ejercicio2 import MVC
from clases.ejercicio1 import Bloque, Si, MientrasQue, Mostrar


if __name__ == '__main__':
    mvc = MVC(input('Introduzca una frase:'), input('Introduzca otra frase:'))
    mvc.fichero()
if __name__ == '__main__':
    mostrar_ok = Mostrar('"OK"') 
    mostrar_ko = Mostrar('"KO"') 
    alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
    bloque_alternativa = Bloque() 
    bloque_alternativa.agregarInstruccion(alternativa) 
    bucle = MientrasQue(True, bloque_alternativa) 

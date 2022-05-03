<h1 align="center">	Estructura de datos</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Estructura_de_Datos)
***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea nos proponen tres ejercicios distintos.



**Ejercicio 1:**

*En el primer ejercicio se nos facilita un código el cual tenemos que arreglar para que tenga el comportamiento esperado.*

**Ejercicio 2:**

*En este segundo ejercicio nos piden crear un programa que lea dos lineas, las convierta a mayúsculas y a continuación las escriba en un fichero.*

**Ejercicio 3:**

*Por último en este ejercicio nos piden implementar un programa que factura productos por valor de 100, con la tasa de IVA correcta, según sean productos de alimentación o servicios.*

***
## Índice

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercicio 3](#id3)

***

## Ejercicio 1:<a name="id1"></a>

**Código**

```
class Bloque: 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruccion(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 
 
class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 
#Y aquí hay un pequeño "programa" escrito usando estas clases:

```

***

## Ejercicio 2:<a name="id2"></a>

**Código**

```
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
```

***

## Ejercicio 3:<a name="id3"></a>

**Código**

```

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
```



***

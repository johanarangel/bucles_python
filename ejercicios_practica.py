#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Johana Rangel
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.2"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    # inicio = ....
    # fin = ....

    # cantidad_numeros ....
    # sumatoria ....

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla

    cantidad_numeros = 0
    sumatoria = 0
        
    inicio = int(input('Ingrese el primer número de la secuencia numérica:\n'))
    fin = int(input('Ingrese el último número de la secuencia numérica:\n'))

    for numero in range(inicio, fin+1):
        cantidad_numeros += 1
        sumatoria += numero 
        promedio = sumatoria / cantidad_numeros
    
    print('Sumatoria: {}, Cantidad de numeros ingresados: {} y promedio: {}'.format(sumatoria, cantidad_numeros, promedio))


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    contador = 0
    simbolo_operacion = True
    
    while simbolo_operacion: 

        numero_uno = float(input('Ingrese un número: \n'))
        numero_dos = float(input('Ingrese otro número diferente de cero: \n'))          
        print('Ingrese el simbolo de la operación a realizar (+ suma, - resta, * multiplicación, / división, **Potencia ) o ingrese la palabra FIN para terminar el programa:')
        simbolo_operacion =  str(input())
        
        if (simbolo_operacion == 'FIN'):
            print('Ha salido del programa')
            break 
        
        elif (simbolo_operacion == '+'):
            resultado = numero_uno + numero_dos
            print('El resultado de sumar {} y {} es {}'.format(numero_uno, numero_dos, resultado))
            contador += 1
            continue  # Inove: Este continue no es necesario ya que el programa al salir de acá igual volverá al principio del while

        elif (simbolo_operacion == '-'):
            resultado = numero_uno - numero_dos
            print('El resultado de restar {} y {} es {}'.format(numero_uno, numero_dos, resultado))
            contador += 1
            continue  # Inove: Este continue no es necesario ya que el programa al salir de acá igual volverá al principio del while

        elif (simbolo_operacion == '*'):
            resultado = numero_uno * numero_dos
            print('El resultado de multiplicar {} y {} es {}'.format(numero_uno, numero_dos, resultado))
            contador += 1
            continue  # Inove: Este continue no es necesario ya que el programa al salir de acá igual volverá al principio del while

        elif (simbolo_operacion == '/'):
            resultado = numero_uno / numero_dos
            print('El resultado de dividir {} y {} es {}'.format(numero_uno, numero_dos, resultado))
            contador += 1
            continue  # Inove: Este continue no es necesario ya que el programa al salir de acá igual volverá al principio del while 

        elif (simbolo_operacion == '**'):
            resultado = numero_uno ** numero_dos
            print('El resultado de {} a la potencia {} es {}'.format(numero_uno, numero_dos, resultado))
            contador += 1
            continue  # Inove: Este continue no es necesario ya que el programa al salir de acá igual volverá al principio del while
                     
        else:
            print('Error, el simbolo ingresado no corresponde con los indicados, intente nuevamente')
    
 
def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    #sumatoria = 0           # Ya le hemos inicializado en 0

    #cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    #cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes
     # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    sumatoria = 0
    cantidad_validas = 0
    cantidad_ausentes = 0
    promedio = 0
    cantidad_notas = len(notas)
       
    for nota in notas:
        sumatoria += nota

        if (nota >= 90 or nota >= 80 or nota >= 70 or nota >= 60 or nota < 60):
            cantidad_validas += 1

        if (nota < 0):
            cantidad_ausentes += 1

    promedio = sumatoria / cantidad_notas
   
    if promedio >= 90:
        print('El promedio {} equivale a "A"'.format(round(promedio, 2))) 
    
    elif promedio >= 80:
        print('El promedio {} equivale a "B"'.format(round(promedio, 2))) 
    
    elif promedio >= 70:
        print('El promedio {} equivale a "C"'.format(round(promedio, 2)))
    
    elif promedio >= 60:
        print('El promedio {} equivale a "D"'.format(round(promedio, 2)))
    
    else:
        print('El promedio {} equivale a "F"'.format(round(promedio, 2)))  
    
    print('La cantidad de ausentes: {}'.format(cantidad_ausentes))
    print('La cantidad de notas válidas: {}'.format(cantidad_validas))
  

def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = len(temp_dataloger)         # Aquí debe almacenar cuantas temperatuas hay en la lista
    

    # Colocar el bucle aqui......

    for temperatura in temp_dataloger:
        temperatura_sumatoria += temperatura

        if (temperatura_max is None) or (temperatura > temperatura_max):
            temperatura_max = temperatura
                        
        if (temperatura_min is None) or (temperatura < temperatura_min):
            temperatura_min = temperatura        
            continue  # Inove: Este continue no es necesario ya que en el próximo paso volvera al "for temperatura in temp_dataloger"

    temperatura_promedio = temperatura_sumatoria / temperatura_len

    print('El temperatura máxima es: {}, la minima es: {} y el promedio de temperatura es: {}'.format(temperatura_max, temperatura_min, round(temperatura_promedio,2))) 
 
    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    print("Máxima temperatura = ", max(temp_dataloger))
    print("Minima temperatura = ", min(temp_dataloger))

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp
    
    print("temperatura_sumatoria = ", round(sum(temp_dataloger),2))

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo
   
    if (19 < temperatura_promedio < 28):
       print('La época del año actualmente es verano')

    elif (11 < temperatura_promedio < 24):
        print('La época del año actualmente es otoño')

    elif (8 < temperatura_promedio < 14):
        print('La época del año actualmente es invierno')

    elif (10 < temperatura_promedio < 24):
        print('La época del año actualmente es primavera')
    

def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''
    consulta = True
    maxima_palabra = ''
    lista_palabras = []
    palabra_mayor = ''
         
    while consulta:
        consulta = str(input('Cómo quiere ordenar la palabras? \n Ingrese 1, para ordenar por alfabético. \n Ingrese 2, par ordenar por cantidad de letras?: \n .Ingrese 3, para salir del programa: \n'))
        
        if consulta == '3':
            print('El programa ha finalizado')
            break

        if consulta == '1':    
            for palabra in range(3):
                palabra = str(input('Ingrese una palabra:\n'))
                lista_palabras.append(palabra)
                continue

            for palabra in lista_palabras:
                if palabra > maxima_palabra:
                    maxima_palabra = palabra

            print('La palabra más grande alfabeticamente es {}'.format(maxima_palabra))
                     
        elif consulta == '2':
            for palabras in range(3):
                palabras = str(input('Ingrese una palabra:\n'))
                lista_palabras.append(palabras)
                continue  # Inove: Este continue no es necesario ya que en el próximo paso volvera al "for palabras in range(3):"

            for palabras in lista_palabras:
                if (len(palabras) > len(palabra_mayor)):
                    palabra_mayor = palabras
                    
            print('La palabra más grande por cantidad de letras es {}'.format(palabra_mayor))
        
        else:
            print('Error, el valor ingresado no corresponde con los indicados. Intente nuevamente.')
            continue
        
        
if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    ej3()
    #ej4()
    #ej5()

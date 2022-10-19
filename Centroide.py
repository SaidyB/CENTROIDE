import matplotlib.pyplot as plt
import random


def Recibir():

    opcion= int(input("Presiona: \n 1. Generar las coordenadas aleatoriamente \n 2. Ingresar coordenadas\n"))

    while (opcion<1 or opcion>2):
        print("Ingresar una opción válida")
        opcion= int(input("Presiona: \n 1. Generar las coordenadas aleatoriamente \n 2. Ingresar coordenadas\n"))

    return opcion


def triangulo ():

    opcion= Recibir()

    if (opcion ==1):
        p1_x = random.randrange(0,100)
        p1_y = random.randrange(0,100)
        p2_x = random.randrange(0,100)
        p2_y = random.randrange(0,100)
        p3_x = random.randrange(0,100)
        p3_y = random.randrange(0,100)

        puntos = [[p1_x, p1_y], [p2_x, p2_y], [p3_x, p3_y]]
    
        return puntos 


    elif (opcion==2):
        p1_x=int(input("Ingrese la primera coordenada en x: \n "))
        p1_y=int(input("Ingrese la primera coordenada en y: \n "))
        p2_x=int(input("Ingrese la segunda coordenada en x: \n "))
        p2_y=int(input("Ingrese la segunda coordenada en y: \n "))
        p3_x=int(input("Ingrese la tercera coordenada en x: \n "))
        p3_y=int(input("Ingrese la tercera coordenada en y: \n "))

        puntos = [[p1_x, p1_y], [p2_x, p2_y], [p3_x, p3_y]]
    
        return puntos 

def circulo():
    opcion= Recibir()
    if opcion==1:
        p1_x = random.randrange(0,100) # Coordenada "x" del centro del circulo.
        p1_y = random.randrange(0,100) # Coordenada "y" del centro del circulo.

        puntos = [[p1_x, p1_y]]

        return puntos # Regresamos lista de puntos.

    if opcion==2:
        p1_x= int(input("Ingrese la Coordenada x del centro del circulo."))
        p1_y= int(input("Ingrese la Coordenada y del centro del circulo."))

        puntos = [[p1_x, p1_y]]

        return puntos # Regresamos lista de puntos.

def rectangulo():
    opcion= Recibir()
    if opcion==1:
        p1_x = random.randrange(0,100)
        p1_y = random.randrange(0,100)
        p2_x = random.randrange(0,100)
        p2_y = p1_y
        p3_x = p2_x
        p3_y = random.randrange(0,100)
        p4_x = p1_x
        p4_y = p3_y

        puntos = [[p1_x, p1_y], [p2_x, p2_y], [p3_x, p3_y], [p4_x, p4_y]]
        
        return puntos 

    if opcion==2:

        p1_x=int(input("Ingrese la primera coordenada en x: \n "))
        p1_y=int(input("Ingrese la primera coordenada en y: \n "))
        p2_x=int(input("Ingrese la segunda coordenada en x: \n "))
        print("La segunda coordenada en y debe ser igual a la primera coordenada en y")
        p2_y = p1_y
        print("La tercra coordenada en x debe ser igual a la segunda coordenada en x")
        p3_x = p2_x
        p3_y=int(input("Ingrese la tercera coordenada en y: \n "))
        print("la cuarta coordenada en x debe ser igual a la primera coordenada en x")
        p4_x = p1_x
        print("la cuarta coordenada en y debe ser igual a la tercera coordenada en y")
        p4_y = p3_y

        puntos = [[p1_x, p1_y], [p2_x, p2_y], [p3_x, p3_y], [p4_x, p4_y]]
        
        return puntos 


def calcularCentroide(puntos):
    # Tenemos que calcular la suma de todos los elementos del eje "x" y el eje "y",
    # y dividirlo entre el la cantidad de elementos de esta lista.

    sum_x = 0 # Total de valores de "x".
    sum_y = 0 # Total de valores de "y".

    for punto in puntos: # Iteramos sobre los puntos de la lista.

        punto_x = punto[0] # Tomamos coordenada "x" (posición [0] del punto).
        punto_y = punto[1] # Tomamos coordenada "y" (posición [1] del punto).

        sum_x += punto_x # Suma de valores de "x".
        sum_y += punto_y # Suma de valores de "y".

    centroide_x = sum_x / len(puntos) # Total del valores de "x" entre numero de puntos.
    centroide_y = sum_y / len(puntos) # Total del valores de "y" entre numero de puntos.

    centroide = [centroide_x, centroide_y]

    # Calculo de distancias medias de los lados de las figuras, para
    # graficar mejor el centroide.
    puntos_medios = [] # Lista de puntos medios.

    if len(puntos) <= 1: # Para el caso del circulo, solo hay un punto.
        unico_punto = puntos[0] # [[c1x, c1y]]
        puntos_medios.append([unico_punto[0], unico_punto[1]])
    else:
        for i in range(len(puntos)):
            punto_ini = puntos[i]   # Primer punto de referencia.
            punto_fin = puntos[i-1] # Segundo punto de referencia, se itera en reversa.        
            media_x = (punto_ini[0] + punto_fin[0]) / 2 # Tomamos la coordenada "x" del punto y dividimos a la mitad.
            media_y = (punto_ini[1] + punto_fin[1]) / 2 # Tomamos la coordenada "y" del punto y dividimos a la mitad.
            puntos_medios.append([media_x, media_y])
    
    return centroide, puntos_medios # Regresamos las coordenas del centroide como lista. 

#- Funcion para graficar -#
# Recibe de parametros el tipo de figura, los puntos de sus aristas, el centroide
# y los puntos medios.
def graficar(figura, puntos, centroide, puntos_medios):

    # Caso si se trata de un circulo
    if figura == 'circulo':
        radio = 5 # Se establece un radio constante de "5".
        figura, conjunto = plt.subplots() # Generamos subgraficas para incorporar el circulo.
        # Generamos una variable (objeto) que será el centroide.
        punto = plt.scatter(centroide[0], centroide[1], color='red',zorder=6)
        # Generamos una variable (objeto) que será el circulo.
        circulo = plt.Circle((puntos[0][0], puntos[0][1]), radio, color='cyan', fill=False, zorder=2 )
        # Incorporamos el centroide y el circulo a la subgrafica
        conjunto.add_artist(circulo)
        conjunto.add_artist(punto)
        # Graficamos las lineas de trazo del centroide.
        plt.plot([centroide[0]-radio, centroide[0]+radio],
                           [centroide[1]-radio, centroide[1]+radio],
                           color='black', linestyle='dashed', zorder=4)
        plt.plot([centroide[0]-radio, centroide[0]+radio],
                           [centroide[1]+radio, centroide[1]-radio],
                           color='black', linestyle='dashed', zorder=5)        
        # Establecemos los limites para visualizar el circulo.
        plt.xlim(puntos[0][0]-10, puntos[0][0]+10)
        plt.ylim(puntos[0][1]-10, puntos[0][1]+10)
        plt.grid(linestyle='--')
    else: # Caso cuando se trata de un TRIANGULO o RECTANGULO.
        # Se utiliza una estructura de "FOR" reducido, el cual lo que hace
        # es iterar como lo haria un FOR, pero esta vez se contienen los elementos
        # dentro de una lista "[ ]".
        x_s = [x[0] for x in puntos]
        y_s = [y[1] for y in puntos]
        plt.plot(x_s, y_s, color='cyan')
        # Aqui se genera la linea entre el ultimo punto y el primero, para llegar
        # al ultimo punto de una lista podemos usar "lista[-1]" y para el primero
        # se usa "lista[0]".
        plt.plot([x_s[-1], x_s[0]], [y_s[-1], y_s[0]], color='cyan')
        # La estrategia del "FOR reducido" se puede usar directamente en funciones.
        plt.scatter([x[0] for x in puntos], [y[1] for y in puntos], color='blue')
        # Agregamos las lineas medias al centroide y el centroide.
        for punto in puntos_medios:
            plt.plot([punto[0], centroide[0]], [punto[1], centroide[1]], color='black', linestyle='dashed')
        for i in range(len(puntos)):
            plt.plot([puntos[i][0], centroide[0]], [puntos[i][1], centroide[1]], color='black', linestyle='dashed')
        # Graficamos el centroide.
        plt.scatter(centroide[0], centroide[1], color='red', zorder=5) # "zorder" manda el punto al frente.
        plt.grid(linestyle='--')

    
    # Esta función no regresa nada explicito, ya que el objeto de la gráfica
    # ya fue generado por "matplotlib", solo es necesario mostrarlo usando
    # "plt.show()" en el cuerpo principal.

""" MAIN """

print("Bienvenido!\n Seleccione una figura para hallar su centroide:")
figura= input("Escoje el tipo de figura: \n circulo \n rectangulo\n triangulo\n").lower()

if (figura=="triangulo"):
    puntos=triangulo()
    centroide, puntos_medios = calcularCentroide(puntos) # Calculo de centroide.
elif (figura=="circulo"):
    puntos=circulo()
    centroide, puntos_medios = calcularCentroide(puntos) # Calculo de centroide.
elif(figura=="rectangulo"):
    puntos=rectangulo()
    centroide, puntos_medios = calcularCentroide(puntos) # Calculo de centroide.
else:
    print("Figura no reconocida")

graficar(figura, puntos, centroide, puntos_medios) # Se llama a la función para graficar.
plt.show()


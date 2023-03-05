""" 
    Algoritmo de Busqueda Binaria
"""

def binarySearch(list, item):
    #inicializamos las variables min y max para almacenar el indice minimo y maximo de la lista
    min = 0
    max = len(list) - 1
    #creamos un contador para contar el numero de iteraciones
    count = 0
    
    #iteramos mientras el indice minimo sea menor o igual al indice maximo
    while min <= max:
        #calculamos el indice medio de la lista
        mid = (min + max) // 2
        #obtenemos el valor del elemento en el indice medio
        guess = list[mid]
        #aumentamos el contador
        count += 1
        
        #si el valor del elemento en el indice medio es igual al valor buscado regresamos el indice
        if guess == item:
            print("Numero de iteraciones para encontrar el elemento: ", count)
            return mid
        elif guess > item:
            max = mid - 1
        else:
            min = mid + 1
    #si no se encuentra el elemento regresamos -1
    return -1

# lista de numeros primos
listaNumerosPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#imprimimos la lista de numeros primos
print("Para la siguiente lista de nuemros primos:")
for n in range(0, len(listaNumerosPrimos)):
    print("------", end="")    
print()
for n in range(0, len(listaNumerosPrimos)):
    print("|",listaNumerosPrimos[n],"|", end="")
print()
for n in range(0, len(listaNumerosPrimos)):
    print("------", end="")  
print()

#pedimos al usuario que ingrese el numero que desea buscar
n = int(input("Ingrese el numero que desea buscar: "))

#obtenemos el indice del elemento buscado
result = binarySearch(listaNumerosPrimos, n)

#imprimimos el resultado
if result != -1:
    print(f"El numero {n} se encuentra en la lista en el indice {result}")
    print(f"El contenido de la lista en el indice {result} es {listaNumerosPrimos[result]} ")
else: 
    print(f"El numero {n} no se encuentra en la lista")
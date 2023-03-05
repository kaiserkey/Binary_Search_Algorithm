""" 
    Algoritmo de Busqueda Binaria
"""

def binarySearch(list, item):
    #inicializamos las variables left y right para almacenar el indice izquierdo y derecho de la lista
    left = 0
    right = len(list) - 1
    #creamos un contador para contar el numero de iteraciones
    count = 0
    
    #iteramos mientras el indice izquierdo sea menor o igual al indice derecho
    while left <= right:
        #calculamos el indice medio de la lista
        mid = (left + right) // 2
        #obtenemos el valor del elemento en el indice medio
        guess = list[mid]
        #aumentamos el contador
        count += 1
        
        #si el valor del elemento en el indice medio es igual al valor buscado regresamos el indice
        if guess == item:
            print("Numero de iteraciones para encontrar el elemento: ", count)
            return mid
        #si el valor del elemento en el indice medio es mayor al valor buscado
        elif guess > item:
            right = mid - 1
        #si el valor del elemento en el indice medio es menor al valor buscado
        else:
            left = mid + 1
    #si no se encuentra el elemento regresamos -1
    return -1

# lista de numeros primos
listOfPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#imprimimos la lista de numeros primos
print("Para la siguiente lista de nuemros primos:")
for n in range(0, len(listOfPrime)):
    print("------", end="")    
print()
for n in range(0, len(listOfPrime)):
    print("|",listOfPrime[n],"|", end="")
print()
for n in range(0, len(listOfPrime)):
    print("------", end="")  
print()

#pedimos al usuario que ingrese el numero que desea buscar
n = int(input("Ingrese el numero que desea buscar: "))

#obtenemos el indice del elemento buscado
result = binarySearch(listOfPrime, n)

#imprimimos el resultado
if result != -1:
    print(f"El numero {n} se encuentra en la lista en el indice {result}")
    print(f"El contenido de la lista en el indice {result} es {listOfPrime[result]} ")
else: 
    print(f"El numero {n} no se encuentra en la lista")
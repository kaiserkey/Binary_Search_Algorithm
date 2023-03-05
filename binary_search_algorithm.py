""" 
    Algoritmo de Busqueda Binaria
"""
listaNumerosPrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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

n = int(input("Ingrese el numero que desea buscar: "))
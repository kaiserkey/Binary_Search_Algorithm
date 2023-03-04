
---
<h1><p align="center">Algoritmo de Busqueda Binaria</p></h1>

![ALgoritmo de BUsqueda Binaria](binary_search.png)

---

| [Definicion](#definicion) | [Utilizacion](#utilizacion) | [Pseudocódigo](#pseudocódigo) |
| ------------------------- | --------------------------- | ----------------------------- |
---

## Definicion

La **búsqueda binaria** es un algoritmo eficiente para encontrar un elemento específico en una lista **ordenada** de elementos. Utiliza una estrategia de búsqueda de **"divide y vencerás"** para reducir la cantidad de elementos que debe revisar, **dividiendo** la lista a la **mitad** en cada iteración. Es uno de los algoritmos de búsqueda más rápidos y eficientes disponibles. 

---
### Utilizacion

El algoritmo de búsqueda binaria se utiliza comúnmente para encontrar elementos en un conjunto de datos ordenados como **listas**, **arreglos** o **matrices ordenadas**. También se utiliza para realizar búsquedas en bases de datos y para encontrar el elemento más próximo a un número dado en un conjunto de números.
Tomemos de ejemplo el catálogo estelar Tycho-2 una base de datos que contiene la posición, la magnitud y la clase espectral de más de 2.5 millones de estrellas. Supongamos que queremos buscar en el catálogo una estrella en particular, con base en el nombre de la estrella. Si el programa examinara cada estrella en el catálogo estelar en orden empezando con la primera, con un algoritmo llamado búsqueda lineal, la computadora podría, en el peor de los casos, tener que examinar todas las 2.5 millones de estrellas para encontrar la estrella que estás buscando. Si el catálogo estuviera ordenado alfabéticamente por nombres de estrellas, la búsqueda binaria no tendría que examinar más de 22 estrellas, incluso en el peor de los casos.

---

## Pseudocódigo

1. Ordenar los elementos si no se encuentran ordenados. El algoritmo de búsqueda binaria requiere que los elementos estén ordenados de forma ascendente.
2. Definir el rango de búsqueda estableciendo los límites izquierdo y derecho como un conjunto de elementos en los que se realizará la búsqueda.
3. Calcular el punto medio. Esto se realiza dividiendo el número de elementos del rango por la mitad. 
4. Comparar el elemento en el punto medio con el elemento que se está buscando.
5. Si el elemento es igual al elemento que se está buscando, se ha encontrado el elemento
6. Si el elemento es mayor, el elemento buscado debe estar en el rango inferior. Establecer el límite derecho como el punto medio - 1.
7. Si el elemento es menor, el elemento buscado debe estar en el rango superior.Establecer el límite izquierdo como el punto medio + 1.
8. Si el elemento buscado se encuentra, devolver su índice.
9.  Si el límite derecho es menor que el limite izquierdo, entonces no está en el array. Regresa -1.
10. Repetir los pasos 2 a 9 hasta que el elemento buscado sea encontrado o el límite derecho sea menor que el limite izquierdo.


![example](binary-search.gif)

---

| [@ByDanielSan](https://github.com/kaiserkey) |
| ------------------------------------------ |





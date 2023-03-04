
---
<center><h2> Algoritmo de Busqueda Binaria</h2></center>

![ALgoritmo de BUsqueda Binaria](binary_search.png)

---

|[Definicion](#definicion)|[Utilizacion](#utilizacion)|[Descripcion](#descripcion-de-los-Pasos-para-crear-el-Algoritmo)
| - | - | - |
---

## Definicion

La **búsqueda binaria** es un algoritmo eficiente para encontrar un elemento específico en una lista **ordenada** de elementos. Utiliza una estrategia de búsqueda de **"divide y vencerás"** para reducir la cantidad de elementos que debe revisar, **dividiendo** la lista a la **mitad** en cada iteración. Es uno de los algoritmos de búsqueda más rápidos y eficientes disponibles. 

---
### Utilizacion

El algoritmo de búsqueda binaria se utiliza comúnmente para encontrar elementos en un conjunto de datos ordenados como **listas**, **arreglos** o **matrices ordenadas**. También se utiliza para realizar búsquedas en bases de datos y para encontrar el elemento más próximo a un número dado en un conjunto de números.
Tomemos de ejemplo el catálogo estelar Tycho-2 una base de datos que contiene la posición, la magnitud y la clase espectral de más de 2.5 millones de estrellas. Supongamos que queremos buscar en el catálogo una estrella en particular, con base en el nombre de la estrella. Si el programa examinara cada estrella en el catálogo estelar en orden empezando con la primera, con un algoritmo llamado búsqueda lineal, la computadora podría, en el peor de los casos, tener que examinar todas las 2.5 millones de estrellas para encontrar la estrella que estás buscando. Si el catálogo estuviera ordenado alfabéticamente por nombres de estrellas, la búsqueda binaria no tendría que examinar más de 22 estrellas, incluso en el peor de los casos.

---

## Descripcion de los Pasos para crear el Algoritmo

1.  Definir el rango de búsqueda. El rango de búsqueda es el conjunto de elementos en los que se realizará la búsqueda. Esto puede ser una lista, un arreglo o una matriz. 

2. Ordenar los elementos del rango. El algoritmo de búsqueda binaria requiere que los elementos estén ordenados de forma ascendente. 

3. Establecer el punto medio. Esto se realiza dividiendo el número de elementos del rango por la mitad. 

4. Comparar el elemento en el punto medio con el elemento que se está buscando. Si el elemento es igual al elemento que se está buscando, se ha encontrado el elemento. Si el elemento es mayor, el elemento buscado debe estar en el rango inferior. Si el elemento es menor, el elemento buscado debe estar en el rango superior. 

5. Repita los pasos 3 y 4 hasta encontrar el elemento o hasta que el rango de búsqueda esté vacío. Si el rango de búsqueda está vacío, el elemento no se encuentra en el rango.










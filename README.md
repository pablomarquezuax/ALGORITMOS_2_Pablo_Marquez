# Segundo Examen Parcial Algoritmos

## Puedes ver este repositorio en linea en este link: https://github.com/pablomarquezuax/ALGORITMOS_2_Pablo_Marquez.git 

### Ejercicio Factorial

En este ejercicio se utiliza la recursividad ya que para calcular el factorial de un numero N, primero se calcula el factorial de N-1 y es precisamente el resultado de esta operación el que se multiplica por N. Si el valor de n es inicialmente igual a 0, automaticamente se dolverá 1 como resultado de la operación.


### Bubble Sort

El método de ordenación Bubble Sort es un algoritmo simple que funciona recorriendo repetidamente la lista, comparando elementos adyacentes y cambiándolos de posición si están en el orden incorrecto. 

**Cómo Funciona?**

- Comienza desde el primer elemento de la lista y compara cada par de elementos adyacentes.
- Si el elemento actual es mayor que el siguiente elemento, los intercambia.
- Continúa recorriendo la lista hasta llegar al final.
- Repite este proceso para cada elemento de la lista, hasta que la lista esté completamente ordenada.

**Ejemplo Conceptual:**

Tomemos la lista [34, 7, 23, 32, 5] y apliquemos el algoritmo Bubble Sort:

***Primera iteración:***

- Comparamos 34 y 7. Como 34 > 7, los intercambiamos. La lista se convierte en [7, 34, 23, 32, 5].
- Comparamos 34 y 23. No se intercambian.
- Comparamos 34 y 32. No se intercambian.
- Comparamos 34 y 5. Como 34 > 5, los intercambiamos. La lista se convierte en [7, 5, 23, 32, 34].


***Segunda iteración:***

- Comparamos 7 y 5. Como 7 > 5, los intercambiamos. La lista se convierte en [5, 7, 23, 32, 34].
- Comparamos 7 y 23. No se intercambian.
- Comparamos 23 y 32. No se intercambian.
- Comparamos 32 y 34. No se intercambian.


***Tercera iteración:***

- Comparamos 5 y 7. No se intercambian.
- Comparamos 7 y 23. No se intercambian.
- Comparamos 23 y 32. No se intercambian.
- Comparamos 32 y 34. No se intercambian.

***La lista está ahora ordenada: [5, 7, 23, 32, 34].***

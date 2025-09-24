<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Architects+Daughter&color=%23FF69B4&size=50&center=true&vCenter=true&height=60&width=600&lines=Proyectos+Estudiantiles!" alt="Title"></div>
---

## CONTEXTO

Este programa permite simular la evaluación de varios equipos en distintas rondas.  
Cada equipo recibe puntos según tres criterios: **innovación**, **presentación** y **errores**.  
Al final, se muestra un **ranking con los resultados**.

---

## BREVE EXPLICACIÓN DEL PROGRAMA

Lo que hace la aplicación es procesar los datos contenidos en el archivo `ACTIVIDAD1.ipynb`, utilizando métodos y estructuras de Python como:

- **Listas** y **diccionarios** para organizar los datos.
- El bucle `for`, que permite ejecutar distintas acciones sobre cada elemento, como:
  - Actualizar estadísticas acumuladas.
  - Calcular el puntaje de cada ronda.
  - Determinar el mejor equipo (**mer**).
  - Procesar los datos ronda por ronda y equipo por equipo.

También se utilizan métodos como:

- `.items()` → para recorrer los equipos evaluados en una ronda (dentro de un `for`).
- `.sorted()` → para ordenar el ranking por puntos.
- `.filter()` → para excluir equipos con puntaje negativo.
- `enumerate()` → para numerar las rondas en el bucle principal.

---

## FUNCIONES DEL PROGRAMA

Las funciones que hacen todos los cálculos están en el archivo:

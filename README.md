Simulador de Evaluaciones por Rondas

Este programa permite simular la evaluación de varios equipos en distintas rondas. Cada equipo recibe puntos según tres criterios: innovación, presentación y errores. Al final, se muestra un ranking con los resultados.
Basicamente lo que hace el programa lo que haces es:
- Toma los datos de evaluación de cada ronda.
- Asigna puntos según este criterio:
- Innovación: 3 puntos por unidad.
- Presentación: 1 punto por unidad.
- Errores: resta 1 punto si hubo errores.
- Calcula los totales por equipo.
- Muestra quién fue el mejor equipo de cada ronda (llamado "mer").
- Imprime una tabla con los resultados.
Todas las funciones están en src/funciones.py. Algunas de las más importantes son:
- simular_rondas: ejecuta todas las rondas.
- actualizar_estadisticas: calcula los puntos de cada ronda.
- mostrar_ranking: muestra los resultados ordenados.

Mis archivos son:
- ACTIVIDAD1.ipynb: es el archivo principal que ejecuta la simulación.
- src/funciones.py: contiene las funciones que hacen los cálculos y muestran los resultados.

Lo que necesito para usarlo es unicamente tener Python instalado. No se use librerías externas.



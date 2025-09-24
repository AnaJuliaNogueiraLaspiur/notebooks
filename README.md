✨Sistema de Evaluación de Proyectos Estudiantiles✨

## CONTEXTO
Este programa permite simular la evaluación de varios equipos en distintas rondas. Cada equipo recibe puntos según tres criterios: innovación, presentación y errores. Al final, se muestra un ranking con los resultados.

## BREVE EXPLICACION DEL PROGRAMA 
Lo que hace la aplicacion es procesar los datos contenidos en el archivo ACTIVIDAD1.ipynb, utilizando metodos y estrucutas de python como listas y diccionarios para organizar los datos. Para recorrer las estructras de datos use el for que me permite ejecutar distintas acciones sobre cada elemento como por ejemplo actualizar estadisticas acumuladas, sacar el puntaje de cada ronda, determinar el mejor equipo (mer). Es decir, lo use para procesar los datos ronda por ronda y equipo por equipo.
Ademas use metodos como .items() para recorrer los equipos evaluados en una ronda (lo use dentro de un for), .sorted() para ordenar el ranking por puntos, .filter() para excluir equipos con puntaje negativo y enumerate() para numerar las rondas en el bucle principal.

Las funciones que hacen todos los calculos estan en el archivo src/funciones.py

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Sistema de Evaluación de Proyectos Estudiantiles</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 40px;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2 {
      color: #2c3e50;
    }
    h1 {
      font-size: 2em;
      margin-bottom: 0.2em;
    }
    h2 {
      font-size: 1.5em;
      margin-top: 1.5em;
    }
    p {
      margin-bottom: 1em;
    }
    .highlight {
      background-color: #ffeaa7;
      padding: 0.2em 0.4em;
      border-radius: 4px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <h1>✨Sistema de Evaluación de Proyectos Estudiantiles✨</h1>

  <h2>CONTEXTO</h2>
  <p>
    Este programa permite simular la evaluación de varios equipos en distintas rondas. Cada equipo recibe puntos según tres criterios: innovación, presentación y errores. Al final, se muestra un ranking con los resultados.
  </p>

  <h2>BREVE EXPLICACION DEL PROGRAMA</h2>
  <p>
    Lo que hace la aplicacion es procesar los datos contenidos en el archivo <span class="highlight">ACTIVIDAD1.ipynb</span>, utilizando metodos y estrucutas de python como listas y diccionarios para organizar los datos.
  </p>
  <p>
    Para recorrer las estructras de datos use el <span class="highlight">for</span> que me permite ejecutar distintas acciones sobre cada elemento como por ejemplo actualizar estadisticas acumuladas, sacar el puntaje de cada ronda, determinar el mejor equipo (mer). Es decir, lo use para procesar los datos ronda por ronda y equipo por equipo.
  </p>
  <p>
    Ademas use metodos como <span class="highlight">.items()</span> para recorrer los equipos evaluados en una ronda (lo use dentro de un for), <span class="highlight">.sorted()</span> para ordenar el ranking por puntos, <span class="highlight">.filter()</span> para excluir equipos con puntaje negativo y <span class="highlight">enumerate()</span> para numerar las rondas en el bucle principal.
  </p>

  <p>
    Las funciones que hacen todos los calculos estan en el archivo <span class="highlight">src/funciones.py</span>
  </p>

</body>
</html>

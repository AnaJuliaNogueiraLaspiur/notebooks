# archivo: funciones.py

def crear_diccionario_estadisticas(equipos):
    """
    Inicializa un diccionario con las estadísticas de cada equipo en cero.
    parametros de ingreso: lista de equipos
    parametros de salida: diccionario con estadísticas inicializadas en cero
    
    """
    
    return {
        equipo: {'innovacion': 0, 'presentacion': 0, 'errores': 0, 'mer': 0, 'points': 0}
        for equipo in equipos
    }


def copiar_diccionario_con_ceros(diccionario_original): 
    """
    Crea una copia del diccionario con todas las estadísticas puestas a cero.
    parametros de ingreso: diccionario original
    parametros de salida: diccionario copiado con valores en cero       
    """
    return {
        clave: {k: 0 for k in subdic}
        for clave, subdic in diccionario_original.items()
    }

def mostrar_ranking(stats, titulo="Ranking total"):
    """
    Muestra un ranking ordenado por puntos, con todas las estadísticas.
    """
    stats_filtrados = dict(filter(lambda x: x[1]['points'] >= 0, stats.items()))
    ranking = sorted(stats_filtrados.items(), key=lambda x: x[1]['points'], reverse=True)

    print(f"\n{titulo}")
    print(f"{'Equipo':<10} {'INNOVACION':<12} {'PRESENTACION':<15} "
          f"{'ERRORES':<10} {'Puntos':<8} {'mer':<5}")
    print("-" * 70)
    for equipo, stat in ranking:
        mer_value = stat['mer'] if 'mer' in stat else '-'
        print(f"{equipo:<10} {stat['innovacion']:<12} {stat['presentacion']:<15} "
              f"{stat['errores']:<10} {stat['points']:<8} {mer_value:<5}")
    print("-" * 60)

def actualizar_estadisticas(evaluacion_data, estadisticas_equipos, points):
    """
    Calcula los puntajes de una ronda, actualiza las estadísticas acumuladas
    y determina el mer de la ronda.
    """
    mer = None
    max_puntos_ronda = float('-inf') #truco para que el primer puntaje siempre sea mayor

    
    evaluacion_data_stats = copiar_diccionario_con_ceros(estadisticas_equipos)

    
    for equipo, stats in evaluacion_data.items():
        innovacion = stats['innovacion']
        presentacion = stats['presentacion']
        errores = stats['errores']

        
        puntos_ronda = (innovacion * points['innovacion'] +
                        presentacion * points['presentacion'] +
                        (points['errores'] if errores else 0))

        
        evaluacion_data_stats[equipo]['innovacion'] = innovacion
        evaluacion_data_stats[equipo]['presentacion'] = presentacion
        evaluacion_data_stats[equipo]['errores'] = 1 if errores else 0
        evaluacion_data_stats[equipo]['points'] = puntos_ronda

        
        if mer is None or puntos_ronda > max_puntos_ronda:
            mer = equipo
            max_puntos_ronda = puntos_ronda

    if mer:
        evaluacion_data_stats[mer]['mer'] += 1

    
    mostrar_ranking(evaluacion_data_stats, f"Estadísticas de la ronda (mer: {mer})") #Llamo a la función que imprime la tabla SOLO de esa ronda.

    
    for equipo in estadisticas_equipos:
        estadisticas_equipos[equipo]['innovacion'] += evaluacion_data_stats[equipo]['innovacion']
        estadisticas_equipos[equipo]['presentacion'] += evaluacion_data_stats[equipo]['presentacion']
        estadisticas_equipos[equipo]['errores'] += evaluacion_data_stats[equipo]['errores']
        estadisticas_equipos[equipo]['points'] += evaluacion_data_stats[equipo]['points']
        estadisticas_equipos[equipo]['mer'] += evaluacion_data_stats[equipo]['mer']

    
    mostrar_ranking(estadisticas_equipos, "Estadísticas actualizadas")

    return mer

def simular_rondas(evaluaciones, diccionario_puntos):
    """
    Ejecuta la simulación de todas las rondas y muestra los resultados.
    """
    equipos = list(evaluaciones[0].keys())
    estadisticas_equipos = crear_diccionario_estadisticas(equipos)

    for round_num, round_data in enumerate(evaluaciones, 1):
        print(f"\nRonda {round_num}:")
        actualizar_estadisticas(round_data, estadisticas_equipos, diccionario_puntos)
        print("_" * 100)

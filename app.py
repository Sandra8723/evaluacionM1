notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}
def promedio(calificaciones):
    for alumno,calificaciones in notas_estudiantes.items():
      promedio=sum(calificaciones)/len(calificaciones)  
      print(f"El promedio: {promedio}")


promedio(promedio)
    
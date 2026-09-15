


# Este programa calculará el promedio de un estudiante basado en 5 calificaciones ingresadas por el usuario.
# Si el promedio es mayor o igual a 6.0, el estudiante aprobará; entre 4.0 y 5.9 el estudiante estará en 
#  recuperación; y si es menor a 4.0, el estudiante reprobará.

print("Bienvenido al programa de cálculo de promedio de calificaciones.")
estudiante = input("Ingrese el nombre del estudiante: ")
calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))
calificacion4 = float(input("Ingrese la cuarta calificación: "))
calificacion5 = float(input("Ingrese la quinta calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

if promedio >= 6.0:
    print(f"El promedio es {promedio}. ¡Felicidades! {estudiante}, Has aprobado.")
elif promedio >= 4.0:
    print(f"El promedio es {promedio}. {estudiante}, Estás en recuperación.")
else:
    print(f"El promedio es {promedio}. {estudiante}, Has reprobado.") 
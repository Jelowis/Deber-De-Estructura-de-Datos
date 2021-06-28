'''Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen
DEFINICIÓN DEL PROBLEMA
El mismo enunciado.
ANÁLISIS DEL PROBLEMA
Salidas: mensaje de aprobado si se cumple la condición.
Entradas: calificación
Datos adicionales:   un alumno aprueba si la calificación es mayor o igual que 7.'''

nota = float(input("Ingrese su nota:"))
if nota < 7:
    print("Usted reprobo")
elif nota >= 7:
    print ("Usted aprobo")
else:
    print("Ingrese un valor correcto")
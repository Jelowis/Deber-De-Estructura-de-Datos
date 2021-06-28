#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
# si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

sueldo = float(input("Ingrese su sueldo: "))
a=600
if sueldo > a:
    op1 = (sueldo+a*0.10)
    print(f"Su nuevo sueldo sera de: ${op1}")
else:
    print("Usted no recibe aumento.")
'''Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
 El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las 
 tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su 
 sueldo base y sus comisiones'''

sueldo = float(input("Ingrese el sueldo:"))
a = float(input("Ingresa la venta 1:"))
b = float(input("Ingresa la venta 2:"))
c = float(input("Ingresa la venta 3:"))
comision = (a+b+c)*0.10
print(f"El sueldo del trabajador es : ${sueldo}")
print(f"La comision de las 3 ventas es: ${comision}")
print (f"El sueldo final es: ${sueldo+comision}")
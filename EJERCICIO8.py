#En una tienda se ofrece un descuento del 15% sobre el total de la 
# compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

precio = float(input("Digite el precio:"))
descuento = precio * 0.15
preciof = precio- descuento
print (f"El precio que debe pagar es de: ${preciof:.2f} ")


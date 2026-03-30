#Calculo de un producto con IVA incluido

base = int(input("Ingrese el valor base del producto: " ))
iva = float(input("Ingrese el procentaje del IVA:  " ))

total_iva = (base * iva)
print(f"El valor del IVA es: $ {total_iva}")

total_iva_incluido = (base + total_iva)
print(f"El valor del final del producto con IVA incluido es: $ {total_iva_incluido}")
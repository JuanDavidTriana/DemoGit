print("Hola Mundo para GitHub 1")


numero = int(15)

print("LA suma es: ", numero)
numero2=int(20)

print(numero - numero2)

notas = [3.5, 4.2, 3.8, 3.6, 4.1, 4.3, 3.9, 3.7, 4.0, 4.4,
        3.5, 4.2, 3.6, 4.0, 3.9, 4.1, 3.8, 4.2, 3.5, 4.3,
        3.7, 4.0, 3.6, 4.5, 3.9, 4.1, 3.5, 4.2, 3.8, 3.7,
        4.0, 4.2, 3.6, 3.9, 4.4, 3.5, 4.1, 3.8, 4.0, 3.6]

aprobados = 0
reprobados = 0
umbral = 4

for nota in notas:
    if nota >= 4:
        aprobados += 1
    else:
        reprobados += 1

print(f"Total de notas: {len(notas)}, Aprobados: {aprobados}, Reprobados: {reprobados}")

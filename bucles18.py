maikoll = 0
contador_impares = 0

while maikoll < 22:
    if maikoll % 2 != 0:
        contador_impares += 1
    maikoll += 1

print(f"Hay {contador_impares} números impares")

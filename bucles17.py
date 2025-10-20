maikoll = 0
contador_pares = 0

while maikoll < 22:
    if maikoll % 2 == 0:
        contador_pares += 1
    maikoll += 1

print(f"Hay {contador_pares} números pares")

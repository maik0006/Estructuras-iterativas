#Contar cuántos números divisibles entre 3 hay del 1 al 100.
maikoll = 1
n_divisibles = 0

while maikoll < 101:
    if maikoll % 3 == 0 :
        print(f"{maikoll} es divisible por 3")
        n_divisibles += 1
    maikoll += 1

print(f"Hay {n_divisibles} números divisibles entre 3 del 1 al 100")

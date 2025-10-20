maikoll = int(input("Ingresa un número: "))
daniel = 1
torres = 1

while daniel <= maikoll:
    torres *= daniel
    daniel += 1

print(f"El factorial de {maikoll} es: {torres}")

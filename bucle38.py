maikoll = "Hola mundo desde Python"
daniel = 0
for torres in maikoll:
    if torres.lower() in "aeiou":
        daniel += 1
print("Vocales:", daniel)

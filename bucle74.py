maikoll = [2, 5, 8, 11, 14]
daniel = []
for torres in maikoll:
    if torres % 2 == 0:
        daniel.append(torres)
print(sum(daniel) / len(daniel))

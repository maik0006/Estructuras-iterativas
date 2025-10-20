maikoll = [10, 5, 3, 9, -2, 4]
daniel = 1
torres = maikoll[0]

while daniel < len(maikoll):
    if maikoll[daniel] < torres:
        torres = maikoll[daniel]
    daniel += 1

print("El número menor es:", torres)

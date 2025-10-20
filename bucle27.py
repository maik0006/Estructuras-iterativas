maikoll = [1, -5, 0, 7, -3, 0, 8, -2]
daniel = 0
torres = 0  
fandiño = 0  
torres1 = 0  

while daniel < len(maikoll):
    if maikoll[daniel] > 0:
        torres += 1
    elif maikoll[daniel] < 0:
        fandiño += 1
    else:
        torres1 += 1
    daniel += 1

print("Positivos:", torres)
print("Negativos:", fandiño)
print("Ceros:", torres1)

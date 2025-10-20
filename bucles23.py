#Contar cuántas vocales hay en una cadena de texto (utilizando for sobre la cadena).
maikoll=("Hola")
torres_n_vocales=0
for torres in maikoll:
    
    if torres == ("a"):
        torres_n_vocales+=1

    elif torres == ("e"):
        torres_n_vocales+=1

    elif torres == ("i"):
        torres_n_vocales+=1

    elif torres == ("o"):
        torres_n_vocales+=1

    elif torres == ("u"):
        torres_n_vocales+=1


print(f"El numero de vocales en {maikoll} es de: {torres_n_vocales}")

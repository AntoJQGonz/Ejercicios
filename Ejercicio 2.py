#Dispones de frase y una letra, solicitados al usuario y debes mostrar la cantidad de veces que aparece la letra en la frase.

frase = input("Dime una frase: ")
letra = input("Elige una letra: ")
# resultado = frase.count(letra)

item = 0
for item in frase:
    if item == letra:
        item += 1
        print(item)


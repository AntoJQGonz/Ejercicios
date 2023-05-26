"""Crea una variable que sea una letra, si es una a muestra el número 7, si es una b, el 9, si es una c el 101 y si no es
ninguno de los tres, indica que se han equivocado de letra"""


variable = input("Elige una letra del abecedario: ").lower()
if variable == "a":
    print(7)
elif variable == "b":
    print(9)
elif variable == "c":
    print(101)
else:
    print("Te has equivocado de letra")

"""Dispones de tres números enteros H, M, S correspondientes a hora, minutos y segundos respectivamente,
debes comprobar si se trata de una hora válida."""
hora = int(input("Dime en qué hora estamos: "))
minutos = int(input("Dime en qué minuto estamos: "))
segundos =int(input("Dime en qué segundo estamos: "))

if hora in range(0, 24) and minutos in range (0, 61) and segundos in range(0, 61):
    print("La hora es correcta")
else:
    print("La hora es incorrecta")
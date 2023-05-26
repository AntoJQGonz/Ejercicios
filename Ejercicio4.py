"""Permite validar a un usuario con 3 intentos y los datos de validación correctos almacenados en dos
constantes predefinidas."""

usuario = "Antonio"
clave = "123456"
login = False
userClave = int(0)

intentos = 3

while not login and not intentos == 0:
    user = input("Introduzca su nombre de usuario: ")
    userClave = input("Introduzca la contraseña numérica: ")
    if user != usuario and userClave != clave:
        print("Contraseña o usuario incorrectos")
        intentos -= 1
        print(f"Te quedan {intentos} intentos")
    else:
        print("Usuario y contraseña correctos")
        login = True

if intentos == 0:
    print("Estás bloqueado")


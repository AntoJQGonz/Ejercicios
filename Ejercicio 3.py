print("Bienvenido a nuestra calculadora que solo suma y resta")
n1 = int(input("Diga un número: "))
n2 = int(input("Diga otro número: "))
elección = input("Diga 'suma' para sumar o 'resta' para restar ")
resultado = 0

if elección == "suma":
    resultado = n1 + n2
    print(f"El resultado de sumar {n1} más {n2} es {resultado} ")
else:
    resultado = n1 - n2
    print(f"El resultado de restar {n1} menos {n2} es {resultado} ")



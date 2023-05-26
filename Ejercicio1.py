#Indicar cuál es el menor de tres enteros solicitados al usuario

n1= int(input("Di un número: "))
n2= int(input("Dime otro número: "))
n3= int(input("Dime el tercer número: "))

if n1 < n2 and n3:
    print(f"{n1} es el menor de todos")
elif n2< n1 and n3:
    print(f"{n2} es el número menor de todos")
else:
    print(f"{n3} es el número menor de todos")


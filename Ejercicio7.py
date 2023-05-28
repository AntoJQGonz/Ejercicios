"""Solicita al usuario dos fechas del mismo año e indica la cantidad de días que hay entre ellas."""
día1 = int(input("Hola usuario1, tienes que decirme día:\n"))
mes1= int(input("Ahora tienes que decirme un mes del año en número:\n"))
día2 = int(input("Hola usuario2, tienes que decirme día:\n"))
mes2= int(input("Ahora tienes que decirme un mes del año en número:\n"))

díasMeses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

díasQuedanMes1 = 0
sumaMesesCompletos= 0
total= 0

if mes1 < mes2:
    díasQuedanMes1 = díasMeses[mes1] - día1
    sumaMesesCompletos = díasMeses[mes1 + 1] + díasMeses[mes2] + día2
    total = díasQuedanMes1 + sumaMesesCompletos
    print(f"La diferencia en días entre ambas fechas es {total}")

elif mes2 == mes2:
    total = día2 - día1
    print(f"La diferencia en días entre ambas fechas es {total}")

else:
    print("No se pueden hacer viajes al pasado")

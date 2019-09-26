SUE=float(input("ingrese el sueldo del trabajador:$  "))
AUM=SUE*0.15
NSUE=SUE+AUM
if SUE < 1000:
    print(f"El trabajador tendra un amunto del 15%, siendo su nuevo sueldo :${NSUE}.")
if SUE >= 1000:
    print(f"Usted no tiene derecho a un aumento de sueldo")


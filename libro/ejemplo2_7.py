NUM=int(input("escribe el valor de NUM: "))
V=int(input("Ingreso otro numero entero"))
VAL=0
if NUM==1:
    VAL= 100*V
elif NUM==2:
    VAL=100**V
elif NUM==3:
    VAL=100/V
else:
    VAL=0
print(VAL)
print("Fin del programa")

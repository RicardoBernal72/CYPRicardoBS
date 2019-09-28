A=float(input("Variable a: "))
B=float(input("Variable b: "))
C=float(input("variable c: "))
HOLA=B**2 -4*A*C
if HOLA>=0:
    X1=((-B)+HOLA*.5)/2*A
    X2=((-B)-HOLA*.5)/2*A
    print(f"Las incognitas de tu ecuacion son X1= {X1} y X2= {X2}.")
if HOLA<0:
    print(f"no se puede escribir las raices puesto que {HOLA} es negativo.")


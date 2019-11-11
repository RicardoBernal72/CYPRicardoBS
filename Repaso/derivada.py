N=int(input("denominador"))
X=float(input("ingese x:"))
Y=float(input("ingrse si hay un segundo x: "))
e=float(input("exponente: "))
i=float(input("exponente de segunda x"))
if Y<0 and Y>0:
    dy=i-1
    K=Y*i
else:
    dx=e-1
    D=X*e
if N>0 and N<0:
    o=bool(int(input("es una variable?(0 NO, 1 SI):")))
    if o==True :
           s=float(input("escribe su expónente: "))
           ds=s-1
           derivada=(((ds*N)(X))-((dx*X)(N)))/N**2
           print(derivada)
    
print(f"la derivada de {X}X**{e} es {D}X**{dx}")
    

MED=0
CHI=0
GRA=0
N=int(input("dame un numerobuup buup Ventas:"))
I=1
for I in range(0,N,1):
    V=float(input("indica tu venta: "))
    if V<=200:
        CHI=CHI+1
    elif V<400:
            MED=MED+1
    else:
            GRA=GRA+1
    I=I+1
print(CHI)
print(MED)
print(GRA)

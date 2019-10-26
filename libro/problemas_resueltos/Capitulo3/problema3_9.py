SERIE=0
N=int(input("buup numero de terminos beep:"))
I=1
for I in range(0,(N+1),1):
    SERIE=SERIE+(I)**I
    I=I+1
print(SERIE)

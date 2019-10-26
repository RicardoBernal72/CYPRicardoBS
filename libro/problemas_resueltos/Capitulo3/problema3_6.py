MAY=-100000
MEN=100000
N=int(input("num de enteros que se ingresan"))
I=1
for I in range(0,N,1):
    NUM=int(input("num enetro"))
    if NUM>MAY:
        MAY=NUM
    elif NUM<MEN:
            MEN=NUM
    else:
            I=I+1
print(MAY)
print(MEN)

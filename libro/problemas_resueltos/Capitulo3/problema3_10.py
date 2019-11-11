PRI=0
SEG=1
I=3
while I<7:
    SIG=PRI+SEG
    PRI=SEG
    SEG=SIG
    I=I+1
print(SIG)

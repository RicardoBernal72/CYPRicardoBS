CAN1=0
CAN2=0
CAN3=0
CAN4=0
VOTO=int(input("elige a ru candidato"))
while VOTO>0:
    if VOTO==1:
        CAN1=CAN1+1
    if VOTO==2:
        CAN2=CAN2+1
    if VOTO==3:
        CAN3=CAN3+1
    if VOTO==4:
        CAN4=CAN4+1
    VOTO=int(input("elige a ru candidato"))
SUMV=CAN1+CAN2+CAN3+CAN4
POR1=(CAN1/SUMV)*100
POR2=(CAN2/SUMV)*100
POR3=(CAN3/SUMV)*100
POR4=(CAN4/SUMV)*100
print(CAN1)
print(CAN2)
print(CAN3)
print(CAN4)

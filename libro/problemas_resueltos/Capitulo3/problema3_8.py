NUM=int(input("bep introduzca un numero positivo buuup bep:"))
if NUM>0:
    while NUM>1:
        x=(-1)**NUM
        if x>0:
            NUM=NUM/2
        if x<0:
            NUM=(NUM*3)+1
    print(NUM)
        
else:
    print("NUM Tine que ser un entero positivo")
            

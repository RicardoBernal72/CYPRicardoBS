PREBA=float(input("Precio BASE del producto: "))
if PREBA>500:
    IMP=20*.30+(PREBA-40)*.50
    PRETOT=IMP+PREBA
    print(PRETOT)
if PREBA>40:
    IMP=20*.30(PREBA-40)*.40
    PRETOT=IMP+PREBA
    print(PRETOT)
if PREBA>20:
    IMP=20*.30(PREBA-20)*.30
    PRETOT=IMP+PREBA
    print(PRETOT)
else:
    IMP=0
    PRETOT=IMP+PREBA
    print(PRETOT)


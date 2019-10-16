SUE=float(input("Sueldo basico del trabajador: "))
CATE=int(input("Categoria del trabajador: "))
HE=int(input("horas extras trabajadas: "))
PHE=0
if CATE==1:
    PHE=30
if CATE==2:
    PHE=38
if CATE==3:
    PHE=50
if CATE==4:
    PHE=70

if HE>30:
    NSUE=SUE+30*PHE
else:
    NSUE=SUE+HE*PHE
print(PHE)
print("su nuevo sueldo es",NSUE)


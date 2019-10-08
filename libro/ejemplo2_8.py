CATE=int(input("Categoria del trabajador(1-4-4)): "))
SUE=float(input("Sueldo del trabajador: $"))
if CATE==1:
    NSUE=SUE*1.15
elif CATE==2:
    NSUE=SUE*1.10
elif CATE==3:
    NSUE=SUE*1.08
elif CATE==4:
    NSUE=SUE*1.07
else:
    CATE==0
    print("usted no esta entre las categorias que recibiran aumento")
    NSUE=("No tiene derecho a aumento")
print(f"El Nuevo sueldo de este trabajador es de ${NSUE} ")


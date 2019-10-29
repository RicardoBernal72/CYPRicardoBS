N= int(input("ingrese el numero de elementos del arreglo:"))
VEC=[]

if N>=1 and N<=500:
    #logica
    for I in range(0,N,1):
        VEC.append(int(input("ingresa un valor:")))
    VEC.sort()
    print(VEC)
    print(f"lista de numeros sin repeticiones:")
    while I<= (N-1):
        print(VEC[I])
        REPET=VEC[I]
        while I<= (N-1) and REPET == VEC[I]:
            I+=1
else:
    print("El numero de elementos del arreglo es incorrecto:")

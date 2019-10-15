Cuecer=0
N=int(input("un numero entero positivo: "))
for Z in range(0,N,1):
    NUM=int(input("ingresa un entero:"))
    if NUM==0:
        Cuecer += 1
print(f"el numero de ceros capturados fue {Cuecer}")

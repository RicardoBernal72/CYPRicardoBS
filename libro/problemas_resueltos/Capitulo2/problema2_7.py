A=int(input("dame un numero: "))
B=int(input("dame un numero: "))
C=int(input("el ultimo numero: "))
if A<B:
    if B<C:
        print("los numeros estan en orden creciente")
    else:
        print("los numeros no estan en orden creciente")
else:
    print("los numeros no estan en orden creciente")

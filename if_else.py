Edad = int(input("dame tu edad: "))
INE = bool(int(input("tienes INE ( 0 NO / 1 SI)?: ")))
if Edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puede entrar al bar")
else:
    print("Eres menor de edad")
    print("pudes ir a jugar LOL")
print("fin del programa")

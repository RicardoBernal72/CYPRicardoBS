edad= int (input("dame tu edad:  "))
INE = bool(int(input("tienes INE (0 NO / 1 SI: ")))
if edad>= 18 and INE == True:
    print("Es mayor de edad")
    print("puedes entrar al Bar")
if edad<18:
    print("fin del programa")

L1=float(input("lado 1: "))
L2=float(input("lado 2: "))
L3=float(input("lado 3: "))
S=(L1+L2+L3)/2
Area=(S*(S-L1)*(S-L2)*(S-L3))**(1/2)
print(Area)

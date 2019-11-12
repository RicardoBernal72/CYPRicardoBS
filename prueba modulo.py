#import modulos
#modulos.mi_print("Hola")

from modulos import mi_print,otro_print,sumar,restar
import time
import sys
from asciistuff import Banner
mi_print("Hola de nuevo")
otro_print("Hola k ase")
print(sumar(4,5))
print(restar(5,4))
#from modulos import * (te importa todas las funciones)
for i in range(2,0,-1):
    print(i,"...")
    time.sleep(.2)
print(Banner("QUESO"))
print(sys.platform)

def sumar(x , y):
    z=x+y
    return z
def restar (x , y):
    return x-y

def mi_print(texto):
    print("Este es mi pr", texto)

def multiplica(valor,veces):
    if veces == None:
        print("debes enviar el segundo argumento de la funcion")
    else:
        print(valor*veces)

def comanda(mesa, comensal, entrada , medio, fuerte, postre="Queso Manchego"):
    print("Mesa", mesa,"comensal",comensal)
    print("entrada",entrada)
    print("segundo timpo",medio)
    print("plato fuerte",fuerte)
    print("postre",postre)

def imprime_argumentos(*argumentos):
   for ele in argumentos:
       print(ele)

def comanda2(**comida):
    llaves= comida.keys()
    for elem in llaves:
        print(elem,"->", comida[elem])

def main():
    a=10
    b=5
    c= sumar(a,b)
    print("la suma es",c)
    c= restar(a,b)
    print("la resta es",c)
if __name__=='__main__':
    main()
mi_print("hola¡¡¡¡")
multiplica(10, 3)
multiplica(10, None)
multiplica('hola', 3)
comanda(2,1,"Ensalada","sopa","filete(bien rikolino)(/º-º)/","Flan")
comanda(entrada="ensalada",fuerte="filete",comensal=3, mesa=1, medio="sopa")
print("--------------------------")
#{}
comanda2(entrada="ensalada",fuerte="filete",comensal=3, mesa=1, medio="sopa",postre="strudel de Manzana",bebida='agua de horchata')

#diccionario es un estructura de datos no ordenadas que almacenan informacion por pares de tipo valor {:}, y siempre son string(str)
#Diccionarios {'llave':'valor'}
alumno={'num_cta':'20164', 'nombre':'jose' , 'paterno':'perez'}

print(alumno['nombre'])
alumno={'num_cta':'20164',
        'nombre':'Ricardo',
        'paterno':'Bernal',
        'semestre':1,
        'promedio':0.0,
        'materias':['Cyp','algebra','calculo','geometria','intro ICO'],
        'regular':True,
        'lagrimasporex':5,
        'direccion':{
            'calle':'francisco villa',
            'numero':28,
            'cp':14070,
            'del_num':'Tlalpan',
            'colonia':'Romulo Sanchez Mireles',
            'estado':{
                'id':15,
                'nombre':'Ciudad de Mexico',
                'corto':'EDOMEX'
                }
            }
        }
print(alumno['nombre'])
print(alumno)
print(alumno['nombre'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['materias'][1:3:])
mi_lista=[['a','b'],['c',10],['d',True]]
diccionario = dict(mi_lista)
print(diccionario)
print(alumno['materias'][1].upper())
print(alumno['direccion']['estado']['nombre'][10::].upper())
alumno['lagrimasporex']=10
print(alumno)

#son mutables

alumno['cursa_inglès']=True
print(alumno)

#funcion keys ()
llaves = alumno.keys()
print(llaves)
for llave in llaves:
    print("------------------")
    print(llave)
    print('......................')
    print(alumno[llave])
    print("+++++++++++++++++++++")
#funciones Values
for val in alumno.values():
    print('......')
    print(val)
    print('++++++++++++++++')
#funcion item
for elem in alumno.items():
    print('..............')
    print(elem)

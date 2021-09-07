#Argumentos y parametros indeterminados

# Primer  Caso :  Por posicion

def resta(a,b):
    pass

def  validar_tipos_datos(*args): # "*args"  Es un estandar : Manejar con tuplas

    print("tipo args", type(args))
    sub_tupla = args[0:4]

    print(sub_tupla)

    for arg in args:
        print(f"arg : type : {type(arg)}")

#Argumentos indeterminados
validar_tipos_datos(5,10,5.2,"Hola",[1,2,3,4])
#                   0  1  2     3       4

# Segundo Caso por NOmbre
# Las estructuras de datos  llamados Dicionarios

print("Indeterminados por Nombre : Diccionarios")

def  validar_tipos_datos_kw(**Kwargs):  # **Kwargs   enviado de argumentos via dicionarios : d = {k:v}
    print(Kwargs)
    for k in Kwargs:
        print(f"llave : [{k}] = {Kwargs[k]}")


validar_tipos_datos_kw(numero1=5, cadena='Hola', lista1=[1,2,3], flotante=1.5)


#Ejemplos
print("-----EJEMPLOS----")
def sumar(a,b,c,d,e,f):
    return a+b+c+d+e+f

print(f"El resultado de sumar : {sumar(2,4,6,8,10,70)}")

def sumar_args(*args):
    suma_total = 0
    for num in args:
        suma_total += num
    return suma_total

print(f"El resultado de sumar_args : {sumar_args()}")



















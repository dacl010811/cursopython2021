def convertir():
    a = '10a'
    cadena_1 = ''
    lista_num = []

    for car in (list(a)):    # Lista ['1','0','a']
        if isinstance(car,str):
            try:
                print(type(car))
                numerico = int(car)
                lista_num.append(numerico)
            except:
                print("No pudo realizar el castin")

    print("Mi numero es ", str(lista_num))

convertir()
convertir()
from datetime import datetime

fecha =  datetime.datetime.now()
print(fecha)

#Acceder al año
print(fecha.year)

#Acceder al mes
print(fecha.month)

#Acceder al dia
print(fecha.day)

#Acceder al dia
print(fecha.hour)
print(fecha.minute)
print(fecha.second)
print(fecha.microsecond)

#Metodos de la clase datetime
#Time Zone
print(fecha.timetz())

print(f"{fecha.hour}h{fecha.minute}m{fecha.second}seg")

#Crear un datetime

print("Creando Fechas Manualmente")
fecha_2 = None

try:
    fecha_2 = datetime(2022,2,28,21,21,21)
except TypeError:
    print("Error - TypeError: - Error en tipos de datos")
except ValueError:
    print("Error - ValueError: - Error en los valor amo mes o dia")
except Exception as e:
    print(type(e).__name__)

print(fecha_2)

#Remplazar componentes de las fechas
fecha_3 = datetime.now()
print(f"Inicio : {fecha_3}")
#Forma 1
fecha_3 = fecha_3.replace(year=2025)
fecha_3 = fecha_3.replace(month=12)
# Forma 2 :  Desencadenar funciones
fecha_3 = fecha_3.replace(year=2025).replace(month=12)

print(f"Fin : {fecha_3}")

print("Formato automatico  ISO")
#Formatear  Fechas
fecha_4  = datetime.now()
resultado = fecha_4.isoformat()
print(resultado)

#Formateo manual de las fechas

fecha_5  = datetime.now()
fecha_5 = fecha_5.strftime("%A %d %B %Y %I:%M %p - %X - %x :  %a ")
print(fecha_5)

#Operaciones con fechas

print("Operaciones")

fecha_6 = datetime.now()
print("Inicio : ",fecha_6)

time_delta = datetime.timedelta(days=15, hours=4, minutes=20)
print(time_delta)









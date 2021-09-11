#Operaciones con fechas
import datetime

print("Operaciones")

fecha_6 = datetime.datetime.now()
print("Inicio : ",fecha_6)

time_delta = datetime.timedelta(days=15, hours=4, minutes=20)
print(time_delta)

#Suma
resultado =  fecha_6 + time_delta
print(f"Suma delta {resultado}")


#resta
resta =  fecha_6 - time_delta
print(f"Resta delta {resta}")

#producto
producto =  10 * time_delta
print(f"Producto delta {producto}")



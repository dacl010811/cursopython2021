"""try:
    n = input("Introduce un número: ")
    5/n
except TypeError:
    print("No se puede dividir el número por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print( type(e).__name__ )"""

def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")

#mi_funcion()

def mi_funcion_lista():
    lista = [1,2,3,4,5,6,7,]
    try:
        lista[1] = lista[1/0]
    except ZeroDivisionError:
        print("Error Division por Cero")
    except TypeError:
        print("Error de Tipo de Dato")
    except IndexError:
        print("Error de Index")
    except Exception as e:
        print("Error General")
        print(f"Error General : {type(e).__name__}")
    else:
        pass
    finally:
        pass


mi_funcion_lista()
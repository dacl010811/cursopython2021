# -*- coding: utf-8 -*-
from  io import open

def lectura_personas():
    fichero = open('personas.txt','r')
    lineas_archivo = fichero.readlines()
    fichero.close()

    lista_personas = []

    for linea in lineas_archivo:
        campos = linea.replace("\n","").split(";")
        persona =  {"id":campos[0], "nombre":campos[1],"apellido":campos[2], "nacimiento":campos[3]}
        lista_personas.append(persona)

    for persona in lista_personas:
        print(f"Persona : {persona['id']} - {persona['nombre']} - {persona['apellido']} - {persona['nacimiento']}")


lectura_personas()


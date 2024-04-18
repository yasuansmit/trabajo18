list_id = []
list_nombreComp = []
list_identificacion = []
list_correo = []
list_contacto = []
list_edad = []
list_añosDExp = []
list_profesion = []
list_ciudad = []
lsit_sexo = []

import os
def fnt_limpiar():
    os.system("")
    print("Autor: Yasuan Smith C")
    print("Fecha: 2024-04-18\n\n")
def fnt_registrar(nombreComp, identificacion, correo, contacto, edad, añosDExp, profesion, ciudad):
    if id == " " or nombreComp == " " or list_identificacion == " " or list_correo == " " or list_contacto == " " or list_edad == " " or list_añosDExp == " " or list_profesion == " " or list_ciudad == " ":
        enter = input("\nError debe ingresar todos los datos <ENTER>")
    else:
        list_id.append(id)
        list_nombreComp.append(nombreComp)
        list_identificacion.append(identificacion)
        list_correo.append(correo)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_añosDExp.append(añosDExp)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        fnt_limpiar()
        enter = input("\nRegistro exitoso <ENTER>")
def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == "1":
        id = input("Id: ")
        if id in list_id:
            enter = input("\nEl id ya existe <ENTER>")
        else:
            nombreComp = input("Nombre completo: ")
            identificacion = input("Identificacion: ")
            correo = input("Correo: ")
            contacto = input("Contacto: ")
            edad = input("Edad: ")
            añosDexp = input("Años de experiencia: ")
            profesion = input("Profesion: ")
            ciudad = input("Ciudad: ")
            fnt_registrar(nombreComp, identificacion, correo, contacto, edad, añosDexp, profesion, ciudad)
sw = True
while sw == True:
    fnt_limpiar()
    op = input("\n\n 1.ANTES DE QUE SE REGISTRE DEBE TENER DE 25 A 30 Años,\n 2-SER INGENIERO EN SISTEMAS O FORMATICO\n 3- 2 O 4 AÑOS DE EXPERIENCIA\n<<< MENU PRINCIPAL >>> \n1. Registrar\n2. Seleccionar\n3. Salir\n")
    fnt_selector(op)
    







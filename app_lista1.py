list_id = []
list_name = []
list_contact = []
list_e_mail = []
import os
def fnt_limpiar():
    os.system("cls")
    print("Autor: Yasuan Smith C")
    print("Fecha: 2024-04-18\n\n")

def fnt_registrar(id, name, contact, e_mail):
    if id == "" or name == " " or e_mail == "" or contact == "":
        enter = input("\n Error, debe ingresar todo los datos <ENTER>")
    else:
        list_id.append(id)
        list_name.append(name)
        list_contact.append(contact)
        list_e_mail.append(e_mail)
        enter = input("\n Registro exitoso <ENTER>")
def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == "1":
        id = input("id: ")
        if id in list_id:
            enter = input("\n Error, el id ya existe <ENTER>")
        else:
            name = input("Nombre: ")
            contact = input("Contacto: ")
            e_mail = input("Email: ")
        fnt_registrar(id, name, contact, e_mail)
    elif opcion == "2":
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'{list_id[i]}     {list_name[i]}     {list_contact[i]}     {list_e_mail[i]}')
        enter = input("\n Seleccionar opcion <ENTER> para continuar")
sw = True
while sw == True:
    fnt_limpiar()
    op = input("\n\n<<<<<< MENU PRINCIPAL >>>>>>>> \n1. REGISTRAR \n2. CONSULTAR \n3. SALIR\n-> ")
    fnt_selector(op)



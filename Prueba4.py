"""
Prueba Parcial 4
"""

#
#Profe compasion a la hora de revisar porfavor :)
#

usuarios = {
    "nombres":[],
    "generos":[],
    "contraseñas":[],
}

Confirmation = False

print("Bienvenido al sistema de administracion de usuarios de Fio!!")


def agregar_usuarios():
    nombre = input("Ingrese su nombre: ")
    for n in usuarios["nombres"]:
        if nombre == n:
            print("El usuario ya esta registrado")
            
    if True:    
        genero = input("Ingrese su genero con una F, M o c: ")
        if genero.lower() == "F" or "M" or "c":
            Confirmation == True
        else:
            print("Debe de ingresar una de las opciones anteriormente mencionadas")



    if Confirmation == True:  
        contraseña = input("Ingrese su contraseña: ")
        if len(contraseña) >= 8 and Confirmation == True:
            usuarios["nombres"].append(nombre)
            usuarios["generos"].append(genero)
            usuarios["contraseñas"].append(contraseña)

###

def buscar_usuarios():
    nombre = input("Ingrese el nombre del usuario que busca: ")
    num = 0
    for n in usuarios["nombres"]:
        num += 1
        if nombre == n:
            print(f"Usuario: {usuarios["nombres"][num-1]}")
            print(f"Genero: {usuarios["generos"][num-1]}")
            print(f"Contraseña: {usuarios["Contraseñas"][num-1]}")

###


def eliminar_usuarios():
    nombre = input("Ingrese el nombre de usuario a eliminar: ")
    for n in usuarios["nombres"]:
        num+=1
        if num == n:
            usuarios.pop(["nombre",num-1][num-1])
            print(f"{usuarios}" "Usuario Eliminado.")



print("1.- Ingrese usuario: ")
print("2.- Buscar usuario: ")
print("3.- Eliminar Usuario: ")
print("4.- Salir. ")

option = 0
option = int(input("Ingrese su opcion a continuacion: "))

match option:
    case 1:
        agregar_usuarios()

    case 2:
        buscar_usuarios()

    case 3:
        eliminar_usuarios()

    case 4:
        print("Gracias por su preferencia !!")
    
    case _:
        print("Debe seleccionar una de las opciones anteriores")

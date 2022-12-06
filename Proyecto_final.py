#enconding: utf-8    
import os 
running = True
os.system('clear')
print("------------------------------------------------------")
print("|Bienvenido al sistema dehistorys clinicas del 🏥🏥|")
print("------------------------------------------------------")


#********************
#*VARIABLES GLOBALES*
#********************

running = True
#database = list()
database = [{'nombre': 'juan', 'history': 'resfrio'}, {'nombre': 'maria', 'history': 'parto natural'}, {'nombre': 'matias', 'history': 'dolor de cabeza'}, {'nombre': 'juan', 'history': 'dolor de panza'}, {'nombre': 'patricio', 'history': 'transgenero'}]
#********************
#*FUNCIONES GLOBALES*
#********************

def show_menu():
    print("") 
    print("") 
    print("\t\t") 
    print("🔵 1 - Cargar Pacientes") 
    print("🔵 2 - Buscar Pacientes") 
    print("🔵 3 - Listar Pacientes") 
    print("🔴 4 - Salir") 
    print("") 
    res = input("INGRESE UNA OPCION ➡️ \t") 
    os.system('clear')
    return res
def response_validate(r):
    validated = False
    num_res = 0
        
    if response.isdigit():
        num_res = int(response)
        if num_res >= 1 and num_res <= 4:
            msg = "estan en rango"
            validated = True
        else :
            msg = "Fuera de rango"
    else:
        msg = "Entrada incorrecta, por favor ingrese un numero"
    return validated, num_res, msg
#****************
#*LOOP PRINCIPAL*
#****************

while running:
    response = show_menu()
    validated, num_res, msg = response_validate(response)
    if validated: 
        if num_res == 1:
            name = input("Ingrese el nombre del paciente ➡️ ")
            history = input("Ingrese historia clinica del paciente ➡️ ")
            paciente = {"nombre":name, "history":history}
            database.append(paciente)

            print(database)
        elif num_res == 2:
            name = input("Ingrese el nombre del paciente  ▶ ")

            finded = True
            for x in range(len(database)):
                if  database[x]['nombre'].lower() == name.lower():
                    print("")
                    print("PACIENTE ENCONTADO | H. CLINICA ▶ ",database[x]['nombre'])
                    print("PACIENTE ENCONTADO | H. CLINICA ▶ ",database[x]['history'])
                    print("")
                else:
                    finded = False
            if not finded :
                print("paciente no encontrado! :(")

        elif num_res == 3:
            print(" -----------------------")
            print("| LISTADO DE PACIENTES |")
            print(" -----------------------")
            for x in range(len(database)):
                print("Nombre ▶ ".ljust(10), database[x]['nombre'],"\t\t Historia C ▶ ".ljust(10), database[x]['history'])
            
            print(" --------------")
            print("| FIN DE LISTA |")
            print(" --------------")
                
        else :
            print(" -----------------------")
            print("| APLICACION FINALIZADA |")
            print(" -----------------------")
            running = False
    else:
            print(msg)
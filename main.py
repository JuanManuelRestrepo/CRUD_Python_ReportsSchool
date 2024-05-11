#crear un menu para que el usuario pueda elegir que desea hacer (NO HACERLO DENTRO DE NA FUNCION, SINO EN UN CONDICIONAL)
print("Welcome")
#Creamos la lista donde se almacenaran las notas de los estudiantes
List_notas=[]
#creamo el diccionario donde se guardaran las keys con los valores de cda nua de ellas 
estudiante={}
ruta="C:/Users/USUARIO/OneDrive/Escritorio/Prueba_git/CRUD_Python_ReportsSchool"
nombre_archivo="Grupo 1.txt"
archivo= ruta + nombre_archivo


def guardar_notas(List_notas, archivo):
    try:
        # Leer el archivo para obtener el último número asignado previamente
        with open(archivo, "r") as documento:
            lineas = documento.readlines()  # Leer todas las líneas del archivo
            if lineas:  # Verificar si hay al menos una línea en el archivo
                ultimo_numero = int(lineas[-1].split("-")[0].split(":")[-1].strip())
            else:
                ultimo_numero = 0
    except FileNotFoundError:
        # Si el archivo no existe, iniciar desde 1
        ultimo_numero = 0

    # Abrir el archivo en modo de adición ("a") para agregar el nuevo registro
    documento = open(archivo, "a")
    for i, estudiante in enumerate(List_notas, ultimo_numero + 1):
            documento.write(f'id: {i} - {estudiante["Nombre"]} - {estudiante["Identificación"]} - {estudiante["Nota"]}\n')
    documento.close()

#Funcionalidad de promedio
def Promedio(archivo):
    #Inicializar las variables de suma de las notas registradas
    #Inicializar un contador para conocer el numero de registros conocidos
    suma_total=0
    num_ids=0 

    #abrimos el archivo en modo lectura
    with open(archivo,"r") as documento:
        #iteramos por cada linea dentro del archivo
        for linea in documento:
            #la variable suma una por cada id encontrado 
            num_ids+=1
            #separamos la linea por el caracter "-"
            partes=linea.split("-")
            #separamos la ultima parte de la linea por el caracter "- "
            #y extraemos el ultimo elemento de la lista que es la nota
            nota=float(partes[-1].strip())

            #sumamos la nota a la variable suma_total
            suma_total+=nota

        # Si no hay id, la operación no se puede hacer 
        if num_ids==0: 
            print("No hay notas registradas")

        #Realizamos la operació para obtener el promedio   
        else:
            promedio=suma_total/num_ids
            print(f"El promedio del grupo es: {round(promedio,2)}")

def Analisis_datos(archivo):
    #declaramos contadores de aprobados y reprobados
    cont_aprob=0
    cont_repro=0
    n_est=0
    #abrimos el archivo en modo lectura
    with open(archivo, "r") as documento:
        #iteramos por cada linea dentro del archivo
        for linea in documento:
            #la variable suma una por cada id encontrado
            n_est+=1
            partes=linea.split("-")
            # en la variable nota almacenamos cada una de las notas del arhivo
            nota=float(partes[-1].strip())

            #Validaciones de aprobados y reprobados
            if nota>=3:
                cont_aprob+=1
            else:
                cont_repro+=1
        if n_est==0:
                print("No hay estudiantes registrados")
    print(f"EL numero de estudiantes que aprobaron fueron: {cont_aprob}")
    print(f"El numero de estudiantes reprobados es de: {cont_repro}")


def Grupode_finido(): 
    #definimos el numero de estudiantes del grupo
    N_estudiantes=int(input("Digite el numero de estudiantes del curso: "))
    print("NOTAS 0-5")
    #creamos un bucle desde 1 hasta el numero de estudiantes del curso
    for i in range(1,N_estudiantes+1): 

        #Inputs de los estudiantes
        nombre=input(f"Digite el nombre  del estudiante {i}: ")
        identificacion=(input(f"Digite el numero de identificación del estudiante{i}: "))
        while True:  # Repetir hasta que la calificación sea válida
            calificacion = float(input(f'Digite la calificacion del estudiante {i}: '))
            if 0.0 <= calificacion <= 5.0:
                break  # Salir del bucle si la calificación es válida, sale del bucle while
            else: # si la calificacion no es valida, la vuelve a pedir 
                print("La calificación debe estar entre 0 y 5. Inténtelo de nuevo.") 
        #cada dato del estudiante se guarda en un diccionario 
        #Cada ckey tiene el calor asignado al estudiante correspondiente        
        estudiante={"Nombre": nombre , 
                    "Identificación": identificacion,
                     "Nota":calificacion }   
        #Se guarda el diccionario en una lista
        List_notas.append(estudiante)
    guardar_notas(List_notas,archivo)
    
    return List_notas


def Editar_Estudiante():
    # Solicitar al usuario que ingrese el ID del estudiante que desea editar
    indice = input("Digite el ID del estudiante que desea editar: ")

    try:    
        # Abrir el archivo en modo lectura
        with open(archivo, "r") as documento:
            lineas = documento.readlines()  # Leer todas las líneas del archivo

        # Variable para indicar si se encontró el ID
        id_encontrado = False
            
        # Iterar sobre cada línea del archivo para buscar el ID y mostrar los datos si se encuentra
        for linea in lineas:
            #Dividimos la linea por cada caracter " - "
            partes = linea.strip().split(" - ")
            #Si el ID de la linea es igual al ID que se ingreso, se imprime la linea
            if partes[0].split(": ")[1] == indice:
                id_encontrado = True
                # Mostrar los datos actuales del estudiante
                print("Datos actuales del estudiante:")
                print(f"Nombre: {partes[1]}")
                print(f"Identificación: {partes[2]}")
                print(f"Calificación: {partes[3]}")
                break
        
        # Verificar si se encontró el ID
        if id_encontrado:
            # Abrir el archivo en modo escritura para sobrescribirlo
            with open(archivo, "w") as documento:
                # Iterar sobre cada línea del archivo para realizar la edición si es necesario
                for linea in lineas:
                    partes = linea.strip().split(" - ")
                    if partes[0].split(": ")[1] == indice:
                        # Realizar la edición solicitando los nuevos datos al usuario
                        nuevo_nombre = input("Digite el nuevo nombre: ")
                        nueva_identificacion = input("Digite la nueva identificación: ")
                        nueva_calificacion = float(input("Digite la nueva calificación: "))
                        
                        nueva_linea = f"id: {indice} - {nuevo_nombre} - {nueva_identificacion} - {nueva_calificacion}\n"
                        documento.write(nueva_linea)
                    else:
                        documento.write(linea)
            print("Los datos del estudiante han sido actualizados correctamente.")
        else:
            print(f"No se encontró ningún estudiante con el ID {indice}") 

    except FileNotFoundError:
        print("El archivo no existe.")


    
def Agregar_estudiante_dinamicamente(): 
    while True:
        nombre = input("Digite el nombre del estudiante: ")
        identificacion = input("Digite el número de identificación del estudiante: ")
        calificacion = float(input("Digite la calificación del estudiante: "))

        while not 1 <= calificacion <= 5:
            # Si la calificación no está en el rango correcto, pedir al usuario que ingrese nuevamente la calificación
            print("La calificación debe estar entre 1 y 5. Inténtelo de nuevo.") 
            calificacion = float(input("Digite la calificación del estudiante: "))

        # Crear el diccionario para el estudiante y agregarlo a la lista
        estudiante = {"Nombre": nombre, "Identificación": identificacion, "Nota": calificacion}
        List_notas.append(estudiante)

        guardar_notas(List_notas, archivo)  # Guardar las notas en el archivo

        respuesta = input("¿Desea agregar otro estudiante? (Sí/No): ").lower()
        if respuesta != "si":
            break  # Salir del bucle si el usuario no desea agregar más estudiantes
    return List_notas

def Listar_estudiantes_texto():
    with open(archivo,"r") as documento:
        for linea in documento:
            print(linea)



     
while True:   
    # Menu de opciones del programa
    print("----------------------------------------------------------------------------------------------")
    print("BIENVENIDO AL MENU PRINCIPAL")
    decision=int(input("1.Definir tamaño grupo \n2.Agregar notas dinamicamente \n3.Promedio Notas \n4.Mostrar datos de las notas \n5.Listar\n6.Editar usuario\n7.Salir del programa \nDigite la opcion: "))
    if decision==1: 
        Grupode_finido() 
        while True: 
            # Menu de opciones del programa
            print("--------------------------------------------------------------------------------------------")
            opciones = int(input("1.Promedio Notas \n2.Analisis de las notas \n3.Listar\n4.Salir \nDigite la opcion: "))
            if opciones == 1:       
                Promedio(archivo)
            elif opciones == 2:
                Analisis_datos(archivo)
                pass  # Aquí podrías llamar a una función para realizar análisis si lo deseas
            elif opciones == 3:
                Listar_estudiantes_texto()
                pass  # Aquí podrías llamar a una función para mostrar los datos de las notas si lo deseas
            elif opciones == 4:
                break

    elif(decision==2):
        Agregar_estudiante_dinamicamente()

    elif(decision==3): 
        Promedio(archivo)
    elif(decision==4): 
        Analisis_datos(archivo)
    elif(decision==5): 
        Listar_estudiantes_texto()
    elif(decision==6): 
        Editar_Estudiante()
    elif(decision>=7): 
        print("FUE UN PLACER")
        break
    elif(decision<=0):
        print("Opcion no valida")
        break

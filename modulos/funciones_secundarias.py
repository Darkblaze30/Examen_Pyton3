#Módulo que me sirve para guardar opciones secundarias
import json
from datetime import datetime


#Función que me permite  validar la entrada númerica de un archivo
def v_numerica(minimo,maximo):

    #Manejo de errores
    try:

        #Pido el dato a validar
        num = int(input(f"Ingresa tú respuesta en el rango {minimo} - {maximo} : "))

        #Ciclo para validar el dato este en el rango
        while num < minimo or num > maximo:
            num = int(input(f"ups !! Por favor ingresa tú respuesta en el rango {minimo} - {maximo} : "))
        
        #Devuelvo el dato
        return num
    
    #Manejo de errores
    except ValueError as error:

        #Misma lógica que el código dentro del try: de arriba
        num = int(input(f"Error de tipo {error} !!Ingresa tú respuesta en el rango {minimo} - {maximo} : "))
        while num < minimo or num > maximo:
            num = int(input(f"ups !! Por favor ingresa tú respuesta en el rango {minimo} - {maximo} : "))
        return num
    


#Función que me permite validar si un dato esta en una posición dada en una lista    
def v_dato(dato,lista,posicion1,posicion2):


    #Inicio una variable bandera
    comprobacion = False


    #For para que me recorra lo que hay en lista en busca del dato
    for contador in lista:

        #Sí encunetra lo que busca comprobar es True
        if contador[posicion1][posicion2] == dato:
            comprobacion = True
            break

    #Devuelvo el valor de comprovar por medio de un if y un else
    if comprobacion:
        return True
    else:
        return False
    

#Función qu8e me valida su un dato es númerico
def v_cantidad(mensaje):


    #Manejo de error por medio de un try:
    try:

        #Pido el valor a validar
        cantidad = float(input(mensaje))

        #Devulvo el valor de cantidad
        return cantidad
    
    #Manejo el error capturado y pido el dato nuevamente
    except ValueError as error :
        cantidad = float(input(f"Error {error}, {mensaje}"))

        #Devuelvo el valor de cantidad
        return cantidad
    

#Función que me valida una entrada alfabetica
def v_alfabetica(mensaje):


    #Pido la respuesta del ususario
    dato = input(mensaje).lower()

    #Si la respuesta no es valida, entra a un while hasta que sea la deseada
    while dato not in ["no","si"]:
        dato = input("Por favor ingresa una opción correcta (si/no) : ")

    #Devielvo un valor de verdad segín el valor de dato
    if dato == "si":
        return False
    else:
        return True


#Función que me carga los archivos a una lista
def cargar_archivos(archivo):

    #Manejo de errores
    try:
        with open(archivo,"r") as file:
            lista = json.load(file)
            return lista
        
    #En caso de error devuelvo una lista vacia
    except FileNotFoundError:
        return []
    except FileExistsError:
        return []


#Función que me guarda en el archivo lo que tenga una lista
def a_data(lista,archivo):

    with open(archivo,"w") as file:
        json.dump(lista,file, indent=3)
    print("GUARDADO EXITOSAMENTE !! ")


def menu_meses():
    print("!!MES A REGISTRAR !!")
    print("1. Enero")
    print("2. Febrero")
    print("3. Marzo")
    print("4. Abril")
    print("5. Mayo")
    print("6. Junio")
    print("7. Julio")
    print("8. Agosto")
    print("9. septiembre")
    print("10. Octubre")
    print("11. Noviembre")
    print("12. Diciembre")

    respuesta = v_numerica(1,12)

    return respuesta


def fecha_actual():

    fecha = datetime.now()

    dia = fecha.strftime("%d")
    mes = fecha.strftime("%m")
    year = fecha.strftime("%Y")

    return dia,mes,year

def fecha():

    dia_actual,mes_actual,year_actual = fecha_actual()

    try:
        print("DÍA EN NÚMEROS !! ")
        year = v_cantidad("AÑO : ")
        while year > year_actual:
            year = v_cantidad("INGRESA UN AÑO QUE NO SOBREPASE EL AÑO ACTUAL : ")
        if year == year_actual:
            mes = menu_meses()
            while mes > mes_actual:
                mes = v_cantidad("INGRESA UN MÉS QUE NO SOBREPASE LA FECHA ACTUAL ")
            dia = v_cantidad("DÍA : ")
            while dia > dia_actual:
                dia = v_cantidad("DÍA : ")
        mes = menu_meses()
        dia = v_numerica(1,31)

    except ValueError:
        print("Error !!, INGRESE LOS DATOS CORRECTAMENTE")
        print("DÍA EN NÚMEROS !! ")

        print("DÍA EN NÚMEROS !! ")
        year = v_cantidad("AÑO : ")
        while year > year_actual:
            year = v_cantidad("INGRESA UN AÑO QUE NO SOBREPASE EL AÑO ACTUAL : ")
        if year == year_actual:
            mes = menu_meses()
            while mes > mes_actual:
                mes = v_cantidad("INGRESA UN MÉS QUE NO SOBREPASE LA FECHA ACTUAL ")
            dia = v_cantidad("DÍA : ")
            while dia > dia_actual:
                dia = v_cantidad("DÍA : ")
        mes = menu_meses()
        dia = v_numerica(1,31)
    return dia,mes,year

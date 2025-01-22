#Espacio donde importo lo que necesito para las funciones de mi módulo
from modulos.funciones_secundarias import cargar_archivos,v_dato,v_cantidad,v_alfabetica, a_data, fecha
from modulos.funciones_secundarias import fecha

def faltas():

    salida = True

    while salida:

        ced = input("----> CÉDULA : ")
        
        lista_nomina = []
        lista_nomina = cargar_archivos("nomina.json")

        #Compruebo la  cedula en la lista_nomina
        comprobacion = v_dato(ced,lista_nomina,'persona','ced')


        #Devuelve el valor de comprobacion, en caso de ser False, pide la data para guardarla
        if comprobacion:
            lista_faltas = []
            lista_faltas = cargar_archivos("faltas.py")
            dia,mes = fecha()

            lista_faltas.append({"persona":{"ced": ced, "falta": 1, "dia": dia , "mes" : mes}})
            a_data(lista_faltas,"falta.json")


            

        else:

            print(f"CÓDIGO {ced} NO EXISTE EN NÓMINA")

        #Pregunto si quiere salir
        salida = v_alfabetica("¿Quierés salir? (si/no) ")

def bonos():
    salida = True

    while salida:

        ced = input("----> CÉDULA : ")
        
        lista_nomina = []
        lista_nomina = cargar_archivos("nomina.json")

        #Compruebo la  cedula en la lista_nomina
        comprobacion = v_dato(ced,lista_nomina,'persona','ced')


        #Devuelve el valor de comprobacion, en caso de ser False, pide la data para guardarla
        if comprobacion:
            lista_faltas = []
            lista_faltas = cargar_archivos("bonos.py")

            dia, mes = fecha()

            lista_faltas.append({"persona":{"ced": ced, "bono": v_cantidad("---> CANTIDAD :"), "dia": dia, "mes": mes}})
            a_data(lista_faltas,"falta.json")


            

        else:

            print(f"CÓDIGO {ced} NO EXISTE EN NÓMINA")

        #Pregunto si quiere salir
        salida = v_alfabetica("¿Quierés salir? (si/no) ")
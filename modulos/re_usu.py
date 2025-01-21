#Espacio para importar lo que necesito para mi módulo
from modulos.funciones_secundarias import cargar_archivos,v_dato,v_cantidad,v_alfabetica, a_data

#Función que me guarda las personas en el archivo nomina
def i_usuario():

    salida = True

    while salida:
        
        #Pioo la cedula
        ced = (input("----> CÉDULA : "))


        #Inicio y cargo la data a la lista lista_nomina
        lista_nomina = []
        lista_nomina = cargar_archivos("nomina.json")

        #Compruebo la  cedula en la lista_nomina
        comprobacion = v_dato(ced,lista_nomina,'persona','ced')


        #Devuelve el valor de comprobacion, en caso de ser False, pide la data para guardarla
        if comprobacion:
            print(f"CÓDIGO {ced} YA EXISTE EN NÓMINA")
        else:
            lista_nomina.append({"persona":{"ced": ced, "nombre": input("-----> NOMBRE : "), "salario": v_cantidad("---->SALARIO : "),"cargo": input("---->CARGO :")}})
            a_data(lista_nomina,"nomina.json")

        #Pregunto si quiere salir
        salida = v_alfabetica("¿Quierés salir? (si/no) ")
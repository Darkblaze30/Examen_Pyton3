#Espacio donde importo lo que necesito para mi módulo
from modulos.funciones_secundarias import v_numerica

#Función que me imprime el menú principal y me captura en valor de respuesta
def menu_principal():
    print("0. Salir")
    print("1. Registrar Empleado")
    print("2. Registro de  Inasistencias")
    print("3. Registro de bonos")
    print("4. Buscar Salario De Un empleado")
    print("5. Generar Salarios De La Nómina")

    respuesta = v_numerica(0,5)

    return respuesta


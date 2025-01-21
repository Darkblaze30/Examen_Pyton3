#Espacio para impotar lo que necesito para mi main.py
from modulos.menu import menu_principal
from modulos.re_usu import i_usuario
from modulos.re_novedades import faltas,bonos

#Inicio de la ejecución
while True:
    respuesta = menu_principal()
    match respuesta:
        case 0:
            break
        case 1:
            i_usuario()
        case 2:
            faltas()
        case 3:
            bonos()
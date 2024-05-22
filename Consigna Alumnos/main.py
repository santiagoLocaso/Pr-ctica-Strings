"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""

from class_video import Video
from data import lista_videos

bandera_ingreso = False
bandera_seguir = True


while bandera_seguir == True:

    opcion = int(input("\n1.NORMALIZAR OBJETOS\n2.MOSTRAR TEMAS\n3.ORDENAR TEMAS\n4.PROMEDIO DE VISTAS\n5.MAXIMA REPRODUCCION\n6.BUSQUEDA POR CODIGO\n7.LISTAR POR COLABORADOR\n8.LISTAR POR MES\n9.SALIR\nElija una opcion: \n"))

    match opcion:
        #A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización de videos que nos solicitan.
        case 1:
            for i in lista_videos:
                i.dividir_titulo()
                i.obtener_codigo_url()
                i.formatear_fecha()
                print()
        case 2:
            # B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
            for i in lista_videos:
                i.dividir_titulo()
                print()
        case 3:
            # C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
            for i in lista_videos:
                i.dividir_titulo()
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            bandera_seguir = False
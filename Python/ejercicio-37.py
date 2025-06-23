# 37. Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

def determinar_momento_del_dia():
    try:
        hora = int(input("Introduce solo la hora: "))
        if  not 0 <= hora <= 23:
            raise IndexError("Introduzca un numero entre 0 y 23")
        print("Es por la mañana" if 6 <= hora < 12 else ( "Es por la tarde" if 12 <= hora < 21 else "Es por la noche"))
    except ValueError:
        print("Introduzca numeros")
    except IndexError as e:
        print(e)

determinar_momento_del_dia()
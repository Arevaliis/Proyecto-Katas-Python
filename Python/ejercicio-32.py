# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista 
# y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

empleados = [
    {"nombre": "Ana Gomez", "puesto": "Gerente de Ventas"},
    {"nombre": "Carlos Perez", "puesto": "Analista de Datos"},
    {"nombre": "Elena Rodriguez", "puesto": "Desarrolladora Backend"},
    {"nombre": "Javier Lopez", "puesto": "Disenador UX/UI"},
    {"nombre": "Maria Fernandez", "puesto": "Especialista en Marketing"},
    {"nombre": "Pedro Ramirez", "puesto": "Soporte Tecnico"},
    {"nombre": "Sofia Mendez", "puesto": "Contadora"},
    {"nombre": "Tomas Herrera", "puesto": "Ingeniero de Software"}
]

def buscar_empleados(name, lista_empleados):
    for trabajador in lista_empleados:
        nombre, puesto = trabajador.values()
        if nombre == name:
            print(f"{nombre} trabaja de {puesto}")   
            return     
    print(f"{name} no trabaja aqui")

buscar_empleados("Tomas Herrera", empleados)
buscar_empleados("Juan Garcia", empleados)
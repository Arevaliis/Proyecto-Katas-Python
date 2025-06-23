""" 
40. Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. 

- El programa debe:
    1. Solicitar al usuario el precio original de un artículo.
    2. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    3. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    4. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    5. Mostrar el precio final de la compra, considerando o no el descuento.
    6. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
"""

def calcular_precio():
    try: 
        precio_inicial = float(input("¿Cual es el precio del producto?: "))
        if precio_inicial > 0:        
            tiene_descuento = input("¿Tienes Descuento? (S/N): ").upper()
            if tiene_descuento == "S":
                valor_descuento = int(input("¿Cual es el valor del descuento?: (1-100%)"))
                if 1 <= valor_descuento <= 100:
                    print(f"El precio final de la compra es de {precio_inicial * (1 - (valor_descuento / 100))}€.")
                else:
                    print("El descuento no puede ser mejor que 1 ni mayor que 100.")
                    print(f"El precio final de la compra es de {precio_inicial}€.")
            else: 
                print(f"El precio final de la compra es de {precio_inicial}€.")
        else:
            print("El precio debe ser mayor a 0")
    except ValueError:
        print("Ingrese numeros.")

calcular_precio()
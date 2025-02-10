PRECIO_POR_KILO = 5.0 

def calcular_descuento(kilos):
    if 0 <= kilos <= 2:
        return 0.10 
    elif 2.01 <= kilos <= 5:
        return 0.20  
    elif 5.01 <= kilos <= 10:
        return 0.30  
    elif kilos > 10:
        return 0.40  
    else:
        return 0  

def calcular_total_a_pagar(kilos):
    descuento = calcular_descuento(kilos)
    subtotal = PRECIO_POR_KILO * kilos
    descuento_aplicado = subtotal * descuento
    total_a_pagar = subtotal - descuento_aplicado
    return subtotal, descuento_aplicado, total_a_pagar

def menu():
    while True:
        print("\n--- Frutería Vitalidad ---")
        print("Seleccione la cantidad de kilos de mandarinas que desea comprar.")
        print("Para salir, ingrese '0'.")
        
        try:
            kilos = float(input("Cantidad de kilos de mandarinas: "))
            
            if kilos == 0:
                print("Gracias por visitar la frutería Vitalidad.")
                break
            
            if kilos < 0:
                print("Por favor, ingrese un número positivo de kilos.")
                continue

            subtotal, descuento_aplicado, total_a_pagar = calcular_total_a_pagar(kilos)
            
            print(f"\nSubtotal: {subtotal:.2f}")
            print(f"Descuento aplicado: {descuento_aplicado:.2f}")
            print(f"Total a pagar: {total_a_pagar:.2f}")

        except ValueError:
            print("Por favor, ingrese un valor numérico válido para la cantidad de kilos.")

menu()
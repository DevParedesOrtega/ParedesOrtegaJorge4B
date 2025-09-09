#Diagnostico_JorgeParedesOrtega
#Simulador de pedidos
#Conceptos basicos: variables, inputs, condicionales, funciones y bucles

# Simulador de pedidos - versión mínima
productos = ["Cargador tipo C", "Cubo cargador USB", "Audifonos inalambricos"]
precios = [150.0, 200.0, 500.0]  # números, no strings

def calcular_total(cantidades, precios):
    total = 0.0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

print("Menú de tec shop, ¡bienvenido!")
nombre = input("Ingresa tu nombre: ")

cantidades = []
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]:.2f}")
    c = int(input(f"¿Cuántos {productos[i]} deseas? "))
    cantidades.append(c)

total = calcular_total(cantidades, precios)
print(f"\nGracias por tu compra, {nombre}. Total a pagar: ${total:.2f}")

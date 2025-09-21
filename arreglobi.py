departamentos = ["Ropa", "Deportes", "Juguetería"]
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
         "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

# Matriz inicializada en 0
ventas = [[0 for _ in range(len(meses))] for _ in range(len(departamentos))]

def insertar_venta():
    print("Seleccione el departamento:")
    for i, d in enumerate(departamentos):
        print(f"{i} - {d}")
    depto = int(input("Opción: "))

    mes = int(input("Seleccione el mes (0=Enero ... 11=Diciembre): "))
    monto = float(input("Ingrese la venta: "))

    ventas[depto][mes] = monto
    print("Venta registrada con éxito.")

def buscar_venta():
    monto = float(input("Ingrese el monto a buscar: "))
    encontrado = False
    for i in range(len(departamentos)):
        for j in range(len(meses)):
            if ventas[i][j] == monto:
                print(f"Encontrado ${monto} en {departamentos[i]} - {meses[j]}")
                encontrado = True
    if not encontrado:
        print("No se encontró la venta.")

def eliminar_venta():
    print("Seleccione el departamento:")
    for i, d in enumerate(departamentos):
        print(f"{i} - {d}")
    depto = int(input("Opción: "))

    mes = int(input("Seleccione el mes (0=Enero ... 11=Diciembre): "))
    ventas[depto][mes] = 0
    print("Venta eliminada correctamente.")

def mostrar_ventas():
    for i, d in enumerate(departamentos):
        print(f"{d}: ", end="")
        for j, m in enumerate(meses):
            print(f"{m}={ventas[i][j]} | ", end="")
        print()

# --- Menú principal ---
while True:
    print("\n--- Menú ---")
    print("1. Insertar venta")
    print("2. Buscar venta")
    print("3. Eliminar venta")
    print("4. Mostrar todas las ventas")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        insertar_venta()
    elif opcion == "2":
        buscar_venta()
    elif opcion == "3":
        eliminar_venta()
    elif opcion == "4":
        mostrar_ventas()
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")

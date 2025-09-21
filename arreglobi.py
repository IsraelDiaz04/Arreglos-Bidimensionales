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

    try:
        mes = int(input("Seleccione el mes (0=Enero ... 11=Diciembre): "))
        if mes < 0 or mes >= len(meses):
            print(" Mes inválido, debe estar entre 0 y 11.")
            return
    except ValueError:
        print(" 1Debes ingresar un número entero para el mes.")
        return

    try:
        monto = float(input("Ingrese la venta: "))
    except ValueError:
        print(" Debes ingresar un número válido para la venta.")
        return

    ventas[depto][mes] = monto
    print("Venta registrada con éxito.")

def buscar_venta():
    print("Seleccione el departamento:")
    for i, d in enumerate(departamentos):
        print(f"{i} - {d}")
    depto = int(input("Opción: "))

    mes = int(input("Seleccione el mes (0=Enero ... 11=Diciembre): "))

    monto = ventas[depto][mes]
    if monto != 0:
        print(f"Venta encontrada: ${monto} en {departamentos[depto]} - {meses[mes]}")
    else:
        print("No hay venta registrada en esa posición.")

def eliminar_venta():
    print("Seleccione el departamento:")
    for i, d in enumerate(departamentos):
        print(f"{i} - {d}")
    depto = int(input("Opción: "))

    mes = int(input("Seleccione el mes (0=Enero ... 11=Diciembre): "))

    if ventas[depto][mes] != 0:
        ventas[depto][mes] = 0
        print(f"Venta eliminada en {departamentos[depto]} - {meses[mes]}")
    else:
        print("No había venta registrada en esa posición.")

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

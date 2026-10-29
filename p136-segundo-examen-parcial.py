# ============================================================
# AeroRegistro
# Registro de vuelos con diccionarios, listas, sets y tuplas.
# ============================================================


# ============================================================
# FASE 1: CAPTURA
# Cada vuelo se guarda en un diccionario; todos los diccionarios
# se agregan a una lista principal (el inventario).
# ============================================================
inventario = []  # Lista de diccionarios (un diccionario por vuelo)

print("=== AeroRegistro ===")
print("Para terminar la captura, deja vacío el número de vuelo o escribe *\n")

while True:
    # El número de vuelo se pide primero porque también controla la salida
    numero_vuelo = input("Número de vuelo (ej. AA-101): ").strip().upper()

    # Condición de término: entrada vacía o "*"
    if numero_vuelo == "" or numero_vuelo == "*":
        break

    # Origen: se repite la pregunta mientras quede vacío
    while True:
        origen = input("Origen (ej. Ciudad de México): ").strip().title()
        if origen != "":
            break
        print("El origen no puede estar vacío.")

    # Destino: se repite la pregunta mientras quede vacío
    while True:
        destino = input("Destino (ej. Guadalajara): ").strip().title()
        if destino != "":
            break
        print("El destino no puede estar vacío.")

    # Aerolínea: se repite la pregunta mientras quede vacía
    while True:
        aerolinea = input("Aerolínea (ej. Volaris): ").strip().title()
        if aerolinea != "":
            break
        print("La aerolínea no puede estar vacía.")

    # Pasajeros: debe ser un entero no negativo
    while True:
        try:
            pasajeros = int(input("Pasajeros a bordo: "))
            if pasajeros < 0:
                print("Los pasajeros no pueden ser negativos.")
                continue
            break
        except ValueError:  # El usuario escribió algo que no es entero
            print("Entrada inválida. Escribe un número entero.")

    # Tarifa: debe ser un decimal no negativo
    while True:
        try:
            tarifa = float(input("Tarifa del boleto (pesos): "))
            if tarifa < 0:
                print("La tarifa no puede ser negativa.")
                continue
            break
        except ValueError:  # El usuario escribió algo que no es número
            print("Entrada inválida. Escribe un número (ej. 2350.75).")

    # Diccionario con los datos de un solo vuelo
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa,
    }
    inventario.append(vuelo)  # Se agrega a la lista principal
    print(f"Vuelo {numero_vuelo} registrado.\n")


# ============================================================
# FASE 2: COLECCIONES ESPECIALES
# Set: destinos sin repetir.
# Lista de tuplas: registro histórico inmutable.
# ============================================================
destinos_unicos = set()    # Set vacío (no permite elementos repetidos)
registro_inmutable = []    # Lista de tuplas (numero_vuelo, aerolinea, destino)

for vuelo in inventario:
    destinos_unicos.add(vuelo["destino"])  # Si ya existe, add() lo ignora
    registro_inmutable.append(
        (vuelo["numero_vuelo"], vuelo["aerolinea"], vuelo["destino"])
    )  # Cada tupla ya no se puede modificar


# ============================================================
# FASE 3: VISUALIZACIÓN
# Datos crudos, tabla alineada, set y tuplas.
# ============================================================
if len(inventario) == 0:
    # Evita imprimir estructuras vacías si no se capturó nada
    print("\nNo se registró ningún vuelo.")
else:
    # Datos crudos: la lista de diccionarios tal como se almacenó
    print("\n" + "=" * 60)
    print("DATOS CRUDOS (lista de diccionarios)")
    print("=" * 60)
    print(inventario)

    # Tabla: < alinea a la izquierda, > a la derecha, el número es el ancho
    print("\n" + "=" * 60)
    print("TABLA DE VUELOS")
    print("=" * 60)

    encabezado = (
        f"{'No. Vuelo':<10} {'Origen':<20} {'Destino':<20} "
        f"{'Aerolínea':<15} {'Pasajeros':>9} {'Tarifa':>12}"
    )
    print(encabezado)
    print("-" * len(encabezado))  # Línea separadora del mismo largo

    for v in inventario:
        print(
            f"{v['numero_vuelo']:<10} {v['origen']:<20} {v['destino']:<20} "
            f"{v['aerolinea']:<15} {v['pasajeros']:>9} "
            f"{'$' + format(v['tarifa'], ',.2f'):>12}"
        )

    # Set de destinos únicos
    print("\n" + "=" * 60)
    print("DESTINOS ÚNICOS (set)")
    print("=" * 60)
    print(destinos_unicos)

    # Lista de tuplas
    print("\n" + "=" * 60)
    print("REGISTRO INMUTABLE (lista de tuplas)")
    print("=" * 60)
    print(registro_inmutable)


# ============================================================
# FASE 4: CÁLCULOS
# Conteos, sumas, promedios, máximo y mínimo en un solo recorrido.
# ============================================================
if len(inventario) > 0:  # Protege contra división entre cero

    # Contadores y acumuladores
    total_vuelos = len(inventario)
    vuelos_por_aerolinea = {}  # Diccionario usado como contador
    vuelos_por_destino = {}    # Diccionario usado como contador
    total_pasajeros = 0
    total_tarifas = 0.0

    # El primer vuelo sirve de referencia inicial para máximo y mínimo
    vuelo_mas_caro = inventario[0]
    vuelo_mas_barato = inventario[0]

    for v in inventario:
        # get(clave, 0) devuelve 0 si la clave aún no existe
        vuelos_por_aerolinea[v["aerolinea"]] = vuelos_por_aerolinea.get(v["aerolinea"], 0) + 1
        vuelos_por_destino[v["destino"]] = vuelos_por_destino.get(v["destino"], 0) + 1

        total_pasajeros += v["pasajeros"]
        total_tarifas += v["tarifa"]  # Una sola tarifa por vuelo

        # Comparación estricta: en empate se conserva el primero capturado
        if v["tarifa"] > vuelo_mas_caro["tarifa"]:
            vuelo_mas_caro = v
        if v["tarifa"] < vuelo_mas_barato["tarifa"]:
            vuelo_mas_barato = v

    # Promedios
    promedio_pasajeros = total_pasajeros / total_vuelos
    promedio_tarifa = total_tarifas / total_vuelos

    # Impresión del resumen
    print("\n" + "=" * 60)
    print("RESUMEN DEL REGISTRO")
    print("=" * 60)

    print(f"Total de vuelos registrados: {total_vuelos}")

    print("\nVuelos por aerolínea:")
    for nombre, cantidad in vuelos_por_aerolinea.items():
        print(f"  {nombre:<20} {cantidad}")

    print("\nVuelos por ciudad de destino:")
    for ciudad, cantidad in vuelos_por_destino.items():
        print(f"  {ciudad:<20} {cantidad}")

    print(f"\nTotal de pasajeros: {total_pasajeros}")
    print(f"Promedio de pasajeros por vuelo: {promedio_pasajeros:.2f}")

    print(f"\nSuma total de tarifas: ${total_tarifas:,.2f}")
    print(f"Tarifa promedio: ${promedio_tarifa:,.2f}")

    print(f"\nVuelo más caro: {vuelo_mas_caro['numero_vuelo']} "
          f"(${vuelo_mas_caro['tarifa']:,.2f})")
    print(f"Vuelo más barato: {vuelo_mas_barato['numero_vuelo']} "
          f"(${vuelo_mas_barato['tarifa']:,.2f})")
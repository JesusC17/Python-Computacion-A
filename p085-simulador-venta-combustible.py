# ================================================================
# SISTEMA DE GESTIÓN - ESTACIÓN DE SERVICIO
# Fase 1: Descomposición y Diseño de Algoritmo -> Menú Principal
# ================================================================
# Reglas respetadas:
#   - Ciclo infinito con while True
#   - break SOLO para salir del programa
#   - continue para regresar al menú tras cada módulo
#   - if / elif / else para validar la opción
#   - f-strings para toda salida en consola
#   - Sin funciones, sin listas, sin estructuras avanzadas
# ================================================================

while True:
    print()
    print("=" * 48)
    print(f"{'ESTACIÓN DE SERVICIO - MENÚ PRINCIPAL':^48}")
    print("=" * 48)
    print(f"  {'1.':<3}Venta de Combustible")
    print(f"  {'2.':<3}Simulación de Rendimiento")
    print(f"  {'3.':<3}Clasificador de Cliente")
    print(f"  {'4.':<3}Salir")
    print("=" * 48)

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print()
        print("-" * 48)
        print(f"{'MÓDULO: VENTA DE COMBUSTIBLE':^48}")
        print("-" * 48)

        # ------------------------------------------------------
        # 1. Tipo de combustible (str) -> validado con while
        # ------------------------------------------------------
        while True:
            print("Tipos de combustible disponibles:")
            print(f"  {'1.':<3}Diesel")
            print(f"  {'2.':<3}Premium")
            print(f"  {'3.':<3}Magna")
            tipo_seleccion = input("Seleccione el tipo (1-3): ")

            if tipo_seleccion == "1":
                tipo_combustible = "Diesel"
                break
            elif tipo_seleccion == "2":
                tipo_combustible = "Premium"
                break
            elif tipo_seleccion == "3":
                tipo_combustible = "Magna"
                break
            else:
                print(f"\n*** Opción de combustible inválida. Intente de nuevo. ***\n")
                continue

        # ------------------------------------------------------
        # 2. Precio por litro (float) -> debe ser positivo
        # ------------------------------------------------------
        while True:
            entrada_precio = input("\nIngrese el precio por litro ($): ")
            try:
                precio_litro = float(entrada_precio)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido (ej. 24.50). ***")
                continue

            if precio_litro > 0:
                break
            else:
                print("*** El precio debe ser un valor positivo. Intente de nuevo. ***")
                continue

        # ------------------------------------------------------
        # 3. Cantidad de litros (float) -> debe ser positiva
        # ------------------------------------------------------
        while True:
            entrada_litros = input("Ingrese la cantidad de litros: ")
            try:
                cantidad_litros = float(entrada_litros)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido (ej. 10.5). ***")
                continue

            if cantidad_litros > 0:
                break
            else:
                print("*** La cantidad de litros debe ser positiva. Intente de nuevo. ***")
                continue

        # ------------------------------------------------------
        # 4. Cálculo y ticket de venta formateado
        # ------------------------------------------------------
        total_venta = precio_litro * cantidad_litros

        print()
        print("=" * 48)
        print(f"{'TICKET DE VENTA':^48}")
        print("=" * 48)
        print(f"{'Tipo de combustible:':<28}{tipo_combustible:>20}")
        print(f"{'Precio por litro ($):':<28}{precio_litro:>20.2f}")
        print(f"{'Litros cargados (L):':<28}{cantidad_litros:>20.2f}")
        print("-" * 48)
        print(f"{'TOTAL A PAGAR ($):':<28}{total_venta:>20.2f}")
        print("=" * 48)

        continue

    elif opcion == "2":
        print()
        print("-" * 48)
        print(f"{'MÓDULO: SIMULACIÓN DE RENDIMIENTO':^48}")
        print("-" * 48)

        # ------------------------------------------------------
        # 1. Kilometraje inicial (float) -> puede ser 0 (auto nuevo)
        # ------------------------------------------------------
        while True:
            entrada_km = input("Ingrese el kilometraje inicial (km): ")
            try:
                kilometraje_inicial = float(entrada_km)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido. ***")
                continue

            if kilometraje_inicial >= 0:
                break
            else:
                print("*** El kilometraje no puede ser negativo. ***")
                continue

        # ------------------------------------------------------
        # 2. Factor de rendimiento constante (float, km por litro)
        # ------------------------------------------------------
        while True:
            entrada_rendimiento = input("Ingrese el rendimiento del vehículo (km por litro): ")
            try:
                rendimiento = float(entrada_rendimiento)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido. ***")
                continue

            if rendimiento > 0:
                break
            else:
                print("*** El rendimiento debe ser mayor a cero. ***")
                continue

        # ------------------------------------------------------
        # 3. Kilómetros estimados a recorrer por mes (float)
        # ------------------------------------------------------
        while True:
            entrada_km_mensual = input("Ingrese los km estimados a recorrer por mes: ")
            try:
                km_mensual = float(entrada_km_mensual)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido. ***")
                continue

            if km_mensual > 0:
                break
            else:
                print("*** Los km mensuales deben ser mayores a cero. ***")
                continue

        # ------------------------------------------------------
        # 4. Capacidad del tanque en litros (float) -> para // y %
        # ------------------------------------------------------
        while True:
            entrada_tanque = input("Ingrese la capacidad del tanque (litros): ")
            try:
                capacidad_tanque = float(entrada_tanque)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido. ***")
                continue

            if capacidad_tanque > 0:
                break
            else:
                print("*** La capacidad del tanque debe ser mayor a cero. ***")
                continue

        # ------------------------------------------------------
        # 5. Número de meses a proyectar (int) -> controla el range()
        # ------------------------------------------------------
        while True:
            entrada_meses = input("Ingrese el número de meses a proyectar: ")
            try:
                meses_proyeccion = int(entrada_meses)
            except ValueError:
                print("*** Debe ingresar un número entero válido. ***")
                continue

            if meses_proyeccion > 0:
                break
            else:
                print("*** El número de meses debe ser mayor a cero. ***")
                continue

        # ------------------------------------------------------
        # 6. Tabla proyectada mes a mes (ciclo for + range())
        # ------------------------------------------------------
        litros_acumulados = 0.0

        print()
        print("-" * 76)
        print(f"{'PROYECCIÓN DE RENDIMIENTO - ' + str(meses_proyeccion) + ' MESES':^76}")
        print("-" * 76)
        print(f"{'Mes':>5} | {'Km Proyectado':>13} | {'Litros Mes':>11} | "
              f"{'Litros Acum.':>13} | {'Tanques':>9} | {'Desgaste':>9}")
        print("-" * 76)

        for mes in range(1, meses_proyeccion + 1):
            km_proyectado = kilometraje_inicial + (km_mensual * mes)
            litros_mes = km_mensual / rendimiento
            litros_acumulados = litros_acumulados + litros_mes

            tanques_llenos = int(litros_acumulados // capacidad_tanque)  # división entera
            indice_desgaste = mes ** 2                                   # potencia

            print(f"{mes:>5} | {km_proyectado:>13.2f} | {litros_mes:>11.2f} | "
                  f"{litros_acumulados:>13.2f} | {tanques_llenos:>9} | {indice_desgaste:>9}")

        litros_sobrantes = litros_acumulados % capacidad_tanque  # residuo

        print("-" * 76)
        print(f"{'RESUMEN FINAL DE LA PROYECCIÓN':^76}")
        print("-" * 76)
        print(f"{'Litros totales consumidos:':<45}{litros_acumulados:>25.2f} L")
        print(f"{'Tanques llenos requeridos (total):':<45}{tanques_llenos:>25}")
        print(f"{'Litros sobrantes (residuo del tanque):':<45}{litros_sobrantes:>25.2f} L")
        print(f"{'Kilometraje final proyectado:':<45}{km_proyectado:>25.2f} km")
        print("-" * 76)

        continue

    elif opcion == "3":
        print()
        print("-" * 48)
        print(f"{'MÓDULO: CLASIFICADOR DE CLIENTE':^48}")
        print("-" * 48)

        # ------------------------------------------------------
        # Volumen de compra mensual (float) -> debe ser positivo
        # ------------------------------------------------------
        while True:
            entrada_volumen = input("Ingrese el volumen de compra mensual (litros): ")
            try:
                volumen_compra = float(entrada_volumen)
            except ValueError:
                print("*** Debe ingresar un valor numérico válido. ***")
                continue

            if volumen_compra > 0:
                break
            else:
                print("*** El volumen de compra debe ser mayor a cero. ***")
                continue

        # ------------------------------------------------------
        # Clasificación con if / elif / else + operador lógico "and"
        #   Regular  -> < 100 L
        #   Premium  -> 100 L a 500 L (rango: se necesita "and")
        #   Flotilla -> > 500 L
        # ------------------------------------------------------
        if volumen_compra < 100:
            categoria_cliente = "Regular"
            beneficio = "Sin descuentos especiales"

        elif volumen_compra >= 100 and volumen_compra <= 500:
            categoria_cliente = "Premium"
            beneficio = "5% de descuento y acumulación de puntos"

        else:
            categoria_cliente = "Flotilla"
            beneficio = "10% de descuento y facturación consolidada"

        # ------------------------------------------------------
        # Salida formateada
        # ------------------------------------------------------
        print()
        print("=" * 48)
        print(f"{'RESULTADO DE CLASIFICACIÓN':^48}")
        print("=" * 48)
        print(f"{'Volumen de compra (L/mes):':<28}{volumen_compra:>20.2f}")
        print(f"{'Categoría asignada:':<28}{categoria_cliente:>20}")
        print("-" * 48)
        print(f"Beneficio: {beneficio}")
        print("=" * 48)

        continue

    elif opcion == "4":
        print()
        print(f"{'Gracias por usar el sistema. ¡Hasta pronto!':^48}")
        break

    else:
        print()
        print(f"{'*** Opción inválida. ***':^48}")
        print(f"{'Por favor, ingrese un valor válido (1-4).':^48}")
        continue

print("Programa finalizado correctamente.")
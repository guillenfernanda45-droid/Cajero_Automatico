print("---- BIENVENIDO(A) AL CAJERO AUTOMATICO ----")

pin_secreto = 1234
saldo_inicial = 100000
nombre = "Fersha"
intentos = 0
es_usuario_valido = False

# Validación del PIN
while intentos < 3 and not es_usuario_valido:
    entrada = int(input(f"Intento {intentos + 1}/3 - Ingrese su PIN: "))
    if entrada == pin_secreto:
        print(f"\nBienvenido(a) {nombre}!")
        es_usuario_valido = True
    else:
        print("PIN Incorrecto")
        intentos += 1

# Menú principal
if es_usuario_valido:
    opcion = ""
    saldo = saldo_inicial

    while opcion != "4":
        print("\n" + "=" * 15)
        print(f"SALDO ACTUAL: ₡{saldo}")
        print("=" * 15)
        print("1. Consultar saldo")
        print("2. Retirar efectivo")
        print("3. Depositar fondos")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print(f">> Su saldo disponible es: ₡{saldo}")

        elif opcion == "2":
            print("Billetes disponibles: ₡20000, ₡10000, ₡5000, ₡2000, ₡1000")
            retiro = int(input("Ingrese el monto a retirar: "))

            if retiro <= 0:
                print("Error: El monto debe ser mayor a 0.")
            elif retiro > saldo:
                print("Error: Fondos insuficientes.")
            elif retiro % 1000 != 0:
                print("Error: Solo se permiten montos múltiplos de ₡1000.")
            else:
                pendiente = retiro
                b20 = pendiente // 20000; pendiente %= 20000
                b10 = pendiente // 10000; pendiente %= 10000
                b5 = pendiente // 5000; pendiente %= 5000
                b2 = pendiente // 2000; pendiente %= 2000
                b1 = pendiente // 1000; pendiente %= 1000

                saldo -= retiro
                print("\n--- RETIRO EXITOSO ---")
                if b20 > 0: print(f"{b20} billetes de ₡20000")
                if b10 > 0: print(f"{b10} billetes de ₡10000")
                if b5 > 0: print(f"{b5} billetes de ₡5000")
                if b2 > 0: print(f"{b2} billetes de ₡2000")
                if b1 > 0: print(f"{b1} billetes de ₡1000")

                imprimir = input("¿Desea imprimir el voucher de retiro? (s/n): ")
                if imprimir.lower() == "s":
                    print("\n--- VOUCHER DE RETIRO ---")
                    print(f"Monto retirado: ₡{retiro}")
                    print(f"Saldo restante: ₡{saldo}")
                else:
                    print("No se imprimió el voucher.")

        elif opcion == "3":
            deposito = int(input("Ingrese el monto a depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"Depósito realizado. Nuevo saldo: ₡{saldo}")

                imprimir = input("¿Desea imprimir el voucher de depósito? (s/n): ")
                if imprimir.lower() == "s":
                    print("\n--- VOUCHER DE DEPÓSITO ---")
                    print(f"Monto depositado: ₡{deposito}")
                    print(f"Saldo actual: ₡{saldo}")
                else:
                    print("No se imprimió el voucher.")
            else:
                print("Error: El monto debe ser mayor a 0.")

        elif opcion == "4":
            print("¡Gracias por utilizar nuestro cajero!")

        else:
            print("Opción inválida. Intente de nuevo.")

else:
    print("\nACCESO DENEGADO")
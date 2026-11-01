def mostrar_menu():
    print("\n--- FinTech Guard: Sistema de Detección de Fraudes ---")
    print("\n=== Consultas MongoDB (Expedientes y Riesgo) ===")
    print("1. Consultar expediente completo de un cliente")
    print("2. Ver clientes con nivel de riesgo elevado y alertas")
    print("3. Consultar tarjetas asociadas a un cliente")
    print("4. Buscar comercios con reportes sospechosos por ciudad")
    print("5. Ver cuentas bancarias con restricciones de seguridad")
    print("6. (Agregación) Total de transacciones sospechosas por tipo de operación")
    print("7. (Agregación) Monto promedio de transacciones por nivel de riesgo")
    print("8. Ver detalle completo de una alerta de fraude")

    print("\n=== Consultas Cassandra (Historiales y Series de Tiempo) ===")
    print("9. Ver últimas 50 transacciones de una tarjeta")
    print("10. Buscar transacciones de tarjeta en una ventana de tiempo específica")
    print("11. Consultar transferencias SPEI enviadas por cuenta en un mes")
    print("12. Consultar transferencias SPEI recibidas por cuenta en un rango de fechas")
    print("13. Ver retiros en cajero de los últimos 7 días")
    print("14. Consultar últimos 30 inicios de sesión de un cliente")
    print("15. Buscar alertas de fraude generadas en un día por severidad")
    print("16. Ver transacciones en un comercio específico por día")

    print("\n=== Consultas Dgraph (Redes y Patrones de Relación) ===")
    print("17. Identificar clientes y cuentas asociados a un mismo dispositivo")
    print("18. Buscar rutas de transferencias en cadena (Mulas financieras)")
    print("19. Encontrar clientes conectados por información de contacto compartida")
    print("20. Identificar comercios que concentran tarjetas reportadas fraudulentas")
    print("21. Explorar red de beneficiarios frecuentes de cuenta sospechosa")
    print("22. Identificar clientes operando desde la misma IP en ciudades incongruentes")
    print("23. Recomendar cuentas de alto riesgo por cercanía en la red")
    print("24. Ver conglomerado de cuentas asociadas a un mismo RFC/Identificación")
    print("\n0. Salir")


def main():

    while True:
        mostrar_menu()
        choice = input("Seleccione opción: ")
        if choice == "1":
            print("Hola")
        elif choice == "2":
            print("Hola")
        elif choice == "3":
            print("Hola")
        elif choice == "4":
            print("Hola")
        elif choice == "5":
            print("Hola")
        elif choice == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")
            break

if __name__ == "__main__":
    main()
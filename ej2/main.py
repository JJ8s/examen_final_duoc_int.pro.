from funciones import*
tienda=Tienda()
while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Listar productos por categoría")
        print("2. Totalizar ventas por categoría")
        print("3. Totalizar ventas por año")
        print("4. Listar productos por rango de precio")
        print("5. Cambiar precio de producto")
        print("6. Salir")
            
        op = input("\nSeleccione una opción: ").strip()
        match op:
            case "1":
                tienda.listar_categoria()
            case "2":
                tienda.total_ventas_cat()
            case "3":
                tienda.totalizar_ventas_anio()
            case "4":
                tienda.listar_productos_por_rango_precio()
            case "5":
                tienda.cambiar_precio_producto()
            case "6":
                print("\n¡Gracias por usar el sistema!")
                break
            case _:
                print("\nOpción inválida. Intente nuevamente.")
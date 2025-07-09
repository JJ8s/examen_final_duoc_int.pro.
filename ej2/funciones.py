class Tienda:
    def __init__(self):
            self.productos ={
            "001":['apio','verdura',500],
            "002":['platano','fruta',1500],
            "003":['repollo','verdura',800],
            "004":['pera','fruta',600],
                }

            self.ventas ={"001":[50,'01-03-2024'],
            "002":[10,'12-03-2025'],
            "003":[ 5,'14-05-2024'],
            "004":[20,'17-10-2025'],
            "005":[14,'12-12-2024'],
                    }
            
            
    def listar_categoria(self):
        print(" Listar productos por categoria")
        categoria=input("Ingrese categoria: ").strip().lower()
        encontrados=False
        
        print(f"\nProductos en categoria '{categoria.title()}':")
        for id_producto, datos in self.productos.items():
            if datos[1].lower()==categoria:
                print(f"ID: {id_producto} | {datos[0].title()} - ${datos[2]}  ")
                encontrados=True        
        if not encontrados:
            print("No se encontraron productos en esta categoria")
        
    def total_ventas_cat(self):
        print('='*4," Totalizar ventas por categoria ",'='*4)        
        categoria_ventas={}
        
        for id_producto, datos_venta in self.ventas.items():
            cantidad = datos_venta[0]   
            
            
            if id_producto in self.productos:
                producto=self.productos[id_producto]
                categoria=producto[1]
                precio=producto[2]
                total_venta=precio*cantidad
                
                if categoria not in categoria_ventas:
                    categoria_ventas[categoria]=0
                categoria_ventas[categoria]+=total_venta
        if not categoria_ventas:
            print("no hay ventas registradas")
            return
            
        print("\ntotal de ventas por categoria: ")
        
        for categoria, total in categoria_ventas.items():     
            print(f"{categoria.title()}: ${total}")
            
    def totalizar_ventas_anio(self):
        print("\n--- TOTALIZAR VENTAS POR AÑO ---")
        anio = input("Ingrese año (ej: 2024): ").strip()
        total = 0
        
        for id_productos, datos_venta in self.ventas.items():
            cantidad=datos_venta[0]
            fecha = datos_venta[1]
            
            if fecha.split("-")[2] == anio:
                if id_productos in self.productos:
                    precio=self.productos[id_productos][2]
                    total+=precio*cantidad
                        
        print(f"\nTotal de ventas en {anio}: ${total}")
    
    def listar_productos_por_rango_precio(self):
        print("\n--- Listar productos por rango de precio ---")
        print("precio minimo 500 y maximo que hay 1500")
        try:
            min_precio=float(input("Precio minimo: "))    
            max_precio=float(input("Precio maximo: "))
            
            if min_precio<0 or max_precio<0:
                print("Error: los precios no pueden ser negativos")
                return            
            if min_precio>max_precio:
                print("Error: el precio minimo no pueden ser mayor al maximo")
                return
            
            encontrados=False
            print(f"\nProductos entre ${min_precio} y $ {max_precio}: ")
            for id_producto, datos in self.productos.items():
                nombre=datos[0]
                precio=datos[2]
                if min_precio<=precio<=max_precio:
                    print(f"ID: {id_producto} | {nombre.title()} - ${precio}")
                    encontrados=True
            if not encontrados:
                print("No se encontraron productos en este rango")
                
        except ValueError:
            print("Error: Ingrese valores numericos validos")  
              
    def cambiar_precio_producto(self):
        print("\n---Cambiar precio de producto---")
        id_producto=input("Id del producto: ").strip()
        if id_producto not in self.productos:
            print("Error: producto no encontrado")
            return
        try:
            nuevo_precio=float(input("Nuevo precio: "))
            if nuevo_precio<0:
                print("Error: el precio no pueden ser negativo")
                return
            producto=self.productos[id_producto]
            producto[2]=nuevo_precio
            print(f"\nPrecio actualizado! {producto[0].title()} ahora cuesta ${nuevo_precio}")
        
        except ValueError:
            print("Error: ingrese un valor numerico valido")
            

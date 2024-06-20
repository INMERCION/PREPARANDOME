import json
import datetime

pizzas={
    "peperoni":{"pequeña":5000,"mediana":8000,"familiar":10000},
    "mediterranea":{"pequeña":6000,"mediana":9000,"familiar":12000},
    "vegetariana":{"pequeña":5500,"mediana":8500,"familiar":11000},
}

ventas=[]
def menu_inicio():
    print(".::::Pizzas DuocUC::::.")
    print("1.Registrar una venta")
    print("2.Mostrar todas las ventas.")
    print("3.Buscar ventas por cliente.")
    print("4.Guardar las ventas en un archivo.")
    print("5.Cargar las ventas desde un archivo.")
    print("6.Generar Boleta")
    print("7.Salir del programa.")

def registrar_ventas():
        cliente=input("Ingrese nombre del cliente: ")
        pizza=input("Que tipo de pizza desea \npeperoni\nmediteranea\nvegatariana\n: ")
        tamaño=input("Que tamaño desea \npequeña\nmediana\nfamiliar\n: ")
        cantidad=int(input("cuantas pizzas desea: "))

        if pizza in pizzas and tamaño in pizzas[pizza]:
              precio =pizzas[pizza][tamaño]*cantidad
        else:
              print("Tipo de Pizza o tamaño no valido")  
              return
         
        tipo=input("Ingrese el tipo de usuario \nestudiante diurno\nestudiante vespertino\nadministrativo\n: ")
        descuento=0.0

        if tipo=="estudiante diurno":
              descuento=0.15
        elif tipo=="estudiante vespertino":
              descuento=0.20
        elif tipo=="administrativo":
              descuento=0.10
        else:
              print("Tipo de usuario no valido")
              return
        descuento_total=precio*descuento
        precio_final=precio-descuento_total

        venta= {
              "cliente":cliente,
              "tipo de pizza":pizza,
              "tamaño de la pizza":tamaño,
              "cantidad":cantidad,
              "total a pagar":precio_final,
              "fecha y hora":datetime.datetime.now().strftime("%y-%m-%d %h:%m")
        }                           
        
        ventas.append(venta)
        print("venta registrada Exitosamente")

def mostrar_ventas():
    if ventas:
        for idx, venta in enumerate(ventas, start=1):
            print(f"\venta {idx}: ")
            print(f"Cliente: {venta['cliente']}")
            print(f"Tipo de pizza: {venta['tipo de pizza']}")
            print(f"Tamaño: {venta['tamaño de la pizza']}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio final: ${venta['total a pagar']:.2f}")
            print(f"Fecha y hora: {venta['fecha y hora']}")
    else:
         print("No hay ventas  resgistradas")
def buscar_clientes():
    cliente_buscar = input("Ingrese el nombre del cliente a buscar: ")
    encontradas = []

    for venta in ventas:
        if venta['cliente'].lower() == cliente_buscar.lower():
            encontradas.append(venta)

    if encontradas:
        print(f"\nVentas encontradas para el cliente '{cliente_buscar}':")
        for idx, venta in enumerate(encontradas, start=1):
            print(f"\nVenta {idx}:")
            print(f"Tipo de pizza: {venta['tipo de pizza']}")
            print(f"Tamaño: {venta['tamaño de la pizza']}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio final: ${venta['total a pagar']:.2f}")
            print(f"Fecha y hora: {venta['fecha y hora']}")
    else:
        print(f"No se encontraron ventas para el cliente '{cliente_buscar}'.")
def guardar_datos():
    ruta_archivo='C:\\Users\\OMAR FM\\Desktop\\COMPLETOS\\clientes.json'

    with open(ruta_archivo, 'w') as file:
        json.dump(ventas, file, indent=4)
    print(f"Ventas guardadas en '{ruta_archivo}'.")

def cargar_datos():
    ruta_archivo='C:\\Users\\OMAR FM\\Desktop\\COMPLETOS\\clientes.json'
    try:
        with open(ruta_archivo, 'r') as file:
            global ventas
            ventas = json.load(file)
        print(f"ventas cargadas desde '{ruta_archivo}'.")
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")    

def generar_boleta():
    if ventas:
        idx_venta = int(input("Ingrese el número de venta para generar boleta: ")) - 1
        if 0 <= idx_venta < len(ventas):
            venta = ventas[idx_venta]
            print("\n------------ Boleta de Venta ------------")
            print(f"Fecha y hora: {venta['fecha y hora']}")
            print(f"Cliente: {venta['cliente']}")
            print("-------------------------------------------")
            print(f"Tipo de pizza:     {venta['tipo de pizza']}")
            print(f"Tamaño       :     {venta['tamaño de la pizza']}")
            print(f"Cantidad     :     {venta['cantidad']}")
            print(f"Precio final :    ${venta['total a pagar']:.2f}")
            print("-------------------------------------------")
        else:
            print("Número de venta no válido.")
    else:
        print("No hay ventas registradas.")
        
     
while True:
    menu_inicio()
    opcion = input("\tOPC: ")

    if opcion == '1':
        registrar_ventas()

    elif opcion == '2':
        mostrar_ventas()

    elif opcion == '3':
        buscar_clientes()  

    elif opcion == '4':
        guardar_datos()

    elif opcion == '5':
        cargar_datos()

    elif opcion == '6':
        generar_boleta()

    elif opcion == '7':
        print("Saliendo del Programa.....") 
        break          
    else:
         print("Seleccione una opcion valida")
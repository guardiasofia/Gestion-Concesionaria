import tkinter as tk
from cargar_guardar_datos import cargar_datos, guardar_datos
from tkinter import messagebox

# Cargar datos desde archivos JSON
vehiculos = cargar_datos('vehiculos.json')
clientes = cargar_datos('clientes.json')
transacciones = cargar_datos('transacciones.json')

# Función para agregar un vehículo
def agregar_vehiculo_gui():
    # Crear una nueva ventana
    ventana = tk.Tk()
    ventana.title("Agregar Vehículo") 

    # Crear etiquetas y entradas para los campos del vehículo
    tk.Label(ventana, text="Patente").grid(row=0)
    tk.Label(ventana, text="Marca").grid(row=1)
    tk.Label(ventana, text="Modelo").grid(row=2)
    tk.Label(ventana, text="Tipo").grid(row=3)
    tk.Label(ventana, text="Año").grid(row=4)
    tk.Label(ventana, text="Kilometraje").grid(row=5)
    tk.Label(ventana, text="Precio Compra").grid(row=6)
    tk.Label(ventana, text="Precio Venta").grid(row=7)
    tk.Label(ventana, text="Estado").grid(row=8)

    patente = tk.Entry(ventana)
    marca = tk.Entry(ventana)
    modelo = tk.Entry(ventana)
    tipo = tk.Entry(ventana)
    año = tk.Entry(ventana)
    kilometraje = tk.Entry(ventana)
    precio_compra = tk.Entry(ventana)
    precio_venta = tk.Entry(ventana)
    estado = tk.Entry(ventana)

    # Ubicar las entradas en la ventana
    patente.grid(row=0, column=1)
    marca.grid(row=1, column=1)
    modelo.grid(row=2, column=1)
    tipo.grid(row=3, column=1)
    año.grid(row=4, column=1)
    kilometraje.grid(row=5, column=1)
    precio_compra.grid(row=6, column=1)
    precio_venta.grid(row=7, column=1)
    estado.grid(row=8, column=1)

    def guardar():
        # Crear un diccionario con los datos del vehículo
        vehiculo = {
            "id_vehiculo": len(vehiculos) + 1,
            "patente": patente.get(),
            "marca": marca.get(),
            "modelo": modelo.get(),
            "tipo": tipo.get(),
            "año": int(año.get()),
            "kilometraje": int(kilometraje.get()),
            "precio_compra": float(precio_compra.get()),
            "precio_venta": float(precio_venta.get()),
            "estado": estado.get()
        }
        # Agregar el vehículo a la lista y guardar los datos
        vehiculos.append(vehiculo)
        guardar_datos('vehiculos.json', vehiculos)
        messagebox.showinfo("Información", "Vehículo guardado exitosamente")
        ventana.destroy()

    # Crear botón para guardar el vehículo
    tk.Button(ventana, text="Guardar", command=guardar).grid(row=9, column=1)
    ventana.mainloop()

# Función para agregar un cliente
def agregar_cliente_gui():
    ventana = tk.Tk()
    ventana.title("Agregar Cliente")

    tk.Label(ventana, text="Nombre").grid(row=0)
    tk.Label(ventana, text="Apellido").grid(row=1)
    tk.Label(ventana, text="Documento").grid(row=2)
    tk.Label(ventana, text="Dirección").grid(row=3)
    tk.Label(ventana, text="Teléfono").grid(row=4)
    tk.Label(ventana, text="Correo Electrónico").grid(row=5)

    nombre = tk.Entry(ventana)
    apellido = tk.Entry(ventana)
    documento = tk.Entry(ventana)
    direccion = tk.Entry(ventana)
    telefono = tk.Entry(ventana)
    correo_electronico = tk.Entry(ventana)

    nombre.grid(row=0, column=1)
    apellido.grid(row=1, column=1)
    documento.grid(row=2, column=1)
    direccion.grid(row=3, column=1)
    telefono.grid(row=4, column=1)
    correo_electronico.grid(row=5, column=1)

    def guardar():
        cliente = {
            "id_cliente": len(clientes) + 1,
            "nombre": nombre.get(),
            "apellido": apellido.get(),
            "documento": documento.get(),
            "direccion": direccion.get(),
            "telefono": telefono.get(),
            "correo_electronico": correo_electronico.get()
        }
        clientes.append(cliente)
        guardar_datos('clientes.json', clientes)
        messagebox.showinfo("Información", "Cliente guardado exitosamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, column=1)
    ventana.mainloop()

# Función para agregar una transacción
def agregar_transaccion_gui():
    ventana = tk.Tk()
    ventana.title("Registrar Transacción")

    tk.Label(ventana, text="ID Vehículo").grid(row=0)
    tk.Label(ventana, text="ID Cliente").grid(row=1)
    tk.Label(ventana, text="Tipo de Transacción").grid(row=2)
    tk.Label(ventana, text="Fecha").grid(row=3)
    tk.Label(ventana, text="Monto").grid(row=4)
    tk.Label(ventana, text="Observaciones").grid(row=5)

    id_vehiculo = tk.Entry(ventana)
    id_cliente = tk.Entry(ventana)
    tipo_transaccion = tk.Entry(ventana)
    fecha = tk.Entry(ventana)
    monto = tk.Entry(ventana)
    observaciones = tk.Entry(ventana)

    id_vehiculo.grid(row=0, column=1)
    id_cliente.grid(row=1, column=1)
    tipo_transaccion.grid(row=2, column=1)
    fecha.grid(row=3, column=1)
    monto.grid(row=4, column=1)
    observaciones.grid(row=5, column=1)

    def guardar():
        transaccion = {
            "id_transaccion": len(transacciones) + 1,
            "id_vehiculo": int(id_vehiculo.get()),
            "id_cliente": int(id_cliente.get()),
            "tipo_transaccion": tipo_transaccion.get(),
            "fecha": fecha.get(),
            "monto": float(monto.get()),
            "observaciones": observaciones.get()
        }
        transacciones.append(transaccion)
        guardar_datos('transacciones.json', transacciones)
        messagebox.showinfo("Información", "Transacción registrada exitosamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, column=1)
    ventana.mainloop()

def modificar_vehiculo_gui():
    ventana = tk.Tk()
    ventana.title("Modificar Vehículo")

    frame = tk.Frame(ventana, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    titulo = tk.Label(frame, text="Seleccione el vehículo a modificar", font=("Arial", 14))
    titulo.pack(pady=5)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=80, height=20)
    lista.pack(pady=10)

    scrollbar.config(command=lista.yview)

    for vehiculo in vehiculos:
        lista.insert(tk.END, f"ID: {vehiculo['id_vehiculo']}, Patente: {vehiculo['patente']}, Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Precio Venta: {vehiculo['precio_venta']}")

    def modificar():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            vehiculo = vehiculos[index]
            
            ventana_modificar = tk.Tk()
            ventana_modificar.title("Modificar Vehículo")

            campos = ["Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio Compra", "Precio Venta", "Estado"]
            entradas = {}
            for i, campo in enumerate(campos):
                tk.Label(ventana_modificar, text=campo).grid(row=i, column=0)
                entradas[campo] = tk.Entry(ventana_modificar)
                entradas[campo].grid(row=i, column=1)
                entradas[campo].insert(0, vehiculo[campo.lower().replace(" ", "_")])

            def guardar():
                vehiculo_modificado = {
                    "id_vehiculo": vehiculo["id_vehiculo"],
                    "patente": entradas["Patente"].get(),
                    "marca": entradas["Marca"].get(),
                    "modelo": entradas["Modelo"].get(),
                    "tipo": entradas["Tipo"].get(),
                    "año": int(entradas["Año"].get()),
                    "kilometraje": int(entradas["Kilometraje"].get()),
                    "precio_compra": float(entradas["Precio Compra"].get()),
                    "precio_venta": float(entradas["Precio Venta"].get()),
                    "estado": entradas["Estado"].get()
                }
                vehiculos[index] = vehiculo_modificado
                guardar_datos('vehiculos.json', vehiculos)
                messagebox.showinfo("Información", "Vehículo modificado exitosamente")
                ventana_modificar.destroy()
                ventana.destroy()

            tk.Button(ventana_modificar, text="Guardar", command=guardar).grid(row=len(campos), column=1)
            ventana_modificar.mainloop()
        else:
            messagebox.showwarning("Modificar", "Por favor, seleccione un vehículo para modificar.")

    boton_modificar = tk.Button(frame, text="Modificar", command=modificar)
    boton_modificar.pack(pady=10)

    ventana.mainloop()


def eliminar_vehiculo_gui():
    ventana = tk.Tk()
    ventana.title("Eliminar Vehículo")

    frame = tk.Frame(ventana, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    titulo = tk.Label(frame, text="Seleccione el vehículo a eliminar", font=("Arial", 14))
    titulo.pack(pady=5)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=80, height=20)
    lista.pack(pady=10)

    scrollbar.config(command=lista.yview)

    for vehiculo in vehiculos:
        lista.insert(tk.END, f"ID: {vehiculo['id_vehiculo']}, Patente: {vehiculo['patente']}, Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Precio Venta: {vehiculo['precio_venta']}")

    def eliminar():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            del vehiculos[index]
            lista.delete(index)
            guardar_datos('vehiculos.json', vehiculos)
            messagebox.showinfo("Eliminar", "Vehículo eliminado exitosamente.")
        else:
            messagebox.showwarning("Eliminar", "Por favor, seleccione un vehículo para eliminar.")

    boton_eliminar = tk.Button(frame, text="Eliminar", command=eliminar)
    boton_eliminar.pack(pady=10)

    ventana.mainloop()

def buscar_vehiculo(criterio, lista_resultados):
    resultados = []
    for vehiculo in vehiculos:
        if criterio.lower() in vehiculo['patente'].lower() or criterio.lower() in vehiculo['marca'].lower() or criterio.lower() in vehiculo['modelo'].lower() or criterio.lower() in str(vehiculo['precio_compra']).lower() or criterio.lower() in str(vehiculo['precio_venta']).lower():
            resultados.append(vehiculo)
    
    lista_resultados.delete(0, tk.END)  # Limpiar el Listbox antes de mostrar nuevos resultados
    
    if resultados:
        for vehiculo in resultados:
            info_vehiculo = f"ID: {vehiculo['id_vehiculo']}, Patente: {vehiculo['patente']}, Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Precio Compra: {vehiculo['precio_compra']}, Precio Venta: {vehiculo['precio_venta']}"
            lista_resultados.insert(tk.END, info_vehiculo)
    else:
        messagebox.showinfo("Información", "No se encontraron resultados.")

def buscar_vehiculos_gui():
    ventana_busqueda = tk.Toplevel()
    ventana_busqueda.title("Buscar Vehículos")

    frame_busqueda = tk.Frame(ventana_busqueda, padx=10, pady=10)
    frame_busqueda.pack(padx=10, pady=10)

    tk.Label(frame_busqueda, text="Ingrese patente, marca, modelo o precios:").pack()
    entrada_busqueda = tk.Entry(frame_busqueda, width=50)
    entrada_busqueda.pack()

    lista_resultados = tk.Listbox(frame_busqueda, width=100, height=15)
    lista_resultados.pack(pady=10)

    scrollbar = tk.Scrollbar(frame_busqueda, orient=tk.VERTICAL)
    scrollbar.config(command=lista_resultados.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista_resultados.config(yscrollcommand=scrollbar.set)

    def realizar_busqueda():
        criterio = entrada_busqueda.get().strip()
        if not criterio:
            messagebox.showwarning("Advertencia", "Por favor ingrese un criterio de búsqueda.")
            return

        buscar_vehiculo(criterio, lista_resultados)

    tk.Button(frame_busqueda, text="Buscar", command=realizar_busqueda).pack(pady=10)

def modificar_cliente_gui():
    ventana = tk.Tk()
    ventana.title("Modificar Cliente")

    frame = tk.Frame(ventana, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    titulo = tk.Label(frame, text="Seleccione el cliente a modificar", font=("Arial", 14))
    titulo.pack(pady=5)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=80, height=20)
    lista.pack(pady=10)

    scrollbar.config(command=lista.yview)

    for cliente in clientes:
        info_cliente = f"ID: {cliente['id_cliente']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}, Documento: {cliente['documento']}, Direccion: {cliente['direccion']}, Telefono: {cliente['telefono']}, Correo Electronico: {cliente['correo_electronico']}"
        lista.insert(tk.END, info_cliente)

    def modificar():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            cliente = clientes[index]
            
            ventana_modificar = tk.Tk()
            ventana_modificar.title("Modificar Cliente")

            campos = ["Nombre", "Apellido", "Documento", "Dirección", "Teléfono", "Correo Electrónico"]
            entradas = {}
            for i, campo in enumerate(campos):
                tk.Label(ventana_modificar, text=campo).grid(row=i, column=0)
                valor_campo = cliente.get(campo.lower().replace(" ", "_"), "")  # Obtener el valor del campo o cadena vacía si no existe
                entradas[campo] = tk.Entry(ventana_modificar)
                entradas[campo].grid(row=i, column=1)
                entradas[campo].insert(0, valor_campo)

            def guardar():
                cliente_modificado = {
                    "id_cliente": cliente["id_cliente"],
                    "nombre": entradas["Nombre"].get(),
                    "apellido": entradas["Apellido"].get(),
                    "documento": entradas["Documento"].get(),
                    "direccion": entradas["Dirección"].get(),
                    "telefono": entradas["Teléfono"].get(),
                    "correo_electronico": entradas["Correo Electrónico"].get()
                }
                clientes[index] = cliente_modificado
                guardar_datos('clientes.json', clientes)
                messagebox.showinfo("Información", "Cliente modificado exitosamente")
                ventana_modificar.destroy()
                ventana.destroy()

            tk.Button(ventana_modificar, text="Guardar", command=guardar).grid(row=len(campos), column=1)
            ventana_modificar.mainloop()
        else:
            messagebox.showwarning("Modificar", "Por favor, seleccione un cliente para modificar.")

    boton_modificar = tk.Button(frame, text="Modificar", command=modificar)
    boton_modificar.pack(pady=10)

    ventana.mainloop()

def eliminar_cliente_gui():
    ventana = tk.Tk()
    ventana.title("Eliminar Cliente")

    frame = tk.Frame(ventana, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    titulo = tk.Label(frame, text="Seleccione el cliente a eliminar", font=("Arial", 14))
    titulo.pack(pady=5)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=80, height=20)
    lista.pack(pady=10)

    scrollbar.config(command=lista.yview)

    for cliente in clientes:
        info_cliente = f"ID: {cliente['id_cliente']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}, Documento: {cliente['documento']}, Direccion: {cliente['direccion']}, Telefono: {cliente['telefono']}, Correo Electronico: {cliente['correo_electronico']}"
        lista.insert(tk.END, info_cliente)

    def eliminar():
        seleccion = lista.curselection()
        if seleccion:
            index = seleccion[0]
            cliente = clientes[index]
            
            confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de eliminar a {cliente['nombre']} {cliente['apellido']}?")
            if confirmacion:
                del clientes[index]
                guardar_datos('clientes.json', clientes)
                messagebox.showinfo("Información", "Cliente eliminado exitosamente")
                ventana.destroy()
        else:
            messagebox.showwarning("Eliminar", "Por favor, seleccione un cliente para eliminar.")

    boton_eliminar = tk.Button(frame, text="Eliminar", command=eliminar)
    boton_eliminar.pack(pady=10)

    ventana.mainloop()

def buscar_cliente(criterio, lista_resultados):
    # Función para buscar clientes por criterio y mostrar resultados en un Listbox
    resultados = []
    for cliente in clientes:
        if criterio.lower() in cliente['nombre'].lower() or criterio.lower() in cliente['apellido'].lower() or criterio.lower() == cliente['documento']:
            resultados.append(cliente)
    
    # Limpiar el Listbox antes de mostrar nuevos resultados
    lista_resultados.delete(0, tk.END)
    
    # Mostrar resultados encontrados
    if resultados:
        for cliente in resultados:
            info_cliente = f"ID: {cliente['id_cliente']}, Nombre: {cliente['nombre']}, Apellido: {cliente['apellido']}, Documento: {cliente['documento']}"
            lista_resultados.insert(tk.END, info_cliente)
    else:
        messagebox.showinfo("Información", "No se encontraron resultados.")

def buscar_clientes_gui():
    # Función para crear la ventana de búsqueda de clientes
    ventana_busqueda = tk.Toplevel()
    ventana_busqueda.title("Buscar Clientes")

    frame_busqueda = tk.Frame(ventana_busqueda, padx=10, pady=10)
    frame_busqueda.pack(padx=10, pady=10)

    tk.Label(frame_busqueda, text="Ingrese documento, apellido o nombres:").pack()
    entrada_busqueda = tk.Entry(frame_busqueda, width=50)
    entrada_busqueda.pack()

    lista_resultados = tk.Listbox(frame_busqueda, width=80, height=15)
    lista_resultados.pack(pady=10)

    scrollbar = tk.Scrollbar(frame_busqueda, orient=tk.VERTICAL)
    scrollbar.config(command=lista_resultados.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lista_resultados.config(yscrollcommand=scrollbar.set)

    def realizar_busqueda():
        criterio = entrada_busqueda.get().strip()
        if not criterio:
            messagebox.showwarning("Advertencia", "Por favor ingrese un criterio de búsqueda.")
            return

        buscar_cliente(criterio, lista_resultados)

    tk.Button(frame_busqueda, text="Buscar", command=realizar_busqueda).pack(pady=10)

# Función para agregar una transacción
def agregar_transaccion_gui():
    ventana = tk.Tk()
    ventana.title("Registrar Transacción")

    tk.Label(ventana, text="ID Vehículo").grid(row=0)
    tk.Label(ventana, text="ID Cliente").grid(row=1)
    tk.Label(ventana, text="Tipo de Transacción (compra/venta)").grid(row=2)
    tk.Label(ventana, text="Fecha (YYYY-MM-DD)").grid(row=3)
    tk.Label(ventana, text="Monto").grid(row=4)
    tk.Label(ventana, text="Observaciones").grid(row=5)

    id_vehiculo = tk.Entry(ventana)
    id_cliente = tk.Entry(ventana)
    tipo_transaccion = tk.Entry(ventana)
    fecha = tk.Entry(ventana)
    monto = tk.Entry(ventana)
    observaciones = tk.Entry(ventana)

    id_vehiculo.grid(row=0, column=1)
    id_cliente.grid(row=1, column=1)
    tipo_transaccion.grid(row=2, column=1)
    fecha.grid(row=3, column=1)
    monto.grid(row=4, column=1)
    observaciones.grid(row=5, column=1)

    def guardar():
        transaccion = {
            "id_transaccion": len(transacciones) + 1,
            "id_vehiculo": int(id_vehiculo.get()),
            "id_cliente": int(id_cliente.get()),
            "tipo_transaccion": tipo_transaccion.get(),
            "fecha": fecha.get(),
            "monto": float(monto.get()),
            "observaciones": observaciones.get()
        }
        transacciones.append(transaccion)
        guardar_datos('transacciones.json', transacciones)
        messagebox.showinfo("Información", "Transacción registrada exitosamente")
        ventana.destroy()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, column=1)
    ventana.mainloop()

def listar_compras_por_cliente_vehiculo_fechas(cliente_id=None, vehiculo_id=None, fecha_inicio=None, fecha_fin=None):
    total_compras = 0
    resultados = []

    for transaccion in transacciones:
        if transaccion['tipo_transaccion'] == 'Compra':
            # Aplicar filtros
            if (cliente_id is None or transaccion['id_cliente'] == cliente_id) and \
               (vehiculo_id is None or transaccion['id_vehiculo'] == vehiculo_id) and \
               (fecha_inicio is None or fecha_inicio <= transaccion['fecha'] <= fecha_fin):

                resultados.append(transaccion)
                total_compras += transaccion['monto']

    return resultados, total_compras

# Función para filtrar y calcular total de ventas por cliente, vehículo y rango de fechas
def listar_ventas_por_cliente_vehiculo_fechas(cliente_id=None, vehiculo_id=None, fecha_inicio=None, fecha_fin=None):
    total_ventas = 0
    resultados = []

    for transaccion in transacciones:
        if transaccion['tipo_transaccion'] == 'Venta':
            # Aplicar filtros
            if (cliente_id is None or transaccion['id_cliente'] == cliente_id) and \
               (vehiculo_id is None or transaccion['id_vehiculo'] == vehiculo_id) and \
               (fecha_inicio is None or fecha_inicio <= transaccion['fecha'] <= fecha_fin):

                resultados.append(transaccion)
                total_ventas += transaccion['monto']

    return resultados, total_ventas

# Ejemplo de uso en una interfaz gráfica (GUI) usando tkinter
def listar_compras_gui():
    ventana_listado = tk.Toplevel()
    ventana_listado.title("Listado de Compras")

    # Filtrar por cliente, vehículo y rango de fechas
    cliente_id = None  # Define el ID del cliente si quieres filtrar
    vehiculo_id = None  # Define el ID del vehículo si quieres filtrar
    fecha_inicio = None  # Define la fecha de inicio si quieres filtrar
    fecha_fin = None  # Define la fecha de fin si quieres filtrar

    # Obtener resultados y total de compras
    resultados, total_compras = listar_compras_por_cliente_vehiculo_fechas(cliente_id, vehiculo_id, fecha_inicio, fecha_fin)

    # Mostrar resultados en un Listbox
    listbox_resultados = tk.Listbox(ventana_listado, width=100, height=20)
    listbox_resultados.pack(padx=10, pady=10)

    for compra in resultados:
        info_compra = f"ID: {compra['id_transaccion']}, Cliente: {compra['id_cliente']}, Vehículo: {compra['id_vehiculo']}, Monto: ${compra['monto']}, Fecha: {compra['fecha']}"
        listbox_resultados.insert(tk.END, info_compra)

    # Mostrar total de compras
    tk.Label(ventana_listado, text=f"Total de Compras: ${total_compras}").pack()

    ventana_listado.mainloop()

# Ejemplo de uso en una interfaz gráfica (GUI) usando tkinter
def listar_ventas_gui():
    ventana_listado = tk.Toplevel()
    ventana_listado.title("Listado de Ventas")

    # Filtrar por cliente, vehículo y rango de fechas
    cliente_id = None  # Define el ID del cliente si quieres filtrar
    vehiculo_id = None  # Define el ID del vehículo si quieres filtrar
    fecha_inicio = None  # Define la fecha de inicio si quieres filtrar
    fecha_fin = None  # Define la fecha de fin si quieres filtrar

    # Obtener resultados y total de ventas
    resultados, total_ventas = listar_ventas_por_cliente_vehiculo_fechas(cliente_id, vehiculo_id, fecha_inicio, fecha_fin)

    # Mostrar resultados en un Listbox
    listbox_resultados = tk.Listbox(ventana_listado, width=100, height=20)
    listbox_resultados.pack(padx=10, pady=10)

    for venta in resultados:
        info_venta = f"ID: {venta['id_transaccion']}, Cliente: {venta['id_cliente']}, Vehículo: {venta['id_vehiculo']}, Monto: ${venta['monto']}, Fecha: {venta['fecha']}"
        listbox_resultados.insert(tk.END, info_venta)

    # Mostrar total de ventas
    tk.Label(ventana_listado, text=f"Total de Ventas: ${total_ventas}").pack()

    ventana_listado.mainloop()


# Ventana principal con botones para cada funcionalidad
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión de Concesionaria")

    tk.Button(ventana, text="Agregar Vehículo", command=agregar_vehiculo_gui).pack(pady=5)
    tk.Button(ventana, text="Modificar Vehículo", command=modificar_vehiculo_gui).pack(pady=5)
    tk.Button(ventana, text="Eliminar Vehículo", command=eliminar_vehiculo_gui).pack(pady=5)
    tk.Button(ventana, text="Buscar Vehículo", command=buscar_vehiculos_gui).pack(pady=5)
    tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente_gui).pack(pady=5)
    tk.Button(ventana, text="Modificar Cliente", command=modificar_cliente_gui).pack(pady=5)
    tk.Button(ventana, text="Eliminar Cliente", command=eliminar_cliente_gui).pack(pady=5)
    tk.Button(ventana, text="Buscar Cliente", command=buscar_clientes_gui).pack(pady=5)
    tk.Button(ventana, text="Registrar Transacción", command=agregar_transaccion_gui).pack(pady=5)
    tk.Button(ventana, text="Listar Compras", command=listar_compras_gui).pack(pady=5)
    tk.Button(ventana, text="Listar Ventas", command=listar_ventas_gui).pack(pady=5)


    ventana.mainloop()

ventana_principal()

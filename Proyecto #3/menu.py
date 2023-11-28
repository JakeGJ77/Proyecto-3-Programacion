#POO
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QScrollArea
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QScrollArea, QGridLayout
import sys
from PyQt5.QtWidgets import QApplication,QHeaderView, QTableWidget,QTableWidgetItem, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout,QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, Qt
import json
import os 
import requests
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QInputDialog, QMessageBox



class MenuWindow(QMainWindow):
    def __init__(self, menu_data):
        super().__init__()
        self.setWindowTitle("Menú")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        central_widget.setLayout(layout)

        menu_widget = QWidget()
        scroll_area.setWidget(menu_widget)
        layout_menu = QGridLayout(menu_widget)

        row = 0
        col = 0

        for item in menu_data["menu"]:
            nombre = item["nombre"]
            categoria = item["categoria"]
            precio = item["precio"]
            ingredientes = ", ".join(item["ingredientes"])
            calorias = item["calorias"]

            label = QLabel(f"{nombre}\n"
                          f"Categoría: {categoria}\n"
                          f"Precio: ${precio:.2f}\n"
                          f"Ingredientes: {ingredientes}\n"
                          f"Calorías: {calorias}", self)

            label.setStyleSheet("background-color: #EDEDED; border-radius: 10px; padding: 10px; margin: 5px;")

            layout_menu.addWidget(label, row, col)
            col += 1

            if col > 1:
                col = 0
                row += 1

        layout.addWidget(scroll_area)

class MiAplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")
        self.setGeometry(350, 100, 600, 400)
        self.setStyleSheet("background-color: #171B26;")
        self.botones_pagina1 = []  #
        self.menu_window = None  # Variable de instancia para mantener una referencia a la ventana del menú

        #notas_label = []
        self.initUI()
        
    def editar_producto(self):
        # Lógica para editar un producto existente en el menú
        nombre_producto, ok = QInputDialog.getText(self, "Editar Producto", "Nombre del producto a editar:")

        if ok and nombre_producto:
            # Aquí debes agregar la lógica para cargar el producto del JSON
            archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json"
            if os.path.exists(archivo_json):
                with open(archivo_json, "r") as json_file:
                    try:
                        json_data = json.load(json_file)
                    except json.JSONDecodeError:
                        json_data = {}
            else:
                json_data = {}

            menu = json_data.get("menu", [])

            # Buscar el producto por nombre
            producto_para_editar = None
            for producto in menu:
                if producto.get("nombre") == nombre_producto:
                    producto_para_editar = producto
                    break

            if producto_para_editar:
                # Obtener nuevos valores para el producto
                nuevo_nombre, ok_nombre = QInputDialog.getText(self, "Editar Producto", "Nuevo nombre:", text=producto_para_editar.get("nombre"))
                #nueva_categoria, ok_categoria = QInputDialog.getItem(self, "Editar Producto", "Nueva categoría:",
                                                                   # ["platos_fuertes", "ensaladas", "postres"],
                                                                   #0, False, text=producto_para_editar.get("categoria"))
                nuevos_ingredientes, ok_ingredientes = QInputDialog.getText(self, "Editar Producto", "Nuevos ingredientes (separados por comas):",
                                                                           text=", ".join(producto_para_editar.get("ingredientes", [])))
                nuevo_precio, ok_precio = QInputDialog.getDouble(self, "Editar Producto", "Nuevo precio:",
                                                                  value=producto_para_editar.get("precio", 0.0))
                nuevas_calorias, ok_calorias = QInputDialog.getInt(self, "Editar Producto", "Nuevas calorías:",
                                                                   value=producto_para_editar.get("calorias", 0))

                # Validar que todas las entradas fueron aceptadas
                if ok_nombre and ok_ingredientes and ok_precio and ok_calorias:
                    # Actualizar los valores del producto
                    producto_para_editar["nombre"] = nuevo_nombre
                    #producto_para_editar["categoria"] = nueva_categoria
                    producto_para_editar["ingredientes"] = [ingrediente.strip() for ingrediente in nuevos_ingredientes.split(',')]
                    producto_para_editar["precio"] = nuevo_precio
                    producto_para_editar["calorias"] = nuevas_calorias

                    # Guardar el JSON actualizado
                    with open(archivo_json, "w") as json_file:
                        json.dump(json_data, json_file, indent=4)

                    # Mostrar mensaje informativo si no hay errores
                    QMessageBox.information(self.nueva_ventana, "Información", f"Producto '{nombre_producto}' editado exitosamente")
                else:
                    # Mostrar advertencia si el usuario cancela o proporciona entradas incorrectas
                    QMessageBox.warning(self.nueva_ventana, "Advertencia", "Edición cancelada o entradas incorrectas.")
            else:
                # Mostrar advertencia si el producto no fue encontrado
                QMessageBox.warning(self.nueva_ventana, "Advertencia", f"Producto '{nombre_producto}' no encontrado en el menú.")
                
                
    def editar_json(self):
        # Implementa la lógica para editar el JSON
        print("Editar JSON")

        # Obtener el nombre del producto que se editará (puedes personalizar esto según tu implementación)
        nombre_producto = self.obtener_nombre_producto()

        # Obtener la ruta del archivo JSON
        archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json"

        # Verificar si el archivo JSON existe
        if os.path.exists(archivo_json):
            with open(archivo_json, "r") as json_file:
                try:
                    # Cargar el contenido actual del archivo JSON
                    json_data = json.load(json_file)

                    # Buscar el producto en la lista
                    for producto in json_data["menu"]:
                        if producto["nombre"] == nombre_producto:
                            # Implementar la lógica de edición (puedes mostrar un cuadro de diálogo para editar campos)
                            nuevo_nombre, ok = QInputDialog.getText(self, "Editar Producto", f"Nuevo nombre para '{nombre_producto}':", QLineEdit.Normal, producto["nombre"])
                            
                            if ok and nuevo_nombre:
                                producto["nombre"] = nuevo_nombre

                                # Guardar la lista actualizada en el archivo JSON
                                with open(archivo_json, "w") as json_file_actualizado:
                                    json.dump(json_data, json_file_actualizado, indent=2)

                                print(f"Producto '{nombre_producto}' editado exitosamente.")
                                return

                            print("Edición cancelada.")
                            return

                    print(f"Producto '{nombre_producto}' no encontrado en el JSON.")

                except json.JSONDecodeError:
                    print("Error al decodificar el JSON.")
        else:
            print("El archivo JSON no existe.")

    def crear_datos_json(self):
        # Obtener el nombre del nuevo producto
        nombre_producto, ok = QInputDialog.getText(self, "Crear Producto", "Nombre del nuevo producto:")

        if ok and nombre_producto:
            # Obtener la categoría del nuevo producto
            categorias = ["platos_fuertes", "ensaladas", "postres"]  
            categoria, ok = QInputDialog.getItem(self, "Seleccionar Categoría", "Categoría:", categorias, 0, False)



            if ok and categoria:
                ingredientes, ok = QInputDialog.getText(self, "Crear Producto", "Ingredientes (separados por comas):")
                if ok:
                    precio, ok = QInputDialog.getDouble(self, "Crear Producto", "Precio:")
                    if ok:
                        calorias, ok = QInputDialog.getInt(self, "Crear Producto", "Calorías:")
                        if ok:
                            nuevo_producto = {
                                "categoria": categoria,
                                "nombre": nombre_producto,
                                "ingredientes": [ingrediente.strip() for ingrediente in ingredientes.split(',')],
                                "calorias": calorias,
                                "precio": precio,
                            }

                            # Aquí debes agregar la lógica para agregar el nuevo producto al JSON
                            archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json"
                            if os.path.exists(archivo_json):
                                with open(archivo_json, "r") as json_file:
                                    try:
                                        json_data = json.load(json_file)
                                    except json.JSONDecodeError:
                                        json_data = {}
                            else:
                                json_data = {}

                            json_data.setdefault("menu", []).append(nuevo_producto)

                            with open(archivo_json, "w") as json_file:
                                json.dump(json_data, json_file, indent=4)

                            # Mostrar mensaje informativo si no hay errores
                            QMessageBox.information(self.nueva_ventana, "Información", "Producto creado exitosamente")
                        else:
                            QMessageBox.warning(self.nueva_ventana, "Advertencia", "Debe proporcionar un valor válido para las calorías.")
                    else:
                        QMessageBox.warning(self.nueva_ventana, "Advertencia", "Debe proporcionar un valor válido para el precio.")
                else:
                    QMessageBox.warning(self.nueva_ventana, "Advertencia", "Debe proporcionar ingredientes para el producto.")
            else:
                QMessageBox.warning(self.nueva_ventana, "Advertencia", "Debe seleccionar una categoría para el producto.")
        else:
            QMessageBox.warning(self.nueva_ventana, "Advertencia", "Debe proporcionar un nombre para el producto.")

                                    # Aquí puedes agregar la lógica para guardar el nuevo producto en el JSON
        self.guardar_nuevo_producto(nuevo_producto)

    def guardar_nuevo_producto(self, nuevo_producto):
        # Aquí debes agregar la lógica para guardar el nuevo producto en tu JSON
        print(f"Nuevo producto creado: {nuevo_producto}")
        # Puedes actualizar tu JSON aquí utilizando la información del nuevo producto
            
    def eliminar_producto(self):
            # Lógica para eliminar un producto existente del menú
            nombre_producto, ok = QInputDialog.getText(self, "Eliminar Producto", "Nombre del producto a eliminar:")

            if ok and nombre_producto:
                # Aquí debes agregar la lógica para eliminar el producto del JSON
                archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json"
                if os.path.exists(archivo_json):
                    with open(archivo_json, "r") as json_file:
                        try:
                            json_data = json.load(json_file)
                        except json.JSONDecodeError:
                            json_data = {}
                else:
                    json_data = {}

                menu = json_data.get("menu", [])

                # Buscar el producto por nombre y eliminarlo si se encuentra
                for idx, producto in enumerate(menu):
                    if producto.get("nombre") == nombre_producto:
                        del menu[idx]
                        break

                # Guardar el JSON actualizado
                with open(archivo_json, "w") as json_file:
                    json.dump(json_data, json_file, indent=4)

                # Mostrar mensaje informativo si no hay errores
                QMessageBox.information(self.nueva_ventana, "Información", f"Producto '{nombre_producto}' eliminado exitosamente")

            # Obtener la ruta del archivo JSON
            archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json"

            # Verificar si el archivo JSON existe
            if os.path.exists(archivo_json):
                with open(archivo_json, "r") as json_file:
                    try:
                        # Cargar el contenido actual del archivo JSON
                        json_data = json.load(json_file)

                        # Buscar el producto en la lista
                        for i, producto in enumerate(json_data["menu"]):
                            if producto["nombre"] == nombre_producto:
                                # Eliminar el producto de la lista
                                del json_data["menu"][i]

                                # Guardar la lista actualizada en el archivo JSON
                                with open(archivo_json, "w") as json_file_actualizado:
                                    json.dump(json_data, json_file_actualizado, indent=2)

                                print(f"Producto '{nombre_producto}' eliminado exitosamente.")
                                return

                        print(f"Producto '{nombre_producto}' no encontrado en el JSON.")

                    except json.JSONDecodeError:
                        print("Error al decodificar el JSON.")
            else:
                print("El archivo JSON no existe.")

    def obtener_nombre_producto(self):
        # Esta función debe ser personalizada según tu implementación
        # Aquí se muestra un ejemplo simple donde el usuario selecciona un producto de una lista
        items = ["Pechuga de Pollo", "Filete de Pescado", "Ensalada César", "Hamburguesa", "Pizza"]
        
        # Mostrar un cuadro de diálogo para que el usuario elija un producto
        item, ok = QInputDialog.getItem(self, "Seleccionar Producto", "Seleccione un producto:", items, 0, False)

        if ok and item:
            return item
        else:
            # Si el usuario cancela la selección, puedes devolver un valor nulo o manejarlo de otra manera
            return None
        
    def confirmar_accion(self):
            # Obtener información seleccionada
            qty = "1"  # Puedes ajustar esto según sea necesario
            producto = self.producto_combo.currentText()
            notas = self.notas_entry.text()
            reemplazo = self.reemplazar_combo.currentText()

            # Añadir fila a la tabla
            row_position = self.tabla.rowCount()
            self.tabla.insertRow(row_position)
            self.tabla.setItem(row_position, 0, QTableWidgetItem(qty))
            self.tabla.setItem(row_position, 1, QTableWidgetItem(f"{producto} ({reemplazo})"))
            self.tabla.setItem(row_position, 2, QTableWidgetItem(notas))

            # Limpiar los campos después de confirmar
            self.producto_combo.setCurrentIndex(0)
            self.notas_entry.clear()
            self.reemplazar_combo.setCurrentIndex(0)

        


#Configuración de una imagen en la interfaz gráfica:  
############################################################################
    def initUI(self):                                                      #
        label = QLabel(self)                                               #
        pixmap = QPixmap("C:/Users/Jake/Desktop/Proyecto #3/img/IMG2.PNG") # 
        label.setPixmap(pixmap)                                            #
        label.setGeometry(255, 0, 350, 400)                                #
                                                                           #
############################################################################


#Creación de widgets y elementos interactivos:
#########################################################################################################################################
                                                                                                                                        #
        self.boton = QPushButton('Ver Menú', self)
        self.boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
        self.boton.setGeometry(62, 100, 130, 25)
        self.boton.clicked.connect(self.mostrar_menu)                                                                                      #
        self.boton.pressed.connect(self.change_color_boton1)                                                                            #
        self.boton.released.connect(self.restore_color_boton1)                                                                          #
                                                                                                                                        #
        titulo_usuario = QLabel('Nombre de Usuario:', self)                                                                             #
        titulo_usuario.setStyleSheet("background: transparent;color: white; font: bold 12px; font-family: Arial")                       #
        titulo_usuario.setGeometry(62, 170, 200, 20)                                                                                    #
                                                                                                                                        #
        self.entrada_usuario = QLineEdit(self)                                                                                          #
        self.entrada_usuario.setStyleSheet("background-color: #D9D9D9; color: #000000; font: Arial")                                    #
        self.entrada_usuario.setGeometry(62, 200, 130, 25)                                                                              #
                                                                                                                                        #
        titulo_contrasena = QLabel('Contraseña:', self)                                                                                 #
        titulo_contrasena.setStyleSheet("background: transparent;color: white; font: bold 12px; font-family: Arial")                    #
        titulo_contrasena.setGeometry(62, 230, 200, 20)                                                                                 #
                                                                                                                                        #
        self.entrada_contrasena = QLineEdit(self)                                                                                       #
        self.entrada_contrasena.setEchoMode(QLineEdit.Password)                                                                         #
        self.entrada_contrasena.setStyleSheet("background-color: #D9D9D9; color: #000000; font: Arial")                                 #
        self.entrada_contrasena.setGeometry(62, 250, 130, 25)                                                                           #
                                                                                                                                        #
        self.boton2 = QPushButton('Iniciar Sesión', self)                                                                               #
        self.boton2.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")    #
        self.boton2.setGeometry(62, 300, 130, 25)                                                                                       #
        self.boton2.pressed.connect(self.change_color_boton2)                                                                           #
        self.boton2.released.connect(self.restore_color_boton2)                                                                         #
        self.boton2.clicked.connect(self.abrir_nueva_ventana)                                                                           #
                                                                                                                                        #
#########################################################################################################################################
        
#Mostrar la ventana
########################
        self.show()    #
########################
    def mostrar_menu(self):
        with open(r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json", 'r', encoding='utf-8') as json_file:
            menu_data = json.load(json_file)

        # Crear la instancia de MenuWindow y almacenarla como variable de instancia
        self.menu_window = MenuWindow(menu_data)
        self.menu_window.show()


# Funciones de cambio y restauración de color del botón
########################################################################################################################################
    def change_color_boton1(self):                                                                                                     #
        self.boton.setStyleSheet("background-color: #81c43b; border-radius: 5%; color: black; font: bold 12px; font-family: Arial")    #
                                                                                                                                       #
    def restore_color_boton1(self):                                                                                                    #
        self.boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")    #
                                                                                                                                       #
    def change_color_boton2(self):                                                                                                     #
        self.boton2.setStyleSheet("background-color: #81c43b; border-radius: 5%; color: black; font: bold 12px; font-family: Arial")   #
                                                                                                                                       # 
    def restore_color_boton2(self):                                                                                                    #
        self.boton2.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")   #
                                                                                                                                       #
########################################################################################################################################
        

#cierra la ventana de mi aplicaccion
###############################
    def cerrar_ventanas(self): #
        self.close()           #
###############################
        
    def abrir_nueva_ventana(self):    
#Obtener la información del usuario y contraseña:
#####################################################
        usuario = self.entrada_usuario.text()       #
        contrasena = self.entrada_contrasena.text() #
#####################################################


#Verifica la contrasena y usuario
###############################################
        if usuario == '' and contrasena == '':#
###############################################


#Si las credenciales son válidas esto abre una nueva ventana
##############################################################################################################
            self.nueva_ventana = QWidget()                                                                   # 
            self.nueva_ventana.setWindowIcon(QIcon("C:/Users/Jake/Desktop/Proyecto #3/monkey.ico"))          #
            self.nueva_ventana.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")       #
            self.nueva_ventana.setGeometry(0, 0, 1080, 720)                                                  #
            self.nueva_ventana.setStyleSheet("background-color: #171B26")                                    #
            self.titulo_nueva_ventana = QLabel("BIENVENIDO AL\nGESTOR DEL\nRESTAURANTE", self.nueva_ventana) #
            self.titulo_nueva_ventana.setStyleSheet("font: bold 100px; font-family: Arial; color: white")    #
            self.titulo_nueva_ventana.setGeometry(200, 20, 800, 500)                                         #
                                                                                                             # 
            rutas_imagenes = [                                                                               #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/orden.png",                                        #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/tarjeta.png",                                      #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/grafico.png",                                      #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/carrito.png",                                      #
                "C:/Users/Jake/Desktop/Proyecto #3/iconos/menu.png"                                          #
            ]                                                                                                #
##############################################################################################################



#lista que contiene referencias a diferentes métodos que se encargarán de actualizar la información mostrada en la nueva ventana.
#################################################################################################################################################################
            actualizar_funciones = [self.actualizar_pagina1, self.actualizar_pagina2, self.actualizar_pagina3, self.actualizar_pagina4, self.actualizar_pagina5]#
#################################################################################################################################################################


#Configuración de botones en la nueva ventana
##############################################################################################
            for i in range(5):                                                               #
                boton_nueva_ventana = QPushButton('', self.nueva_ventana)                    #
                boton_nueva_ventana.setGeometry(0, 144 * i, 120, 150)                        #
                                                                                             #
                icono = QPixmap(rutas_imagenes[i])                                           #
                icono_redimensionado = icono.scaled(80, 80)                                  #
                boton_nueva_ventana.setIcon(QIcon(icono_redimensionado))                     #
                boton_nueva_ventana.setIconSize(icono_redimensionado.rect().size())          #
                boton_nueva_ventana.setStyleSheet("background-color: #1C3659;")              #
                boton_nueva_ventana.clicked.connect(actualizar_funciones[i])                 #
                                                                                             #
                boton_nueva_ventana.show()                                                   #
##############################################################################################

#Mostrar y manipular las ventanas
##########################################################
            self.hide()                                  #
            self.nueva_ventana.show()                    #
            QTimer.singleShot(3000, self.cerrar_ventanas)#
        else:                                            #
            print("Credenciales incorrectas")            #
##########################################################


# Funciones donde se da las opciones del las paginas
########################################################################

    def actualizar_pagina1(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("Página 1")
            #self.titulo_nueva_ventana.setStyleSheet("font: bold 42px; font-family: Arial")
            self.titulo_nueva_ventana.hide()
            start_x = 150
            start_y = 70
            button_width = 200
            button_height = 160
            button_spacing_x = 30
            button_spacing_y = 50

            ruta_icono_comun = r"C:\Users\Jake\Desktop\Proyecto #3\iconos\mesaG.png"

            def mostrar_subpagina(numero_boton):
                #self.titulo_nueva_ventana.setText(f"Subpágina 1.{numero_boton}")
                #self.titulo_nueva_ventana.setGeometry(200, 20, 800, 500)

                # Ocultar botones de la página 1
                for boton in self.botones_pagina1:
                    boton.hide()

                # Mostrar número como texto en la subpágina 1.1
                self.texto_numero = QLabel(f'Mesa #{numero_boton}', self.nueva_ventana)
                self.texto_numero.setStyleSheet("color: white; font: bold 40px; font-family: Segoe UI")
                self.texto_numero.adjustSize()
                self.texto_numero.move(140, 10) #x,y
                self.texto_numero.show()
                

        # Añadir un QLabel y un QComboBox de salector de comida
                self.label_producto = QLabel('Producto', self.nueva_ventana)
                self.label_producto.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                self.label_producto.move(140, 100)
                self.label_producto.show()

                # Cargar productos desde un archivo JSON
                with open(r"C:\Users\Jake\Desktop\Proyecto #3\Menu\menu.json", 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)

                # Asegurarse de que la categoría "menu" exista en el JSON
                if "menu" in data:
                    # Obtener la lista de menu
                    menu = data["menu"]

                    # Extraer los nombres de la lista de diccionarios
                    productos = [plato["nombre"] for plato in menu]

                self.producto_combo = QComboBox(self.nueva_ventana)
                # Añadir los productos al combo box
                self.producto_combo.addItems(productos)
                self.producto_combo.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.producto_combo.move(140, 140)
                self.producto_combo.setFixedSize(420, 30)  # Establecer el tamaño (ancho, alto)
                self.producto_combo.show()

                # Añadir un QLabel y un QComboBox de reemplazo
                self.label_reemplazar = QLabel("Reemplazar", self.nueva_ventana)
                self.label_reemplazar.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                self.label_reemplazar.move(587, 100)
                self.label_reemplazar.show()

                # Obtener las opciones de reemplazo específicas del producto seleccionado desde el archivo JSON
                def actualizar_opciones_reemplazo():
                    producto_seleccionado = self.producto_combo.currentText()
                    opciones_reemplazo = []

                    for plato in menu:
                        if plato["nombre"] == producto_seleccionado and "opciones_reemplazo" in plato:
                            opciones_reemplazo = plato["opciones_reemplazo"]
                            break

                    # Limpiar el combo box y agregar las nuevas opciones de reemplazo
                    self.reemplazar_combo.clear()
                    self.reemplazar_combo.addItems(opciones_reemplazo)

                self.reemplazar_combo = QComboBox(self.nueva_ventana)
                self.reemplazar_combo.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.reemplazar_combo.move(587, 140)
                self.reemplazar_combo.setFixedSize(200, 30)  # Establecer el tamaño (ancho, alto)
                self.reemplazar_combo.show()

                # Conectar la señal currentIndexChanged del producto_combo a la función de actualización
                self.producto_combo.currentIndexChanged.connect(actualizar_opciones_reemplazo)

                # Seleccionar automáticamente el primer elemento de las opciones de reemplazo
                actualizar_opciones_reemplazo()
            # Añadir QLabel y QLineEdit para las notas
                self.notas_label = QLabel('Notas:', self.nueva_ventana)
                self.notas_label.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                self.notas_label.move(140, 200)
                self.notas_label.show()

                self.notas_entry = QLineEdit(self.nueva_ventana)
                self.notas_entry.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.notas_entry.setGeometry(140, 240, 650, 85)  # Establecer el tamaño (ancho, alto)
                self.notas_entry.show()
                
                # Añadir botón "Confirmar"
                self.confirmar_boton = QPushButton('Confirmar', self.nueva_ventana)
                self.confirmar_boton.setGeometry(850, 200, 170, 50)  # Establecer el tamaño (ancho, alto)
                self.confirmar_boton.setStyleSheet("background-color: #0094FF; border-radius: 12%; color: white; font: bold 12px; font-family: Arial")

                self.confirmar_boton.show()
                
                
                
                # Después de crear la tabla en la función mostrar_subpagina
                # Después de crear la tabla en la función mostrar_subpagina
                self.tabla = QTableWidget(self.nueva_ventana)
                self.tabla.setGeometry(140, 340, 890, 280)
                self.tabla.setColumnCount(3)  # Número de columnas
                self.tabla.setHorizontalHeaderLabels(["Qty", "Producto", "Notas del Producto"])
                self.tabla.verticalHeader().setVisible(False)

                # Configurar el tamaño de las columnas
                self.tabla.setColumnWidth(0, 70)  # Establecer el ancho de la columna "Qty" a 70 píxeles
                self.tabla.setColumnWidth(1, 410)  # Establecer el ancho de la columna "Producto" a 200 píxeles (ajustar según sea necesario)
                self.tabla.setColumnWidth(2, 410)  # Establecer el ancho de la columna "Notas del Producto" (ajustar según sea necesario)

                # Establecer el color de fondo de la tabla (ejemplo: verde claro)
                self.tabla.setStyleSheet("background-color: #D9D9D9")  # Puedes cambiar el color según tus preferencias



                # Añadir botón "Ordenar"
                self.ordenar_boton = QPushButton('Ordenar', self.nueva_ventana)
                self.ordenar_boton.setGeometry(850, 630, 170, 50)
                self.ordenar_boton.setStyleSheet("background-color: #0094FF; border-radius: 12%; color: white; font: bold 12px; font-family: Arial")
                self.ordenar_boton.clicked.connect(lambda _, num=numero_boton: self.generar_json(num))
                self.ordenar_boton.show()

                # Conectar el botón "Confirmar" a la función confirmar_accion
                self.confirmar_boton.clicked.connect(self.confirmar_accion)
                # Mostrar la subpágina
                self.tabla.show()
                            

            for fila in range(3):
                for columna in range(4):
                    numero_boton = fila * 4 + columna + 1
                    boton_nueva_ventana = QPushButton(f' {numero_boton}', self.nueva_ventana)
                    boton_nueva_ventana.setGeometry(start_x + columna * (button_width + button_spacing_x),
                                                start_y + fila * (button_height + button_spacing_y),
                                                button_width, button_height)
                    
                    boton_nueva_ventana.setStyleSheet("background-color: #0798F2; border-radius: 15%; color: white; font: bold 40px; font-family: Arial")
                    boton_nueva_ventana.clicked.connect(lambda _, num=numero_boton: mostrar_subpagina(num))

                    icono = QIcon(ruta_icono_comun)
                    icono_redimensionado = icono.pixmap(80, 80)

                    boton_nueva_ventana.setIcon(QIcon(icono_redimensionado))
                    boton_nueva_ventana.setIconSize(icono_redimensionado.rect().size())

                    boton_nueva_ventana.show()
                    
                    self.botones_pagina1.append(boton_nueva_ventana) 
                    
                    


    def ocultar_botones_pagina1(self):
        for boton in self.botones_pagina1:
            boton.hide()
            self.titulo_nueva_ventana.hide()
            self.notas_label.hide()
            self.notas_entry.hide()
            self.confirmar_boton.hide()
            self.reemplazar_combo.hide()
            self.producto_combo.hide()
            self.texto_numero.hide()
            self.label_producto.hide()
            self.label_reemplazar.hide()
            
            
    def generar_json(self, numero_boton):
        # Obtener datos actuales del archivo JSON si existe
        archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\pedidos_actuales.json"
        
        if os.path.exists(archivo_json):
            with open(archivo_json, "r") as json_file:
                try:
                    json_data = json.load(json_file)
                except json.JSONDecodeError:
                    json_data = {}
        else:
            json_data = {}

        # Obtener datos de la tabla
        nuevo_pedido = {"Qty": "", "Producto": "", "Notas del Producto": ""}
        for row in range(self.tabla.rowCount()):
            qty = self.tabla.item(row, 0).text()
            producto = self.tabla.item(row, 1).text()
            notas = self.tabla.item(row, 2).text()
            nuevo_pedido["Qty"] = qty
            nuevo_pedido["Producto"] = producto
            nuevo_pedido["Notas del Producto"] = notas

        # Agregar el nuevo pedido al JSON existente
        json_data["mesa" + str(numero_boton)] = json_data.get("mesas" + str(numero_boton), []) + [nuevo_pedido]

        # Guardar el JSON actualizado
        with open(archivo_json, "w") as json_file:
            json.dump(json_data, json_file)

        print(f"JSON actualizado para el pedido {numero_boton}: {json_data}")
            
            

    def actualizar_pagina2(self):
        if self.titulo_nueva_ventana:
            
                # Añadir un QLabel y un QComboBox de selector de mesa
                self.mesa_numero_label = QLabel('N Mesa', self.nueva_ventana)
                self.mesa_numero_label.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                self.mesa_numero_label.move(140, 100)
                self.mesa_numero_label.show()

                # Cargar mesas desde el archivo JSON
                mesas = self.cargar_mesas_desde_json()
                
                self.mesa_numero = QComboBox(self.nueva_ventana)
                # Añadir las mesas al combo box
                self.mesa_numero.addItems(mesas)
                self.mesa_numero.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.mesa_numero.move(140, 140)
                self.mesa_numero.setFixedSize(82 , 30)  # Establecer el tamaño (ancho, alto)
                self.mesa_numero.show()
                
            # Añadir QLabel y QLineEdit para las correo
                self.correo_label = QLabel('correo:', self.nueva_ventana)
                self.correo_label.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                self.correo_label.move(140, 200)
                self.correo_label.show()

                self.correo_entry = QLineEdit(self.nueva_ventana)
                self.correo_entry.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.correo_entry.setGeometry(140, 240, 430, 39)  # Establecer el tamaño (ancho, alto)
                self.correo_entry.show()

                # Después de crear la tablapagar en la función mostrar_subpagina
                self.tablapagar = QTableWidget(self.nueva_ventana)
                self.tablapagar.setGeometry(140, 340, 735, 280)
                self.tablapagar.setColumnCount(3)  # Número de columnas
                self.tablapagar.setHorizontalHeaderLabels(["Qty", "Producto", "Precio"])
                self.tablapagar.verticalHeader().setVisible(False)

                # Configurar el tamaño de las columnas
                self.tablapagar.setColumnWidth(0, 75)  # Establecer el ancho de la columna "Qty" a 70 píxeles
                self.tablapagar.setColumnWidth(1, 430)  # Establecer el ancho de la columna "Producto" a 200 píxeles (ajustar según sea necesario)
                self.tablapagar.setColumnWidth(2, 230)  # Establecer el ancho de la columna "Notas del Producto" (ajustar según sea necesario)

                # Establecer el color de fondo de la tablapagar (ejemplo: verde claro)
                self.tablapagar.setStyleSheet("background-color: #D9D9D9")  # Puedes cambiar el color según tus preferencias



                # Añadir fila de ejemplo
                self.tablapagar.insertRow(0)
                self.tablapagar.setItem(0, 0, QTableWidgetItem("1"))
                self.tablapagar.setItem(0, 1, QTableWidgetItem("Comida 1"))
                self.tablapagar.setItem(0, 2, QTableWidgetItem("Notas de Comida 1"))
                
                                # Mostrar la subpágina
                self.tablapagar.show()
        
                self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2
                self.titulo_nueva_ventana.hide()
                
    def cargar_mesas_desde_json(self):
        archivo_json = r"C:\Users\Jake\Desktop\Proyecto #3\pedidos_actuales.json"

        if os.path.exists(archivo_json):
            with open(archivo_json, "r") as json_file:
                try:
                    json_data = json.load(json_file)
                    mesas = []
                    for key in json_data.keys():
                        if key.startswith("mesas"):
                            mesas.append(key.replace("mesas", ""))
                    return mesas
                except json.JSONDecodeError:
                    print("Error al decodificar el JSON.")
        return []



    def actualizar_pagina3(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("lo mismo de la tercera")
           
            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2
            self.titulo_nueva_ventana.hide()     


    def actualizar_pagina4(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("y la cuerta de negecia")
            api_key = '94cbe4e64a6a023b627a8fa5af5b064f'  # Reemplaza con tu clave de OpenWeatherMap
            ciudad = 'Madrid'  # Reemplaza con el nombre de tu ciudad
            url_clima = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=imperial'

            try:
                response = requests.get(url_clima)
                response.raise_for_status()
                data = response.json()

                if 'main' in data and 'weather' in data:
                    temperatura = round(data['main']['temp'], 2)
                    descripcion = data['weather'][0]['description']
                    icono_nombre = data['weather'][0]['icon']

                    # Obtener la hora actual
                    hora_actual = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)

                    # Construir la URL completa para la imagen del clima
                    base_url_icono = 'http://openweathermap.org/img/wn/'
                    icono_url = f'{base_url_icono}{icono_nombre}@2x.png'

                    # Mostrar la información en la interfaz gráfica
                    etiqueta_clima = QLabel(f'Temperatura actual en {ciudad}: {temperatura}°F, {descripcion}', self.nueva_ventana)
                    etiqueta_clima.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                    etiqueta_clima.setGeometry(140, 100, 500, 50)
                    etiqueta_clima.show()

                    etiqueta_hora = QLabel(f'Hora actual: {hora_actual}', self.nueva_ventana)
                    etiqueta_hora.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                    etiqueta_hora.setGeometry(140, 150, 500, 50)
                    etiqueta_hora.show()

                    # Descargar la imagen y mostrarla en la interfaz gráfica
                    pixmap = QPixmap()
                    pixmap.loadFromData(requests.get(icono_url).content)
                    etiqueta_icono = QLabel(self.nueva_ventana)
                    etiqueta_icono.setPixmap(pixmap)
                    etiqueta_icono.setGeometry(140, 200, 100, 100)
                    etiqueta_icono.show()

                else:
                    print('Error al procesar los datos de la API: No se encontraron datos de clima actuales.')

            except requests.exceptions.RequestException as e:
                print(f"Error al realizar la solicitud a la API: {e}")

            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2 
            self.titulo_nueva_ventana.hide()  
        
    def actualizar_pagina5(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("La ultima porfiiiiin")
            # Agregar botones para acciones de productos en la página 5
            # Agregar botones para acciones de productos en la página 5
        # Agregar botones para acciones de productos en la página 5
            self.boton_crear_producto = QPushButton('Crear Producto', self.nueva_ventana)
            self.boton_editar_producto = QPushButton('Editar Producto', self.nueva_ventana)
            self.boton_eliminar_producto = QPushButton('Eliminar Producto', self.nueva_ventana)
            self.boton_editar_json = QPushButton('Editar JSON', self.nueva_ventana)
            self.boton_crear_datos_json = QPushButton('Crear Datos JSON', self.nueva_ventana)

            # Conectar los botones a funciones correspondientes
            self.boton_crear_producto.clicked.connect(self.crear_datos_json)
            self.boton_editar_producto.clicked.connect(self.editar_producto)
            self.boton_eliminar_producto.clicked.connect(self.eliminar_producto)
            #self.boton_editar_json.clicked.connect(self.editar_json)
            self.boton_crear_datos_json.clicked.connect(self.crear_datos_json)

            # Posiciona los botones en la interfaz
            self.boton_crear_producto.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
            self.boton_crear_producto.setGeometry(150, 40, 150, 30)
            self.boton_editar_producto.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
            self.boton_editar_producto.setGeometry(150, 80, 150, 30)
            self.boton_eliminar_producto.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
            self.boton_eliminar_producto.setGeometry(150, 130, 150, 30)
            self.boton_editar_json.setGeometry(100, 180, 150, 30)
            self.boton_editar_json.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")
            #self.boton_crear_datos_json.setGeometry(20, 180, 150, 30)

            # Asegúrate de mostrar los botones
            self.boton_crear_producto.show()
            self.boton_editar_producto.show()
            self.boton_eliminar_producto.show()
            #self.boton_editar_json.show()
           # self.boton_crear_datos_json.show()

            # Ocultar otros elementos si es necesario
            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2
            self.titulo_nueva_ventana.hide()
            
            

#Lo ejecuta
#########################################
if __name__ == '__main__':              #
    app = QApplication(sys.argv)        #
    ventana_principal = MiAplicacion()  #
    sys.exit(app.exec_())               #
#########################################

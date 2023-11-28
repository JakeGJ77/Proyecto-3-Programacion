#POO

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout,QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, Qt


class MiAplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Monkey's Garden Oasis: Sabores Saludables de la Selva")
        self.setGeometry(350, 100, 600, 400)
        self.setStyleSheet("background-color: #171B26;")
        self.botones_pagina1 = []  #

        self.initUI()
        


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
        self.boton = QPushButton('Ver Menú', self)                                                                                      #
        self.boton.setStyleSheet("background-color: #0094FF; border-radius: 5%; color: white; font: bold 12px; font-family: Arial")     #
        self.boton.setGeometry(62, 100, 130, 25)                                                                                        #
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
                texto_numero = QLabel(f'Mesa #{numero_boton}', self.nueva_ventana)
                texto_numero.setStyleSheet("color: white; font: bold 40px; font-family: Segoe UI")
                texto_numero.adjustSize()
                texto_numero.move(140, 10) #x,y
                texto_numero.show()
                
                # Añadir un QLabel y un QComboBox de salector de comida
                label_producto = QLabel('Producto', self.nueva_ventana)
                label_producto.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                label_producto.move(140, 100)
                label_producto.show()

                self.producto_combo = QComboBox(self.nueva_ventana)
                self.producto_combo.addItems(["Comida 1", "Comida 2", "Comida 3", "Comida 4"])
                self.producto_combo.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.producto_combo.move(140, 140)
                self.producto_combo.setFixedSize(420 , 30)  # Establecer el tamaño (ancho, alto)
                self.producto_combo.show()
                
                #anadir Un Qlabel y un Q comboBox de remmplazo
                
                label_reemplazar = QLabel("Reemplazar", self.nueva_ventana)
                label_reemplazar.setStyleSheet("color: white; font: bold 20px; font-family: Arial")
                label_reemplazar.move(587, 100)
                label_reemplazar.show()
                
                
                self.reemplazar_combo = QComboBox(self.nueva_ventana)
                self.reemplazar_combo.addItems(["Comida 1", "Comida 2", "Comida 3", "Comida 4"])
                self.reemplazar_combo.setStyleSheet("background-color: #A5A5A5; color: black;")
                self.reemplazar_combo.move(587, 140)
                self.reemplazar_combo.setFixedSize(200 , 30)  # Establecer el tamaño (ancho, alto)
                self.reemplazar_combo.show()
                
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
                #self.confirmar_boton.clicked.connect(self.confirmar_accion)  # Conectar el clic del botón a una función
                self.confirmar_boton.show()
                

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

    def actualizar_pagina2(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("La del segundo")
        
            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2
            self.titulo_nueva_ventana.hide()



    def actualizar_pagina3(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("lo mismo de la tercera")

            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2
            self.titulo_nueva_ventana.hide()     


    def actualizar_pagina4(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("y la cuerta de negecia")

            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2 
            self.titulo_nueva_ventana.hide()  
        
    def actualizar_pagina5(self):
        if self.titulo_nueva_ventana:
            #self.titulo_nueva_ventana.setText("La ultima porfiiiiin")
            
            self.ocultar_botones_pagina1()  # Ocultar los botones al cambiar a la página 2
            self.titulo_nueva_ventana.hide()

#Lo ejecuta
#########################################
if __name__ == '__main__':              #
    app = QApplication(sys.argv)        #
    ventana_principal = MiAplicacion()  #
    sys.exit(app.exec_())               #
#########################################

# @autor: Magno Efren
# https://www.youtube.com/c/MagnoEfren
import sys
from GUI import *
from conexionBD import*
from PyQt5.QtWidgets import QTableWidgetItem

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form() 
		self.ui.setupUi(self)

		self.datosTotal = Registro_datos()
		self.ui.bt_refrescar.clicked.connect(self.m_productos)
		self.ui.bt_agregar.clicked.connect(self.insert_productos)
		self.ui.bt_buscar.clicked.connect(self.buscar_producto)
		self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
		self.ui.bt_actualizar.clicked.connect(self.modificar_productos)
		
		self.ui.tabla_productos.setColumnWidth(0,98)
		self.ui.tabla_productos.setColumnWidth(1,100)
		self.ui.tabla_productos.setColumnWidth(2,98)
		self.ui.tabla_productos.setColumnWidth(3,98)
		self.ui.tabla_productos.setColumnWidth(4,98)
		self.ui.tabla_borrar.setColumnWidth(0,98)
		self.ui.tabla_borrar.setColumnWidth(1,100)
		self.ui.tabla_borrar.setColumnWidth(2,98)
		self.ui.tabla_borrar.setColumnWidth(3,98)
		self.ui.tabla_borrar.setColumnWidth(4,98)
		self.ui.tabla_buscar.setColumnWidth(0,98)
		self.ui.tabla_buscar.setColumnWidth(1,100)
		self.ui.tabla_buscar.setColumnWidth(2,98)
		self.ui.tabla_buscar.setColumnWidth(3,98)
		self.ui.tabla_buscar.setColumnWidth(4,98)

	def m_productos(self):	
		datos = self.datosTotal.buscar_productos()
		i = len(datos)

		self.ui.tabla_productos.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_productos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_productos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_productos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_productos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_productos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			tablerow +=1
	def insert_productos(self):
		codigo = self.ui.codigoA.text() 
		nombre = self.ui.nombreA.text()
		modelo = self.ui.modeloA.text()
		precio = self.ui.precioA.text()
		cantidad = self.ui.cantidadA.text()

		self.datosTotal.inserta_producto(codigo, nombre, modelo, precio, cantidad)
		self.ui.codigoA.clear()
		self.ui.nombreA.clear()
		self.ui.modeloA.clear()
		self.ui.precioA.clear()
		self.ui.cantidadA.clear()

	def modificar_productos(self):
		id_producto = self.ui.id_producto.text() 
		id_producto = str("'" + id_producto + "'")
		nombreXX = self.datosTotal.busca_producto(id_producto)

		if nombreXX != None:
			self.ui.id_buscar.setText("ACTUALIZAR")
			codigoM = self.ui.codigo_actualizar.text() 
			nombreM = self.ui.nombre_actualizar.text()
			modeloM = self.ui.modelo_actualizar.text()
			precioM = self.ui.precio_actualizar.text()
			cantidadM = self.ui.cantidad_actualizar.text()
			act = self.datosTotal.actualiza_productos(codigoM,nombreM , modeloM, precioM, cantidadM)
			if act == 1:
				self.ui.id_buscar.setText("ACTUALIZADO")				
				self.ui.codigo_actualizar.clear()
				self.ui.nombre_actualizar.clear()
				self.ui.modelo_actualizar.clear()
				self.ui.precio_actualizar.clear()
				self.ui.cantidad_actualizar.clear()
				self.ui.id_producto.clear()
			elif act == 0:
				self.ui.id_buscar.setText("ERROR")
			else:
				self.ui.id_buscar.setText("INCORRECTO")		
		else:
			self.ui.id_buscar.setText("NO EXISTE")

	def buscar_producto(self):
		nombre_producto = self.ui.codigoB.text()
		nombre_producto = str("'" + nombre_producto + "'")

		datosB = self.datosTotal.busca_producto(nombre_producto)
		i = len(datosB)

		self.ui.tabla_buscar.setRowCount(i)
		tablerow = 0
		for row in datosB:
			self.ui.tabla_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			tablerow +=1

	def eliminar_producto(self):
		eliminar = self.ui.codigo_borrar.text()
		eliminar = str("'"+ eliminar + "'")
		resp = (self.datosTotal.elimina_productos(eliminar))
		datos = self.datosTotal.buscar_productos()
		i = len(datos)
		self.ui.tabla_borrar.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			tablerow +=1
		if resp == None:
			self.ui.borrar_ok.setText("NO EXISTE")
		elif resp == 0:
			self.ui.borrar_ok.setText("NO EXISTE")
		else:
			self.ui.borrar_ok.setText("SE ELIMINO")

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	

import sys
import shutil
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile

class Saludo(object):
	"""docstring for Saludo"""
	def __init__(self):
		super(Saludo, self).__init__()
		self.ui = QUiLoader().load(QFile("UI.ui"))
		self.ui.pb_py.clicked.connect(self.new_py)
		self.ui.pb_web.clicked.connect(self.new_web)
		self.ui.pb_cur.clicked.connect(self.new_curso)

	def new_py(self):
		name = self.ui.name_input.text()

		if name == "":
			self.emer = QUiLoader().load(QFile("error_name.ui"))
			print("Necesita poner el nombre del proyecto")
			pass
		else:
			ruta = "py/"
			ruta_destino = f"C:/Users/omar/Documents/proyectos/python/{name}_py"
			try:
				shutil.copytree(ruta, ruta_destino)
				print("creada carpeta con exito")
				pass
			except:
				print("ocurrio un error al crear la carpeta")
				pass
			pass
		pass

	def new_web(self):
		name = self.ui.name_input.text()

		if name == "":
			print("Necesita poner el nombre del proyecto")
			pass
		else:
			ruta = "web/"
			ruta_destino = f"C:/Users/omar/Documents/proyectos/html/{name}_web"
			try:
				shutil.copytree(ruta, ruta_destino)
				print("creada carpeta con exito")
				pass
			except:
				print("ocurrio un error al crear la carpeta")
				pass

			pass
		pass

	def new_curso(self):
		name = self.ui.name_input.text()

		if name == "":
			print("Necesita poner el nombre del curso")
			pass
		else:
			ruta = "curso/"
			ruta_destino = f"C:/Users/omar/Documents/proyectos/cursos/{name}"
			try:
				shutil.copytree(ruta, ruta_destino)
				print("creada carpeta con exito")
				pass
			except:
				print("ocurrio un error al crear la carpeta")
				pass

			pass
		pass

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myapp = Saludo()
	myapp.ui.show()
	sys.exit(app.exec_())
		
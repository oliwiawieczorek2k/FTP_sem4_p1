import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QCheckBox
from PyQt5 import uic

import Geo_Conversion as geo_conv

class Window(QMainWindow):
	"""Main Window."""
	def __init__(self, parent=None):
		"""Initializer."""
		super().__init__(parent)
		self.setWindowTitle('Geo_Adjustment')
		self.setCentralWidget(QLabel("I'm the Central Widget"))
		self._createMenu()
		self._createToolBar()
		self._createStatusBar()

	def _createMenu(self):
		self.menu = self.menuBar().addMenu("&Menu")
		self.menu.addAction('&Exit', self.close)

		self.menu_conversion = self.menuBar().addMenu("&Data conversion")
		self.menu_conversion.addAction('&Spherical2XYZ', self.test_window)
		self.menu_conversion.addAction('&Spherical2XYZ') #, self.close)

		self.menu_geo_pre = self.menuBar().addMenu("&Geo_pre_procesing")
		self.menu_geo_pre.addAction('&Observation averaging') #, self.close)

	def _createToolBar(self):
		tools = QToolBar()
		self.addToolBar(tools)
		tools.addAction('Exit', self.close)

	def _createStatusBar(self):
		status = QStatusBar()
		status.showMessage("I'm the Status Bar")
		self.setStatusBar(status)


	def test_window(self):
		def Change_the_Checkbox_Function(self):
			if self.w.checkBox_Batch.isChecked() == True: 
				if self.w.checkBox_Sep.isChecked() == True:
					pass
				else:
					self.w.checkBox_Sep.setChecked(True)
			else:
				self.w.checkBox_Sep.setChecked(False)
		def help_fnc(self):
			print('Help me!!!!!!!')
		def clickBox(self, state):
			if state == QtCore.Qt.Checked:
				print('Checked')
			else:
				print('Unchecked')
		self.w = uic.loadUi("spherical2xyz.ui") #, self.w)
		#self.w.checkBox_Batch.toggle()
		self.w.checkBox_Batch.toggled.connect(self.w.checkBox_Sep.setDisabled)
#		print(check)
#		self.w.checkBox_Batch.stateChanged.connect(self.w.clickBox)
			#print('Batch is checked')
			#self.w.checkBox_Sep.setEnable(False)
		self.w.pushButton.clicked.connect(help_fnc)
		self.w.pushButton_Ok.clicked.connect(help_fnc)
		self.w.pushButton_Cancel.clicked.connect(self.w.close)
		self.w.show()
		#app.exec()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	#win = uic.loadUi("plik.ui")
	win.show()



	sys.exit(app.exec_())
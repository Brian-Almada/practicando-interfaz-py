from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap


class MyApp(QMainWindow):
	def __init__(self):
		super(MyApp, self).__init__()
		loadUi('interfazfull.ui', self)

		self.open_image.clicked.connect(self.load_image)
		self.save_image.clicked.connect(self.save_image_final)
		self.reset_edit.clicked.connect(self.reset_image)

		self.slider_one.valueChanged['int'].connect(self.tonality)
		self.slider_two.valueChanged['int'].connect(self.saturation)
		self.slider_three.valueChanged['int'].connect(self.brightness)
		self.slider_four.valueChanged['int'].connect(self.gray_scale)
		self.filename = str()
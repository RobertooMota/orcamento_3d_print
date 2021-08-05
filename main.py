from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import sys
from time import sleep

version = '1.0.0'
# Importa janela feita no QtDesigner
from ui_main import Ui_MainWindow
from ui_funcoes import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)
		self.show()
		self.setWindowTitle(f"M3D Orçamento - v{version}")

		# Botões menu lateral
		self.interface.btn_Orcamento.clicked.connect(lambda: self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_Orcamento))
		self.interface.btn_ValorCliente.clicked.connect(lambda: self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_ValorCliente))
		self.interface.btn_ValorCompleto.clicked.connect(lambda: self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_ValorCompleto))

		# Sair
		self.interface.btn_Sair.clicked.connect(lambda: UIFuncoes.sair(self))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	sys.exit(app.exec())

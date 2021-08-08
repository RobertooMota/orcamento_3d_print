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

		# 							BOTÕES MENU LATERAL
		######################################################################################
		self.interface.btn_Orcamento.clicked.connect(lambda: UIFuncoes.Orcamento(self))
		self.interface.btn_Modelos3D.clicked.connect(lambda: UIFuncoes.Modelos3D(self))
		self.interface.btn_Configuracoes.clicked.connect(lambda: UIFuncoes.Configuracoes(self))
		self.interface.btn_Sobre.clicked.connect(lambda: UIFuncoes.Sobre(self))

		# Sair
		self.interface.btn_Sair.clicked.connect(lambda: UIFuncoes.sair(self))

		# 							BOTÕES MENU CONFIGURACAO
		######################################################################################
		self.interface.btn_Configuracao_Cancelar.clicked.connect(lambda: UIFuncoes.ConfiguracaoCancelar(self))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	sys.exit(app.exec())

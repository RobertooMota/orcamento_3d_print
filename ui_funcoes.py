from main import *


class UIFuncoes(MainWindow):
	def sair(self):
		sys.exit()

	def Orcamento(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_Orcamento)
		UIFuncoes.SelectPage(self,'pgOrcamento')

	def ValorCliente(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_ValorCliente)
		UIFuncoes.SelectPage(self,'pgValorCliente')

	def ValorCompleto(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_ValorCompleto)
		UIFuncoes.SelectPage(self, 'pgValorCompleto')

	def SelectPage(self, pg):
		if pg == 'pgOrcamento':
			self.interface.btn_Orcamento.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
													   "border-right: 4px solid #383a59;\n"
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"
													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")
			self.interface.btn_ValorCompleto.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"
													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")
			self.interface.btn_ValorCliente.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"
													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")

		if pg == 'pgValorCliente':
			self.interface.btn_Orcamento.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
													   
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"

													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")
			self.interface.btn_ValorCompleto.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"
													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")
			self.interface.btn_ValorCliente.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
														"border-right: 4px solid #383a59;\n"
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"
													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")

		if pg == 'pgValorCompleto':
			self.interface.btn_Orcamento.setStyleSheet(u"QPushButton{\n"
													   "\n"
													   "color: white;\n"
													   "background-color: #6272a4;\n"
													   "border-top-left-radius: 10px;\n"
													   "border-bottom-left-radius: 10px;\n"
													   "}\n"
													   "\n"
													   "QPushButton:hover{\n"
													   "background-color: #ff79c6;\n"
													   "color:#282a36;\n"

													   "}\n"
													   "\n"
													   "QPushButton:Pressed{\n"
													   "background-color: rgb(255, 74, 179);\n"
													   "color:#44475a;\n"
													   "}")
			self.interface.btn_ValorCompleto.setStyleSheet(u"QPushButton{\n"
														   "\n"
														   "color: white;\n"
														   "background-color: #6272a4;\n"
														   "border-top-left-radius: 10px;\n"
														   "border-bottom-left-radius: 10px;\n"
														   "border-right: 4px solid #383a59;\n"
														   "}\n"
														   "\n"
														   "QPushButton:hover{\n"
														   "background-color: #ff79c6;\n"
														   "color:#282a36;\n"
														   "}\n"
														   "\n"
														   "QPushButton:Pressed{\n"
														   "background-color: rgb(255, 74, 179);\n"
														   "color:#44475a;\n"
														   "}")
			self.interface.btn_ValorCliente.setStyleSheet(u"QPushButton{\n"
														  "\n"
														  "color: white;\n"
														  "background-color: #6272a4;\n"
														  "border-top-left-radius: 10px;\n"
														  "border-bottom-left-radius: 10px;\n"
														  "}\n"
														  "\n"
														  "QPushButton:hover{\n"
														  "background-color: #ff79c6;\n"
														  "color:#282a36;\n"
														  "}\n"
														  "\n"
														  "QPushButton:Pressed{\n"
														  "background-color: rgb(255, 74, 179);\n"
														  "color:#44475a;\n"
														  "}")
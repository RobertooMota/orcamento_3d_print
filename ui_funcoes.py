from main import *


class UIFuncoes(MainWindow):
	def sair(self):
		sys.exit()

	# -----------------------------  Botões da tela principal ------------------------------
	def Orcamento(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_Orcamento)
		UIFuncoes.SelectPage(self, 'pgOrcamento')

	def Modelos3D(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_Modelos3D)
		UIFuncoes.SelectPage(self, 'pgModelos3D')

	def Configuracoes(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_Configuracoes)
		UIFuncoes.SelectPage(self, 'pgConfiguracoes')

	def Sobre(self):
		pass

	# -----------------------------  Botões da tela Configuracao ---------------------------
	def ConfiguracaoCancelar(self):
		self.interface.pgs_Operacao.setCurrentWidget(self.interface.pg_home)
		UIFuncoes.SelectPage(self, 'home')
		pass

	def SelectPage(self, pg):
		if pg == 'home':
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
			self.interface.btn_Modelos3D.setStyleSheet(u"QPushButton{\n"
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
			self.interface.btn_Configuracoes.setStyleSheet(u"QPushButton{\n"
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
			self.interface.btn_Modelos3D.setStyleSheet(u"QPushButton{\n"
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
			self.interface.btn_Configuracoes.setStyleSheet(u"QPushButton{\n"
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

		if pg == 'pgModelos3D':
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
			self.interface.btn_Configuracoes.setStyleSheet(u"QPushButton{\n"
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
			self.interface.btn_Modelos3D.setStyleSheet(u"QPushButton{\n"
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

		if pg == 'pgConfiguracoes':
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
			self.interface.btn_Configuracoes.setStyleSheet(u"QPushButton{\n"
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
			self.interface.btn_Modelos3D.setStyleSheet(u"QPushButton{\n"
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

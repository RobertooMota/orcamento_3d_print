from main import *
from math import pi, pow
from DBFunctions import *
import sys
from DBFunctions import DataBase


class UIFuncoes(MainWindow):
	def __init__(self):
		MainWindow.__init__(self)

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

	def AtualizarCampos(self):
		# Atualiza em tempo real a area do filamento ao editar o diametro
		try:
			if self.interface.txt_DiametroFilamento.text() != '':
				diametro = float(self.interface.txt_DiametroFilamento.text())
				area = float(pi * pow(float(diametro) / 2, 2))
				self.interface.txt_AreaFilamento.setText(str(area))
		except:
			self.interface.txt_AreaFilamento.setText('ERRO de entrada de valor!')

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


class OperationsDB(MainWindow):

	def LimparCampos(self):
		# Limpa todos os campos do cadastro
		self.interface.txt_MarcaFilamento.setText('')
		self.interface.txt_TipoFilamento.setText('')
		self.interface.txt_DiametroFilamento.setText('')
		self.interface.txt_ValorKG.setText('')
		self.interface.txt_KWh.setText('')
		self.interface.txt_PotenciaImpressora.setText('')
		self.interface.txt_Depreciacao.setText('')
		self.interface.txt_MediaFalhas.setText('')
		self.interface.txt_Modelagem.setText('')
		self.interface.txt_TempoRetorno.setText('')
		self.interface.txt_ValorImpressora.setText('')
		self.interface.txt_HorasDia.setText('')
		self.interface.txt_DiasMes.setText('')
		self.interface.txt_ValorAdicionalHora.setText('')
		self.interface.txt_Lucro.setText('')

	def CadastrarFilamento(self):
		# Informações do Filamento
		marca = self.interface.txt_MarcaFilamento.text()
		tipo = self.interface.txt_TipoFilamento.text()
		diametro = float(self.interface.txt_DiametroFilamento.text())
		densidade = float(self.interface.cb_densidade.currentText())
		area = float(pi * pow(float(diametro) / 2, 2))
		valorKG = float(self.interface.txt_ValorKG.text())

		# Valores de producao
		KWh = self.interface.txt_KWh.text()
		potenciaImpressora = self.interface.txt_PotenciaImpressora.text()
		depreciacao = self.interface.txt_Depreciacao.text()
		falhas = self.interface.txt_MediaFalhas.text()
		modelage = self.interface.txt_Modelagem.text()

		# Retorno de investimento e Lucros
		tempoRetorno = self.interface.txt_TempoRetorno.text()
		valorImpressora = self.interface.txt_ValorImpressora.text()
		horasDias = self.interface.txt_HorasDia.text()
		diasMes = self.interface.txt_DiasMes.text()
		valorAdicionalHora = self.interface.txt_ValorAdicionalHora.text()
		lucro = self.interface.txt_Lucro.text()

		# Cadastrando dados no banco de dados
		# Instanciando um objeto a classe DataBase()
		dados = DataBase()
		dados.Cadastrar('filamento', marca, tipo, diametro, densidade, float(f'{area:.2f}'), valorKG)
		dados.Cadastrar('valoresProducao', KWh, potenciaImpressora, depreciacao, falhas, modelage)
		dados.Cadastrar('retorno', tempoRetorno, valorImpressora, horasDias, diasMes, valorAdicionalHora, lucro)


def AtualizarFilamento(self):
	pass

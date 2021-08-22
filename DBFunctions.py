import sqlite3


class DataBase:
	def __init__(self):
		super(DataBase, self).__init__()

	def Cadastrar(self, tabela, *infos):
		if tabela == 'filamento':
			banco = sqlite3.connect('DataBase.db')
			BD = banco.cursor()
			informacoes = list()
			for item in infos:
				informacoes.append(item)
			BD.execute(
				"""INSERT INTO filamentos (marca, tipo, diametro, densidade, area, preco) VALUES (?,?,?,?,?,?)""",
				(informacoes[0], informacoes[1], informacoes[2], informacoes[3], informacoes[4], informacoes[5]))
			banco.commit()
			print(informacoes)
			banco.close()

		elif tabela == 'valoresProducao':
			banco = sqlite3.connect('DataBase.db')
			BD = banco.cursor()
			informacoes = list()
			for item in infos:
				informacoes.append(item)
			BD.execute(
				"""INSERT INTO valoresProducao (KWh, consumo, depreciacao, falhas, modelagem) VALUES (?,?,?,?,?)""",
				(informacoes[0], informacoes[1], informacoes[2], informacoes[3], informacoes[4]))
			banco.commit()
			print(informacoes[0], informacoes[1], informacoes[2], informacoes[3], informacoes[4])
			banco.close()

		elif tabela == 'retorno':
			banco = sqlite3.connect('DataBase.db')
			BD = banco.cursor()
			informacoes = list()
			for item in infos:
				informacoes.append(item)
			BD.execute(
				"""INSERT INTO retorno (tempo_desejado, valor_maquina, horas_dia, dias_mes, adicional_hora, lucro) VALUES (?,?,?,?,?,?)""",
				(informacoes[0], informacoes[1], informacoes[2], informacoes[3], informacoes[4], informacoes[5]))
			banco.commit()
			print(informacoes)
			banco.close()

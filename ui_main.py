# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkkEMpD.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1234, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 730))
        icon = QIcon()
        icon.addFile(u":/fundo/imgs/logoMoeda.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.VerticalTabs)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.opc_Filamento = QAction(MainWindow)
        self.opc_Filamento.setObjectName(u"opc_Filamento")
        self.opc_Caixa = QAction(MainWindow)
        self.opc_Caixa.setObjectName(u"opc_Caixa")
        self.opc_Fita = QAction(MainWindow)
        self.opc_Fita.setObjectName(u"opc_Fita")
        self.opc_PlasticoBolha = QAction(MainWindow)
        self.opc_PlasticoBolha.setObjectName(u"opc_PlasticoBolha")
        self.actionKarikos = QAction(MainWindow)
        self.actionKarikos.setObjectName(u"actionKarikos")
        self.actionValores = QAction(MainWindow)
        self.actionValores.setObjectName(u"actionValores")
        self.actionLucro = QAction(MainWindow)
        self.actionLucro.setObjectName(u"actionLucro")
        self.actionQuem_somos_n_s = QAction(MainWindow)
        self.actionQuem_somos_n_s.setObjectName(u"actionQuem_somos_n_s")
        self.actionNos_Ajude = QAction(MainWindow)
        self.actionNos_Ajude.setObjectName(u"actionNos_Ajude")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_MainFrame = QFrame(self.centralwidget)
        self.frm_MainFrame.setObjectName(u"frm_MainFrame")
        self.frm_MainFrame.setStyleSheet(u"background-color: rgb(189, 189, 189);")
        self.frm_MainFrame.setFrameShape(QFrame.NoFrame)
        self.frm_MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_MainFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_sideButtons = QFrame(self.frm_MainFrame)
        self.frm_sideButtons.setObjectName(u"frm_sideButtons")
        self.frm_sideButtons.setMinimumSize(QSize(200, 708))
        self.frm_sideButtons.setMaximumSize(QSize(200, 16777215))
        self.frm_sideButtons.setStyleSheet(u"background-color: #282a36;")
        self.frm_sideButtons.setFrameShape(QFrame.NoFrame)
        self.frm_sideButtons.setFrameShadow(QFrame.Raised)
        self.frm_sideButtons.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frm_sideButtons)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_ButtonsMain = QFrame(self.frm_sideButtons)
        self.frm_ButtonsMain.setObjectName(u"frm_ButtonsMain")
        self.frm_ButtonsMain.setFrameShape(QFrame.NoFrame)
        self.frm_ButtonsMain.setFrameShadow(QFrame.Raised)
        self.frm_ButtonsMain.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frm_ButtonsMain)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 10, 0, 0)
        self.btn_Orcamento = QPushButton(self.frm_ButtonsMain)
        self.btn_Orcamento.setObjectName(u"btn_Orcamento")
        self.btn_Orcamento.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.btn_Orcamento.setFont(font)
        self.btn_Orcamento.setStyleSheet(u"QPushButton{\n"
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
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"background-color: rgb(255, 74, 179);\n"
"color:#44475a;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_Orcamento)

        self.btn_Modelos3D = QPushButton(self.frm_ButtonsMain)
        self.btn_Modelos3D.setObjectName(u"btn_Modelos3D")
        self.btn_Modelos3D.setMinimumSize(QSize(0, 80))
        self.btn_Modelos3D.setFont(font)
        self.btn_Modelos3D.setStyleSheet(u"QPushButton{\n"
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
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"background-color: rgb(255, 74, 179);\n"
"color:#44475a;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_Modelos3D)

        self.btn_Configuracoes = QPushButton(self.frm_ButtonsMain)
        self.btn_Configuracoes.setObjectName(u"btn_Configuracoes")
        self.btn_Configuracoes.setMinimumSize(QSize(0, 80))
        self.btn_Configuracoes.setFont(font)
        self.btn_Configuracoes.setStyleSheet(u"QPushButton{\n"
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
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"background-color: rgb(255, 74, 179);\n"
"color:#44475a;\n"
"}")
        self.btn_Configuracoes.setFlat(False)

        self.verticalLayout_2.addWidget(self.btn_Configuracoes)

        self.btn_Sobre = QPushButton(self.frm_ButtonsMain)
        self.btn_Sobre.setObjectName(u"btn_Sobre")
        self.btn_Sobre.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.btn_Sobre.setFont(font1)
        self.btn_Sobre.setStyleSheet(u"QPushButton{\n"
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
"\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"background-color: rgb(255, 74, 179);\n"
"color:#44475a;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_Sobre)


        self.verticalLayout.addWidget(self.frm_ButtonsMain, 0, Qt.AlignTop)

        self.frm_Secundario = QFrame(self.frm_sideButtons)
        self.frm_Secundario.setObjectName(u"frm_Secundario")
        sizePolicy.setHeightForWidth(self.frm_Secundario.sizePolicy().hasHeightForWidth())
        self.frm_Secundario.setSizePolicy(sizePolicy)
        self.frm_Secundario.setFrameShape(QFrame.NoFrame)
        self.frm_Secundario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_Secundario)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btn_Sair = QPushButton(self.frm_Secundario)
        self.btn_Sair.setObjectName(u"btn_Sair")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_Sair.sizePolicy().hasHeightForWidth())
        self.btn_Sair.setSizePolicy(sizePolicy1)
        self.btn_Sair.setMinimumSize(QSize(0, 80))
        self.btn_Sair.setFont(font1)
        self.btn_Sair.setStyleSheet(u"QPushButton{\n"
"background-color: #6272a4;\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #EE6352;\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"background-color: #EE3312;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_Sair)


        self.verticalLayout.addWidget(self.frm_Secundario)


        self.horizontalLayout_2.addWidget(self.frm_sideButtons)

        self.frm_Telas = QFrame(self.frm_MainFrame)
        self.frm_Telas.setObjectName(u"frm_Telas")
        self.frm_Telas.setMaximumSize(QSize(11111111, 1111111))
        self.frm_Telas.setStyleSheet(u"background-color:#383a59;")
        self.frm_Telas.setFrameShape(QFrame.NoFrame)
        self.frm_Telas.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frm_Telas)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pgs_Operacao = QStackedWidget(self.frm_Telas)
        self.pgs_Operacao.setObjectName(u"pgs_Operacao")
        self.pgs_Operacao.setStyleSheet(u"")
        self.pgs_Operacao.setFrameShape(QFrame.NoFrame)
        self.pgs_Operacao.setFrameShadow(QFrame.Plain)
        self.pgs_Operacao.setLineWidth(0)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_4 = QVBoxLayout(self.pg_home)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 9, 0, 0)
        self.frame = QFrame(self.pg_home)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 600))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.lbl_LogoHome = QLabel(self.frame)
        self.lbl_LogoHome.setObjectName(u"lbl_LogoHome")
        self.lbl_LogoHome.setStyleSheet(u"background-image: url(:/fundo/imgs/3d.png);\n"
"background-position: center top;\n"
"background-repeat: no-repeat;\n"
"")

        self.verticalLayout_5.addWidget(self.lbl_LogoHome)


        self.verticalLayout_4.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.pgs_Operacao.addWidget(self.pg_home)
        self.pg_Orcamento = QWidget()
        self.pg_Orcamento.setObjectName(u"pg_Orcamento")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_Orcamento)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.pg_Orcamento)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(48)
        self.label.setFont(font2)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.pgs_Operacao.addWidget(self.pg_Orcamento)
        self.pg_Modelos3D = QWidget()
        self.pg_Modelos3D.setObjectName(u"pg_Modelos3D")
        self.verticalLayout_7 = QVBoxLayout(self.pg_Modelos3D)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.pg_Modelos3D)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.pgs_Operacao.addWidget(self.pg_Modelos3D)
        self.pg_Configuracoes = QWidget()
        self.pg_Configuracoes.setObjectName(u"pg_Configuracoes")
        self.verticalLayout_8 = QVBoxLayout(self.pg_Configuracoes)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.campo_1_Filamento = QFrame(self.pg_Configuracoes)
        self.campo_1_Filamento.setObjectName(u"campo_1_Filamento")
        self.campo_1_Filamento.setMinimumSize(QSize(0, 243))
        self.campo_1_Filamento.setMaximumSize(QSize(16777215, 16777215))
        self.campo_1_Filamento.setFrameShape(QFrame.StyledPanel)
        self.campo_1_Filamento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.campo_1_Filamento)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo = QFrame(self.campo_1_Filamento)
        self.frm_titulo.setObjectName(u"frm_titulo")
        self.frm_titulo.setMinimumSize(QSize(720, 30))
        self.frm_titulo.setMaximumSize(QSize(11111111, 30))
        self.frm_titulo.setFrameShape(QFrame.StyledPanel)
        self.frm_titulo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frm_titulo)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.titulo_Filamento = QLabel(self.frm_titulo)
        self.titulo_Filamento.setObjectName(u"titulo_Filamento")
        self.titulo_Filamento.setFont(font1)
        self.titulo_Filamento.setStyleSheet(u"\n"
"color:#ff79c6;\n"
"")

        self.verticalLayout_12.addWidget(self.titulo_Filamento, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frm_titulo)

        self.frm_3 = QFrame(self.campo_1_Filamento)
        self.frm_3.setObjectName(u"frm_3")
        self.frm_3.setFrameShape(QFrame.Box)
        self.frm_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frm_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frm_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 207))
        self.frame_5.setMaximumSize(QSize(11111111, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(-1, 9, -1, -1)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color:#bd93f9;\n"
"border: 0px solid;\n"
"border-radius:6px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color:white;\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"background-color:#bd93f9;\n"
"border: 0px solid;\n"
"border-radius:6px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color:#bd93f9;\n"
"border: 0px solid;\n"
"border-radius:6px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color:#bd93f9;\n"
"border: 0px solid;\n"
"border-radius:6px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"color:white;")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color:#bd93f9;\n"
"border: 0px solid;\n"
"border-radius:6px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:white;\n"
"")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)


        self.verticalLayout_17.addLayout(self.formLayout)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frm_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 207))
        self.frame_7.setMaximumSize(QSize(11111111, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color:#bd93f9;\n"
"border: 0px solid;\n"
"border-radius:6px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:white;\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_4)


        self.verticalLayout_18.addLayout(self.formLayout_2)


        self.verticalLayout_19.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_11.addWidget(self.frm_3)


        self.verticalLayout_8.addWidget(self.campo_1_Filamento)

        self.campo_2_ValoresProducao = QFrame(self.pg_Configuracoes)
        self.campo_2_ValoresProducao.setObjectName(u"campo_2_ValoresProducao")
        self.campo_2_ValoresProducao.setFrameShape(QFrame.StyledPanel)
        self.campo_2_ValoresProducao.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.campo_2_ValoresProducao)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo_2 = QFrame(self.campo_2_ValoresProducao)
        self.frm_titulo_2.setObjectName(u"frm_titulo_2")
        self.frm_titulo_2.setMinimumSize(QSize(720, 30))
        self.frm_titulo_2.setMaximumSize(QSize(16777215, 30))
        self.frm_titulo_2.setFrameShape(QFrame.StyledPanel)
        self.frm_titulo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frm_titulo_2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.titulo_ValoresProducao = QLabel(self.frm_titulo_2)
        self.titulo_ValoresProducao.setObjectName(u"titulo_ValoresProducao")
        self.titulo_ValoresProducao.setFont(font1)
        self.titulo_ValoresProducao.setStyleSheet(u"\n"
"color:#ff79c6;\n"
"")

        self.verticalLayout_14.addWidget(self.titulo_ValoresProducao, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frm_titulo_2)

        self.frame_4 = QFrame(self.campo_2_ValoresProducao)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.frame_4)


        self.verticalLayout_8.addWidget(self.campo_2_ValoresProducao)

        self.campo_3_RetornoLucro = QFrame(self.pg_Configuracoes)
        self.campo_3_RetornoLucro.setObjectName(u"campo_3_RetornoLucro")
        self.campo_3_RetornoLucro.setFrameShape(QFrame.StyledPanel)
        self.campo_3_RetornoLucro.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.campo_3_RetornoLucro)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo_3 = QFrame(self.campo_3_RetornoLucro)
        self.frm_titulo_3.setObjectName(u"frm_titulo_3")
        self.frm_titulo_3.setMinimumSize(QSize(0, 30))
        self.frm_titulo_3.setMaximumSize(QSize(16777215, 30))
        self.frm_titulo_3.setFrameShape(QFrame.StyledPanel)
        self.frm_titulo_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frm_titulo_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.titulo_RetornoLucro = QLabel(self.frm_titulo_3)
        self.titulo_RetornoLucro.setObjectName(u"titulo_RetornoLucro")
        self.titulo_RetornoLucro.setFont(font1)
        self.titulo_RetornoLucro.setStyleSheet(u"\n"
"color:#ff79c6;\n"
"")

        self.verticalLayout_16.addWidget(self.titulo_RetornoLucro, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.frm_titulo_3)

        self.frame_6 = QFrame(self.campo_3_RetornoLucro)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_6)


        self.verticalLayout_8.addWidget(self.campo_3_RetornoLucro)

        self.frame_9 = QFrame(self.pg_Configuracoes)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(900, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border:3px solid #50fa7b ;\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"\n"
"color:#50fa7b;\n"
"background-color:#6272a4;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:3px solid #50fa7b ;\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"\n"
"color:#6272a4;\n"
"background-color:#50fa7b;\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border:3px solid #50fa7b ;\n"
"border-radius: 15px;\n"
"\n"
"border-style:inset;\n"
"\n"
"color:#6272a4;\n"
"background-color:#50fa6b;\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border:3px solid #f1fa8c ;\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"border-radius: 15px;\n"
"background-color:#6272a4;\n"
"color:#f1fa8c;\n"
"}\n"
"QPushButton:hover{\n"
"border:3px solid #f1fa8c ;\n"
"border-radius: 15px;\n"
"border-style:outset;\n"
"background-color:#f1f98c;\n"
"color:#6272a4;\n"
"}\n"
"QPushButton:Pressed{\n"
"border:3px solid #c5d957;\n"
"border-radius: 15px;\n"
"border-style:inset;\n"
"background-color:#f1f98c;\n"
"color:#6272a4;\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setFont(font4)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border:3px solid #8be9fd;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"\n"
"background-color:#6272a4;\n"
"color:#8be9fd;\n"
"}\n"
"QPushButton:hover{\n"
"border:3px solid #8be9fd;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"\n"
"background-color:#8be9fd;;\n"
"color:#6272a4;\n"
"}\n"
"QPushButton:Pressed{\n"
"border:3px solid #8be9fd;\n"
"border-radius: 15px;\n"
"border-style: inset;\n"
"\n"
"background-color:#8be9fd;;\n"
"color:#6272a4;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.pushButton_3)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(120, 0))
        self.frame_11.setMaximumSize(QSize(90, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.btn_Configuracao_Cancelar = QPushButton(self.frame_11)
        self.btn_Configuracao_Cancelar.setObjectName(u"btn_Configuracao_Cancelar")
        sizePolicy3.setHeightForWidth(self.btn_Configuracao_Cancelar.sizePolicy().hasHeightForWidth())
        self.btn_Configuracao_Cancelar.setSizePolicy(sizePolicy3)
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setItalic(True)
        self.btn_Configuracao_Cancelar.setFont(font5)
        self.btn_Configuracao_Cancelar.setStyleSheet(u"QPushButton{\n"
"border:2px solid #ff5555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"\n"
"background-color:#6272a4;\n"
"color:#ff5555;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ff5555;\n"
"color:#6272a4;\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border-style: inset;\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_Configuracao_Cancelar)


        self.horizontalLayout_6.addWidget(self.frame_11)


        self.horizontalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_8.addWidget(self.frame_9)

        self.pgs_Operacao.addWidget(self.pg_Configuracoes)

        self.gridLayout_2.addWidget(self.pgs_Operacao, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frm_Telas)


        self.horizontalLayout.addWidget(self.frm_MainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pgs_Operacao.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.opc_Filamento.setText(QCoreApplication.translate("MainWindow", u"Insumos", None))
        self.opc_Caixa.setText(QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.opc_Fita.setText(QCoreApplication.translate("MainWindow", u"Fita", None))
        self.opc_PlasticoBolha.setText(QCoreApplication.translate("MainWindow", u"Plastico Bolha", None))
        self.actionKarikos.setText(QCoreApplication.translate("MainWindow", u"Modelos 3D", None))
        self.actionValores.setText(QCoreApplication.translate("MainWindow", u"Consumo", None))
        self.actionLucro.setText(QCoreApplication.translate("MainWindow", u"Lucro", None))
        self.actionQuem_somos_n_s.setText(QCoreApplication.translate("MainWindow", u"Desenvolvimento", None))
        self.actionNos_Ajude.setText(QCoreApplication.translate("MainWindow", u"Nos Ajude !", None))
        self.btn_Orcamento.setText(QCoreApplication.translate("MainWindow", u"Or\u00e7amento", None))
        self.btn_Modelos3D.setText(QCoreApplication.translate("MainWindow", u"Modelos 3D", None))
        self.btn_Configuracoes.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.btn_Sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.lbl_LogoHome.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pagina Or\u00e7amento", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Modelos 3D", None))
        self.titulo_Filamento.setText(QCoreApplication.translate("MainWindow", u"Filamento", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Di\u00e2metro", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Desnsidade", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1,04", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1,24", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00c1rea", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.titulo_ValoresProducao.setText(QCoreApplication.translate("MainWindow", u"Valores de produ\u00e7\u00e3o", None))
        self.titulo_RetornoLucro.setText(QCoreApplication.translate("MainWindow", u"Retorno de investimento e Lucro", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_Configuracao_Cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi


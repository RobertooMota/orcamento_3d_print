# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmXnaJA.ui'
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
        MainWindow.resize(1000, 730)
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

        self.btn_ValorCliente = QPushButton(self.frm_ButtonsMain)
        self.btn_ValorCliente.setObjectName(u"btn_ValorCliente")
        self.btn_ValorCliente.setMinimumSize(QSize(0, 80))
        self.btn_ValorCliente.setFont(font)
        self.btn_ValorCliente.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_2.addWidget(self.btn_ValorCliente)

        self.btn_ValorCompleto = QPushButton(self.frm_ButtonsMain)
        self.btn_ValorCompleto.setObjectName(u"btn_ValorCompleto")
        self.btn_ValorCompleto.setMinimumSize(QSize(0, 80))
        self.btn_ValorCompleto.setFont(font)
        self.btn_ValorCompleto.setStyleSheet(u"QPushButton{\n"
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
        self.btn_ValorCompleto.setFlat(False)

        self.verticalLayout_2.addWidget(self.btn_ValorCompleto)


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
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
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
        self.pg_ValorCliente = QWidget()
        self.pg_ValorCliente.setObjectName(u"pg_ValorCliente")
        self.verticalLayout_7 = QVBoxLayout(self.pg_ValorCliente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.pg_ValorCliente)
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

        self.pgs_Operacao.addWidget(self.pg_ValorCliente)
        self.pg_ValorCompleto = QWidget()
        self.pg_ValorCompleto.setObjectName(u"pg_ValorCompleto")
        self.verticalLayout_8 = QVBoxLayout(self.pg_ValorCompleto)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.pg_ValorCompleto)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_3)


        self.verticalLayout_8.addWidget(self.frame_4, 0, Qt.AlignHCenter)

        self.pgs_Operacao.addWidget(self.pg_ValorCompleto)

        self.gridLayout_2.addWidget(self.pgs_Operacao, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frm_Telas)


        self.horizontalLayout.addWidget(self.frm_MainFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.mn_CadastrarItens = QMenu(self.menubar)
        self.mn_CadastrarItens.setObjectName(u"mn_CadastrarItens")
        self.mn_IncluirModelos = QMenu(self.menubar)
        self.mn_IncluirModelos.setObjectName(u"mn_IncluirModelos")
        self.menuConfigurar = QMenu(self.menubar)
        self.menuConfigurar.setObjectName(u"menuConfigurar")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.mn_CadastrarItens.menuAction())
        self.menubar.addAction(self.mn_IncluirModelos.menuAction())
        self.menubar.addAction(self.menuConfigurar.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.mn_CadastrarItens.addAction(self.opc_Filamento)
        self.mn_IncluirModelos.addAction(self.actionKarikos)
        self.menuConfigurar.addAction(self.actionValores)
        self.menuConfigurar.addAction(self.actionLucro)
        self.menuSobre.addAction(self.actionQuem_somos_n_s)
        self.menuSobre.addAction(self.actionNos_Ajude)

        self.retranslateUi(MainWindow)

        self.pgs_Operacao.setCurrentIndex(0)


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
        self.btn_ValorCliente.setText(QCoreApplication.translate("MainWindow", u"Valor Cliente", None))
        self.btn_ValorCompleto.setText(QCoreApplication.translate("MainWindow", u"Valor Completo", None))
        self.btn_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.lbl_LogoHome.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pagina Or\u00e7amento", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Valor Cliente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Valor Completo", None))
        self.mn_CadastrarItens.setTitle(QCoreApplication.translate("MainWindow", u"Cadastrar Insumos", None))
        self.mn_IncluirModelos.setTitle(QCoreApplication.translate("MainWindow", u"Incluir Modelos", None))
        self.menuConfigurar.setTitle(QCoreApplication.translate("MainWindow", u"Configurar", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Sobre", None))
    # retranslateUi


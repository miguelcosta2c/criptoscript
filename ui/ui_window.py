# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'windowEBevGs.ui'
##
# Created by: Qt User Interface Compiler version 6.7.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QMenu,
                               QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
                               QSpacerItem, QToolButton, QWidget)


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(813, 600)
        self.actionCriptografar = QAction(mainWindow)
        self.actionCriptografar.setObjectName(u"actionCriptografar")
        self.actionDescriptografar = QAction(mainWindow)
        self.actionDescriptografar.setObjectName(u"actionDescriptografar")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
                                         "	background: #3a3a3a;\n"
                                         "}\n"
                                         "\n"
                                         "QLabel {\n"
                                         "	color: #fff\n"
                                         "}\n"
                                         "\n"
                                         "QPlainTextEdit {\n"
                                         "	padding: 5px;\n"
                                         "	border: 1px solid #5a5a5a;\n"
                                         "	background-color: #5a5a5a;\n"
                                         "	border-radius: 2px;\n"
                                         "	color: white\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit {\n"
                                         "	padding: 5px;\n"
                                         "	border: 1px solid black;\n"
                                         "	border-radius: 2px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton, QPushButton {\n"
                                         "	padding: 5px;\n"
                                         "	background-color: #f4f4f4;\n"
                                         "	border: 1px solid black;\n"
                                         "	border-radius: 2px;\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton:hover, QPushButton:hover {\n"
                                         "	background-color: #909090\n"
                                         "}\n"
                                         "")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(270, 400))

        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 400))
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(270, 400))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setOverwriteMode(False)
        self.plainTextEdit_2.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByKeyboard | Qt.TextInteractionFlag.TextSelectableByMouse)
        self.plainTextEdit_2.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(
            50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(671, 61))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaxLength(32)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../../../../../Downloads/key_30dp_UNDEFINED_FILL0_wght400_GRAD0_opsz24.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.toolButton)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.gridLayout.addWidget(self.frame, 2, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(
            50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 4, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 813, 22))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionCriptografar)
        self.menuArquivo.addAction(self.actionDescriptografar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate(
            "mainWindow", u"MainWindow", None))
        self.actionCriptografar.setText(
            QCoreApplication.translate("mainWindow", u"Encrypt", None))
        self.actionDescriptografar.setText(
            QCoreApplication.translate("mainWindow", u"Decrypt", None))
        self.label_2.setText(QCoreApplication.translate(
            "mainWindow", u"Decrypted Message", None))
        self.label_3.setText(QCoreApplication.translate(
            "mainWindow", u"Encrypted Message", None))
        self.label.setText(QCoreApplication.translate(
            "mainWindow", u"->", None))
        self.plainTextEdit_2.setDocumentTitle("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("mainWindow", u"Key...", None))
# if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate(
            "mainWindow", u"Generate Key", None))
# endif // QT_CONFIG(tooltip)
        self.toolButton.setText(
            QCoreApplication.translate("mainWindow", u"...", None))
# if QT_CONFIG(shortcut)
        self.toolButton.setShortcut(
            QCoreApplication.translate("mainWindow", u"Ctrl+K", None))
# endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate(
            "mainWindow", u"Encrypt", None))
        self.menuArquivo.setTitle(
            QCoreApplication.translate("mainWindow", u"File", None))
    # retranslateUi

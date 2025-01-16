from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, 
                               QMessageBox, QFileDialog)
from PySide6.QtGui import QPixmap

from ui.ui_window import Ui_mainWindow

import cript
import dialogfile

from pathlib import Path
import os
import secrets
import string
import sys

def gerar_senha():
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(32))

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return str(Path(__file__).parent / relative_path)
        
class MainWindow(Ui_mainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CriptoScript")
        self.setWindowIcon(QPixmap(resource_path("icon\\icon.ico")))
        self.pagina = 'Criptografar'
        self.config()
    
    def config(self):
        self.actionCriptografar.triggered.connect(self.ui_criptografar)
        self.actionDescriptografar.triggered.connect(self.ui_descriptografar)
        self.pushButton.clicked.connect(self.slot_button)
        self.toolButton.clicked.connect(self.slot_toolbutton)
        self.toolButton.setIcon(QPixmap(resource_path("images\\key_30dp_UNDEFINED_FILL0_wght400_GRAD0_opsz24.png")))
    
    def selecionar_caminho_arquivo(self) -> str | None:
        """
        Retorna o caminho do arquivo
        """
        file, _ = QFileDialog.getOpenFileName(
            self, 
            caption="Abrir Arquivo",
            filter="Arquivo de Texto (*)"
        )
        return file
    
    def pegar_conteudo_arquivo(self, file: str):
        with open(file, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    
    def abrir_arquivo(self):
        file = self.selecionar_caminho_arquivo()
        print(file)
        if file:
            conteudo = self.pegar_conteudo_arquivo(file)
            if conteudo:
                print(conteudo)
                self.plainTextEdit.setPlainText(conteudo)
    
    def apagar_textos(self):
        self.lineEdit.clear()
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
    
    def slot_button(self):
        if self.pagina == 'Criptografar':
            script = self.plainTextEdit.toPlainText()
            key = self.lineEdit.text()
            if not script or not key:
                self.exibir_informacao("Insira os valores de campo e chave")
                return 
            elif len(key) != 32:
                self.exibir_informação("A senha precisa ter 32 caracteres")
                return 
            try:
                criptografado = cript.criptografar(user_key=key, msg=script)
            except Exception as e:
                self.exibir_erro("Erro: "+str(e))
                return 
            dialog = dialogfile.Dialog()
            if result := dialog.exec():
                if result == QDialog.Accepted:
                    if dialog.key_dir and dialog.script_dir:
                        print(dialog.script_dir)
                        try:
                            with open(dialog.key_dir, 'w') as arquivo:
                                arquivo.write(key)
                            with open(dialog.script_dir, 'w') as arquivo:
                                arquivo.write(criptografado.hex())
                        except Exception as e:
                            self.exibir_erro("Error: "+str(e))
                            return
                    else:
                        self.exibir_erro("Selecione um arquivo válido")
                        return
                elif result == QDialog.Rejected:
                    return
                elif result == 2:
                    pass
            self.plainTextEdit_2.setPlainText(criptografado.hex())
        elif self.pagina == 'Descriptografar':
            script = bytes.fromhex(self.plainTextEdit.toPlainText())
            key = self.lineEdit.text()
            if not script or not key:
                self.exibir_informacao("Insira os valores de campo e chave")
                return 
            elif len(key) != 32:
                self.exibir_informacao("A senha precisa ter 32 caracteres")
                return 
            try:
                descriptografado = cript.descriptografar(
                    user_key=key,
                    dado_criptografado=script
                )
                self.plainTextEdit_2.setPlainText(descriptografado.decode('utf-8'))
            except ValueError as e:
                self.exibir_erro("Verifique se a chave ou o arquivo está correto\n"+"Erro: "+str(e))
                return 
            except Exception as e:
                self.exibir_erro("Erro: "+str(e))

    def slot_toolbutton(self):
        if self.pagina == 'Criptografar':
            if self.lineEdit.isReadOnly():
                self.toolButton.setStyleSheet(
                    "QToolButton {background-color: #fff;}"
                )
                self.lineEdit.clear()
                self.lineEdit.setReadOnly(False)
            else:
                self.lineEdit.setText(gerar_senha())
                self.toolButton.setStyleSheet(
                    "QToolButton {background-color: green;}"
                )
                self.lineEdit.setReadOnly(True)
        elif self.pagina == 'Descriptografar':
            if self.lineEdit.isReadOnly():
                self.toolButton.setStyleSheet(
                    "QToolButton {background-color: #fff;}"
                )
                self.lineEdit.clear()
                self.lineEdit.setReadOnly(False)
            else:
                file, _ = QFileDialog.getOpenFileName(
                    self, 
                    caption="Abrir Arquivo",
                    filter="Arquivo de Chave (*.key);;Todos os Arquivos (*)"
                )
                if not file:
                    self.exibir_erro("Verifique se a chave ou o arquivo está correto")
                    return
                with open(file, 'r') as arquivo:
                    conteudo = arquivo.read()
                self.lineEdit.setText(conteudo.replace("\n", ""))
                self.toolButton.setStyleSheet(
                    "QToolButton {background-color: green;}"
                )
                self.lineEdit.setReadOnly(True)

    def ui_criptografar(self):
        self.apagar_textos()
        self.pagina = 'Criptografar'
        self.abrir_arquivo()
        self.pushButton.setText(self.pagina)
        self.label_2.setText("Mensagem")
        self.label_3.setText("Mensagem Criptografada")
        self.toolButton.setStyleSheet(
            "QToolButton {background-color: #fff;}"
        )
    
    def ui_descriptografar(self):
        self.apagar_textos()
        self.pagina = 'Descriptografar'
        self.abrir_arquivo()
        self.pushButton.setText(self.pagina)
        self.label_2.setText("Mensagem Criptografada")
        self.label_3.setText("Mensagem")
        self.toolButton.setStyleSheet(
            "QToolButton {background-color: #fff;}"
        )

    def exibir_informacao(self, text):
        QMessageBox.information(self, "Informação", text)
    
    def exibir_erro(self, text):
        QMessageBox.critical(self, "Erro", text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

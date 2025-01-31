"""Caixa de dialogo para configuração do caminho dos arquivos"""

from PySide6.QtWidgets import QFileDialog, QDialog, QDialogButtonBox
from ui.ui_dialog import Ui_Dialog


class Dialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.config()

    def config(self):
        self.setWindowTitle("Configs")
        self.key_dir = None
        self.script_dir = None
        self.buttonBox.accepted.connect(self.salvar_tudo)
        self.buttonBox.button(
            QDialogButtonBox.Ignore).clicked.connect(self.ignorar)
        self.buttonBox.rejected.connect(self.cancelar)
        self.pushButton.clicked.connect(self.script_file)
        self.pushButton_2.clicked.connect(self.key_file)

    def selecionar_caminho_arquivo(self, filter) -> str | None:
        """
        Retorna o caminho do arquivo
        """
        file, _ = QFileDialog.getSaveFileName(
            self,
            caption="Save File",
            filter=filter
        )
        return file

    def script_file(self):
        """
        Retorna o caminho do arquivo.enc
        """
        self.label_5.setText(
            self.selecionar_caminho_arquivo(
                "Encrypted File (*.enc);;All Files (*)"
            )
        )

    def key_file(self):
        """
        Retorna o caminho do arquivo.key
        """
        self.label_2.setText(
            self.selecionar_caminho_arquivo(
                "Key File (*.key);;All Files (*)"
            )
        )

    def salvar_tudo(self):
        self.accept()
        self.key_dir = self.label_2.text()
        self.script_dir = self.label_5.text()

    def ignorar(self):
        self.done(2)

    def cancelar(self):
        self.reject()

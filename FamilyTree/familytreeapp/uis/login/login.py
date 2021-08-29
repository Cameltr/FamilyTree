from PyQt5.QtWidgets import QDialog
from familytreeapp.uis.login.loginui import Ui_login
from PyQt5.QtCore import Qt, pyqtSignal

#登录页面的封装
class Login(QDialog):
    
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)


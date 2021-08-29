from PyQt5.QtWidgets import QApplication
import sys
from familytreeapp.uis.login.login import Login
from familytreeapp.uis.home.home import Home

#定义FamilyTreeApp类进行封装
class FamilyTreeApp(QApplication):

    def __init__(self):
        super(FamilyTreeApp, self).__init__(sys.argv)
        self.login = Login()
        self.login.ui.pushButton.clicked.connect(self.Home)
        self.login.show()
    
    #实现登陆页面到主页面的跳转
    def Home(self):
        self.home = Home()
        self.home.show()
        self.login.close()
        
    
    
        
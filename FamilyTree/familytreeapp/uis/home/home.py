from PyQt5.QtWidgets import *
from familytreeapp.uis.home.homeui import Ui_home
from PyQt5.QtCore import Qt, pyqtSignal
from familytreeapp.ais.People import Person
import familytreeapp.ais.People as People
import json

class Home(QMainWindow,Ui_home):
    
    def __init__(self, parent=None):
        
        super(Home, self).__init__(parent)
        self.ui=Ui_home()
        self.ui.setupUi(self)
        # 左侧菜单按键与按钮编辑处信号与槽链接
        self.ui.pushButton_change.clicked.connect(self.page_change)
        self.ui.pushButton_count.clicked.connect(self.page_count)
        self.ui.pushButton_add.clicked.connect(self.page_add)
        self.ui.pushButton_delete.clicked.connect(self.page_delete)
        self.ui.pushButton_show.clicked.connect(self.page_show)
        self.ui.pushButton_search.clicked.connect(self.page_search)
        self.ui.pushButton_exit.clicked.connect(self.close)
        #上方菜单栏的信号与槽的绑定
        self.ui.act_change.triggered.connect(self.page_change)
        self.ui.act_delete.triggered.connect(self.page_delete)
        self.ui.act_add.triggered.connect(self.page_add)
        self.ui.act_count.triggered.connect(self.page_count)
        #page_add的信号与槽
        self.ui.pushButton_10.clicked.connect(self.add_fun)
        self.ui.pushButton_10.clicked.connect(self.clear)
        #page_delete的信号与槽
        self.ui.pushButton.clicked.connect(self.textBrowser_show)
        self.ui.pushButton_9.clicked.connect(self.delete_fun)
        #page_change的信号与槽
        self.ui.pushButton_2.clicked.connect(self.textBrowser_2_show)
        self.ui.pushButton_8.clicked.connect(self.change_fun)
        #page_search的信号与槽
        self.ui.pushButton_13.clicked.connect(self.search_fun)
        #page_count的信号与槽
        self.ui.pushButton_count.clicked.connect(self.count_fun)
        #page_show的信号与槽
        self.ui.pushButton_3.clicked.connect(self.show_fun)
        
    #实现按钮跳转到指定的分页
    def page_add(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def page_delete(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def page_change(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def page_search(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def page_show(self):
        self.ui.stackedWidget.setCurrentIndex(4)


    def page_count(self):
        self.ui.stackedWidget.setCurrentIndex(5)

#page_add的页面功能：添加结点
    def add_fun(self):
        name = self.ui.lineEdit_5.text()
        birthplace = self.ui.lineEdit_24.text()
        birthday = self.ui.lineEdit_8.text()
        deathdate = self.ui.lineEdit_9.text()
        sex = self.ui.lineEdit.text()
        height = self.ui.lineEdit_13.text()
        job = self.ui.lineEdit_14.text()
        couple_name = self.ui.lineEdit_18.text()
        father_name = self.ui.lineEdit_12.text()
        mother_name = self.ui.lineEdit_19.text()
        age = self.ui.lineEdit_2.text()

        node = Person(name, birthday, birthplace, deathdate, height, sex, job, [], father_name,mother_name,couple_name,age)
        People.add(node)

#clear清除Edit控件输入的内容
    def clear(self):
        self.ui.lineEdit_5.setText("")
        self.ui.lineEdit_24.setText("")
        self.ui.lineEdit_8.setText("")
        self.ui.lineEdit_9.setText("")
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_13.setText("")
        self.ui.lineEdit_14.setText("")
        self.ui.lineEdit_18.setText("")
        self.ui.lineEdit_12.setText("")
        self.ui.lineEdit_19.setText("")
        self.ui.lineEdit_2.setText("")

#page_delete的页面功能：（1）显示想要删除结点的信息。（2）调用delete函数删除结点和其所有子节点
    def textBrowser_show(self):

        name = self.ui.lineEdit_16.text()
        if name in People.name_map:
            node = People.name_map[name]
            self.ui.textBrowser.append("此人信息：\n"+"姓名： "+node.name+"\n"+"性别： "+node.sex+
                                        "\n"+"职业： "+node.job+"\n"+"生日： "+node.birthday+
                                        "\n"+"出生地： "+node.birthplace+"\n"+"身高： "+node.height+"\n")
        else:
            self.ui.textBrowser.append("查无此人\n")

    def delete_fun(self):
        name = self.ui.lineEdit_16.text()
        if name in People.name_map:
            People.delete(name)
        else:
            self.ui.textBrowser.append("查无此人\n")
        #存入json文档
        file = open(r"name_map.json",'w')
        json_dict = dict()
        for key in People.name_map:
            tmp = People.name_map[key]
            json_dict[key] = tmp.__dict__
        json.dump(json_dict, file)
        file.close()
        print('save after delete: '+str(json_dict))

#page_change的页面功能（1）显示此人目前的信息。（2）选择并修改用户想要修改的信息
    def textBrowser_2_show(self):
        name = self.ui.lineEdit_17.text()
        if name in People.name_map:
            print('name: '+name)
            node = People.name_map[name]
            self.ui.textBrowser_2.append("当前信息:"+"\n"+"姓名: "+node.name+"\n"+"性别："+node.sex+
                                "\n"+"工作："+node.job+"\n"+"生日："+node.birthday+
                                "\n"+"出生地："+node.birthplace+"\n"+"身高："+node.height+"\n"+"父亲名字："+node.father_name+
                                "\n"+"母亲名字："+node.mother_name+"\n"+"孩子："+str(node.children)+
                                "\n"+"死亡日期："+node.deathdate+"\n"+"年龄："+node.age+"\n")
        else:
            self.ui.textBrowser_2.append("查无此人\n")

    def change_fun(self):
        name = self.ui.lineEdit_17.text()
        info_1 = self.ui.comboBox_2.currentText()
        info_2 = self.ui.lineEdit_10.text()
        People.change(info_1,info_2,name)

#page_search的页面功能：按照程序给定的亲缘关系搜索成员结点
    def search_fun(self):
        name = self.ui.lineEdit_11.text()
        if name in People.name_map:
            node = People.name_map[name]
            info_1 = self.ui.comboBox_3.currentText()
            if info_1 == "父亲":
                if node.father_name in People.name_map:
                    node_f = People.search_father(name)
                    self.ui.textBrowser_3.append("姓名："+node_f.name+"\n"+"性别："+node_f.sex+
                                            "\n"+"工作："+node_f.job+"\n"+"出生日期："+node_f.birthday+
                                            "\n"+"出生地："+node_f.birthplace+"\n"+"身高："+node_f.height+"\n")
                else:
                    self.ui.textBrowser_3.append("未录入父亲信息\n")

            if info_1 == "母亲":
                if node.mother_name in People.name_map:
                    node_m = People.search_mother(name)
                    self.ui.textBrowser_3.append("姓名："+node_m.name+"\n"+"性别："+node_m.sex+
                                            "\n"+"工作："+node_m.job+"\n"+"出生日期："+node_m.birthday+
                                            "\n"+"出生地："+node_m.birthplace+"\n"+"身高："+node_m.height+"\n")
                else :
                    self.ui.textBrowser_3.append("未录入母亲信息\n")

            if info_1 == "配偶":
                if node.couple_name in People.name_map:
                    node_c = People.search_couple(name)
                    self.ui.textBrowser_3.append("姓名："+node_c.name+"\n"+"性别："+node_c.sex+
                                            "\n"+"工作："+node_c.job+"\n"+"出生日期："+node_c.birthday+
                                            "\n"+"出生地："+node_c.birthplace+"\n"+"身高："+node_c.height+"\n")
                else :
                    self.ui.textBrowser_3.append("未录入配偶信息\n")
            #问
            if info_1 == "兄弟姐妹":
                borses = People.search_bors(name)
                if len(borses)==0:
                    self.ui.textBrowser_3.append("没有兄弟信息")
                else:
                    for bors in borses:
                        node_bors = People.name_map[bors]
                        self.ui.textBrowser_3.append("姓名："+node_bors.name+"\n"+"性别："+node_bors.sex+
                                                    "\n"+"工作："+node_bors.job+"\n"+"出生日期："+node_bors.birthday+
                                                    "\n"+"出生地："+node_bors.birthplace+"\n"+"身高："+node_bors.height+"\n")

            if info_1 =="孩子":
                children = People.search_children(name)
                if len(children)==0:
                    self.ui.textBrowser_3.append("未录入孩子信息")
                else:
                    for child in children:
                        node_ch = People.name_map[child]
                        self.ui.textBrowser_3.append("姓名："+node_ch.name+"\n"+"性别："+node_ch.sex+
                                            "\n"+"工作："+node_ch.job+"\n"+"出生日期："+node_ch.birthday+
                                            "\n"+"出生地："+node_ch.birthplace+"\n"+"身高："+node_ch.height+"\n")
        else:
            self.ui.textBrowser_3.append("输入的人不存在\n")

#page_count的页面功能：用于统计整个家谱成员的总人数、平均身高、平均年龄
    def count_fun(self):
        #应该没问题
        if People.name_map is not None:
            i = 0
            all_height = 0
            all_age = 0
            for name in People.name_map:
                node = People.name_map[name]
                i = i+1
                x = int(node.height)
                y = int(node.age)
                all_height = all_height+x
                all_age = all_age+y
            avr_height = all_height/i
            avr_age = all_age/i
        else:
            avr_height = 0
            avr_age = 0
            i = 0

        self.ui.label_9.setText(F"平均年龄:{avr_age}岁")
        self.ui.label_10.setText(F"平均身高:{avr_height}  cm")
        self.ui.label_35.setText(F"家族总人口:{i}人")
        
#page_show的页面功能
    #利用递归遍历输入结点的所有子孙结点，并且利用QTreeWidgetItem完成每个结点的可视化
    def get_map(self,node,root):
            for child_name in node.children:
                node_child = People.name_map[child_name]
                if node_child.children is not None:
                    child_root = QTreeWidgetItem(root)
                    child_root.setText(0,node_child.name)
                    self.get_map(node_child,child_root)
                else:
                    child = QTreeWidgetItem(root)
                    child.setText(0,node_child.name)

    #调用get_map函数，完成树的可视化
    def show_fun(self):
        name = self.ui.lineEdit_3.text()
        root = QTreeWidgetItem(self.ui.treeWidget)
        #如果字典中存在该索引
        if name in People.name_map:
            node = People.name_map[name]
            root.setText(0,node.name)
            if node.children is not None:
                self.get_map(node,root)
        #如果字典不存在
        else:
            root.setText(0,"查无此人")
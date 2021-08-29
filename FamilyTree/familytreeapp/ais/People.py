import json
from PyQt5.QtCore import pyqtSignal

name_map = dict()

#定义用来表示家族成员的person类
class Person():
    #成员信息的初始化
    def __init__(self, name="", birthday="",
                 birthplace="", deathdate="",
                 height=0, sex="", job="",
                 children=[], father_name="",
                 mother_name="", couple_name="",
                 age=""):

        self.name = name
        self.birthday = birthday
        self.birthplace = birthplace
        self.deathdate = deathdate
        self.height = height
        self.sex = sex
        self.job = job
        self.children = children
        self.father_name = father_name
        self.mother_name = mother_name
        self.couple_name = couple_name
        self.age = age

  
#添加家族成员时调用该函数
def add(node):
    
    #建立成员之间的关系
    name_map[node.name] = node
    if node.father_name in name_map:
        father = name_map[node.father_name]
        father.children += [node.name]
    if node.mother_name in name_map:
        mother = name_map[node.mother_name]
        mother.children += [node.name]
    if node.couple_name in name_map:
        couple = name_map[node.couple_name]
        couple.couple_name = node.name

    print('add: '+str(node))

    #保存在json文件中，进行物理存储
    file = open(r"name_map.json",'w')
    json_dict = dict()
    for key in name_map:
        tmp = name_map[key]
        json_dict[key] = tmp.__dict__
    json.dump(json_dict, file)

#实现删除功能时调用该函数，通过递归删除传入的结点以及其所有孩子结点
def delete(name):
    
    node = name_map[name]
    if node.children is not "":
        for children_name in node.children:
            delete(children_name)
    del name_map[name]
    if node.father_name is not "":
        node_father = name_map[node.father_name]
        node_father.children.remove(name)

    if node.mother_name is not "":
        node_mother = name_map[node.mother_name]
        node_mother.children.remove(name)

#更改家庭成员信息
def change(info_1, info_2, name):
    
    
    node = name_map[name]
    
    if info_1 == "出生地":
        node.birthplace = info_2
    if info_1 == "死亡日期":
        node.deathdate = info_2
    if info_1 == "出生日期":
        node.birthday = info_2
    if info_1 == "身高":
        node.height = info_2
    if info_1 == "职业":
        node.job = info_2
    if info_1 == "年龄":
        node.age = info_2
    #存入json文件
    file = open(r"name_map.json",'w')
    json_dict = dict()
    for key in name_map:
        tmp = name_map[key]
        json_dict[key] = tmp.__dict__
    json.dump(json_dict, file)

#寻找父亲结点
def search_father(name):
    node = name_map[name]
    if node.father_name in name_map:
        node_father = name_map[node.father_name]
        return node_father
    else:
        return "此人信息未录入"

#寻找母亲结点
def search_mother(name):
    node = name_map[name]
    if node.mother_name in name_map:
        node_mother = name_map[node.mother_name]
        return node_mother
    else:
        return "此人信息未录入"

#寻找配偶结点
def search_couple(name):
    node = name_map[name]
    if node.couple_name in name_map:
        node_couple = name_map[node.couple_name]
        return node_couple
    else:
        return "此人信息未录入"

#寻找兄弟姐妹结点
def search_bors(name):
    node = name_map[name]
    bors = []
    if node.father_name in name_map:
        node_father = name_map[node.father_name]
        for name_bors in node_father.children:
            if name_bors!=name:
                bors += [name_bors]
        return bors
    else:
        return "此人信息未录入"

#寻找孩子结点
def search_children(name):
    node = name_map[name]
    return node.children









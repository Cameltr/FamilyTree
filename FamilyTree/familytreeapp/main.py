from familytreeapp.uis.familytreeapp import FamilyTreeApp
import json
import familytreeapp.ais.People as People

#载入json文档
file = open(r"name_map.json", 'r')
json_dict = json.load(file)
for key in json_dict:
    print(key)
    tmp = People.Person()
    tmp.__dict__ = json_dict[key]
    People.name_map[key] = tmp
file.close()

#执行app
app = FamilyTreeApp()
app.exec()
#存入文档
file = open(r"name_map.json",'w')
json_dict = dict()
for key in People.name_map:
    tmp = People.name_map[key]
    json_dict[key] = tmp.__dict__
json.dump(json_dict, file)



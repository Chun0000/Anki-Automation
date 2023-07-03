from mtexam_get_database import get_database
from json_convert import jsonConvertor

mydb = get_database()
name = "molecular"
# subjects = [
#   { id: "path", 'name': "病理學" },
#   { id: "micro", name: "臨床細菌學與黴菌學" },
#   { id: "immuno", name: "臨床血清免疫學" },
#   { id: "biochem", name: "臨床生化學" },
#   { id: "physio", name: "臨床生理學" },
#   { id: "virus", name: "臨床病毒學" },
#   { id: "microscopy", name: "臨床鏡檢學" },
#   { id: "blood", name: "臨床血液學與血庫學" },
#   { id: "molecular", name: "醫學分子檢驗學" },
# ];
collection_name = mydb[name]

collection_name.insert_many(jsonConvertor())

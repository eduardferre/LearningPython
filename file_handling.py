# .txt file

import os

#txt_file = open("./my_file.txt", "r+") # Leer y Escribir
txt_file = open("./my_file.txt", "w+")

#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())

txt_file.write("Eduard\nFerré\n35 anys\nPython")

for line in txt_file.readlines():
    print(line)

txt_file.write("\nEditado")
print(txt_file.readline())

txt_file.close()

with open("./my_file.txt", "a") as my_other_file:
    my_other_file.write("\nEditado otra vez")

#os.remove("./my_file.txt")

txt_file.close()

# .json file

import json

json_file = open("my_json.json", "w+")

json_text = {
    "name": "Eduard",
    "surname": "Ferre",
    "age": 22,
    "language": "Python",
    "github": "https://github.com/eduardferre/LearningPython"
}

json.dump(json_text, json_file, indent=0)

json_file.close()

with open("my_json.json") as my_other_json:
    for line in my_other_json.readlines():
        print(line)

json_dict = json.load(open("my_json.json"))
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("my_csv.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Surname", "Age", "Language", "Github"])
csv_writer.writerow(["Eduard", "Ferre", "22", "Python", "github"])
csv_writer.writerow(["Aleix", "Ferre", "27", "", "github"])

csv_file.close()

with open("my_csv.csv") as my_other_csv:
    for line in my_other_csv.readlines():
        print(line)

# .xlsx file
# import xlrd

# .xml file

import xml
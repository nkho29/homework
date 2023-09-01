import json
import csv
import datetime
import time

#
# person_info = {
#     "Age": "15",
#     "Name": "Nazar",
#     "Surname": "Khomych"
# }
#
# print(type(person_info))
#
# prsninf_data = json.dumps(person_info)
#
# print(type(prsninf_data))
#
# with open("empty_json.json", "w+") as file:
#     json.dump(person_info, file, indent=4)



current_time = datetime.datetime.now()
# current_time = time.localtime()
str_time = str(current_time)
print(current_time)
print(str_time)

with open("empty_txt.txt", "w") as file:
     file.write(str_time)
     file.seek(0)


shop_info = [
    ["OBJECT", "PRICE", "QUANTITY"],
    ["Apples", 10, "kg"],
    ["Oranges", 12, "2kg"],
    ["Bananas", 8, "kg"],
    ["Strawberries", 14, "2kg"]
]

with open("empty_csv.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerows(shop_info[:])

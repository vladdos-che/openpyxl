import json

with open("data_file.json", "r", encoding="UTF-8") as f:
    data = json.load(f)
new_data = list(data.items())


with open("new_data_file_01.json", "w", encoding="UTF-8") as f1:
    json.dump({new_data[0][0]: new_data[0][1]}, f1)

with open("new_data_file_02.json", "w", encoding="UTF-8") as f2:
    json.dump({new_data[1][0]: new_data[1][1]}, f2)

with open("new_data_file_03.json", "w", encoding="UTF-8") as f3:
    json.dump({new_data[2][0]: new_data[2][1]}, f3)

with open("new_data_file_04.json", "w", encoding="UTF-8") as f4:
    json.dump({new_data[3][0]: new_data[3][1]}, f4)

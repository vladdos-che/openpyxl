import json

data = {
    "president": {
        "name": "Бобёр Всемогущий",
        "age": 18
    }
}

with open("data.json", "w", encoding="UTF-8") as f:
    json.dump(data, f)

with open("data.json", "r", encoding="UTF-8") as f:
    new_data = json.load(f)

print(new_data)

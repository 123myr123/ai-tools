
import json
data = {"name": "Joe", "age": 25}
with open("histori.json", "w") as f:
    json.dump(data, f)
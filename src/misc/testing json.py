data = {
    "thing1": ["oof", "blesmon"],
    "thing2": ["dat", "boi", "allan"],
    "thing3": {"boi":"hmm", "wat":"tom"}
        }

import json
with open("data.json", "w") as boi:
    json.dump(data, boi, ensure_ascii=False)

with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(data_loaded)
print(data_loaded["thing1"][1])

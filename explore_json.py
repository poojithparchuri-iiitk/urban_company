import json

with open("data/aiml_labelled_samples.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))

if isinstance(data, list):
    print("Number of records:", len(data))
    print("First record:", data[0])
elif isinstance(data, dict):
    print("Keys:", data.keys())
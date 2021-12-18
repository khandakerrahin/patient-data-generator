import json

def getCondition(name):
    print(name)
    return name

# read JSON file
with open('patients_sample.json') as f:
    data = json.load(f)

# loop through JSON file
for patient in data:
    # print(patient['name'])

    patient['condition'] = getCondition('Yanni')
    patient['trials'] = getCondition('Hans Zimmer')

# dump new JSON file
with open('patients.json', 'w') as f:
    json.dump(data, f, indent=4)
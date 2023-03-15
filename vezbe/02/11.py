# JSON format

import json


ime = input('Unesi ime: ')
prezime = input('Unesi prezime: ')
godine = int(input('Unesi godine: '))

student = {
    "ime" : ime,
    "prezime" : prezime,
    "godine" : godine
}

print(student)

# json.DUMPS(objekat_sa_json-format) sluzi za serijalizaciju
# za pisanje
print(json.dumps(student))

# upis informacija u fajl
with open('./personal.json', 'w') as f:
    json.dump(student, f)


# kako se cita
with open('./personal.json', 'r') as f:
    data = json.load(f)
    print(data)

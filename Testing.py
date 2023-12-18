import json
class Bestilling:
    def to_json(self):
        return {
            "forestilling": self.forestilling,
            "dag": self.dag,
            "sal": self.sal,
            "person": self.person.to_json()
        }

with open('Plasser.json', 'r') as f:
    loaded_person = json.load(f)
    loaded_person_obj = int(loaded_person["Gull"])

plasser = int(input("Skriv inn biletter: "))
ledigplasserny = loaded_person_obj - plasser
ledigplasserny = str(ledigplasserny)
print(loaded_person_obj)

with open('Ledige Plasser.json', 'w') as f:
    json.dump(ledigplasserny, f, indent=2)



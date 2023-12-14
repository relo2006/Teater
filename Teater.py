import json

class Person:
    def __init__(self, navn, adresse, epost, telefon, billetter=None, person_type=""):
        if billetter is None:
            billetter = []
        self.navn = navn
        self.adresse = adresse
        self.epost = epost
        self.telefon = telefon
        self.billetter = billetter
        self.person_type = person_type

    def visBillett(self):
        return self.billetter

    def to_json(self):
        return {
            "navn": self.navn,
            "adresse": self.adresse,
            "epost": self.epost,
            "telefon": self.telefon,
            "billetter": self.billetter,
            "person_type": self.person_type
        }

class Billett:
    def __init__(self, forestilling, dag, sal, person):
        self.forestilling = forestilling
        self.dag = dag
        self.sal = sal
        self.person = person

    def typeBillett(self):
        return self.person.person_type  

    def to_json(self):
        return {
            "forestilling": self.forestilling,
            "dag": self.dag,
            "sal": self.sal,
            "person": self.person.to_json()
        }

    def __str__(self):
        return f'Forestilling: {self.forestilling} \nDag: {self.dag} \nSal: {self.sal} \nPerson: {self.person}'

forestilling1 = str(input("Skriv inn forestilling: "))
dag1 = str(input("Skriv inn dag: "))
sal1 = str(input("Skriv inn sal: "))

# Oppretter billett før person
billett1 = Billett(forestilling1, dag1, sal1, None)

navn1 = str(input("Skriv inn navnet ditt: "))
adresse1 = str(input("Skriv inn adressen din: "))
tlf1 = str(input("Skriv inn telefonnummeret ditt: "))
epost1 = str(input("Skriv inn epostadressen din: "))
alder1 = int(input("Skriv inn alderen din: "))

person_type1 = ""
if alder1 > 19:
    person_type1 = "Ikke student"
else:
    person_type1 = "Student"

# Oppdaterer billett med personinformasjon
person1 = Person(navn1, adresse1, epost1, tlf1, person_type=person_type1)
billett1.person = person1

# Lagrer data i JSON-fil
with open('person1.json', 'w') as f:
    json.dump(person1.to_json(), f, indent=2)

with open('billett1.json', 'w') as f:
    json.dump(billett1.to_json(), f, indent=2)

# Leser data fra JSON-fil
with open('person1.json', 'r') as f:
    loaded_person = json.load(f)
    loaded_person_obj = Person(**loaded_person)

with open('billett1.json', 'r') as f:
    loaded_billett = json.load(f)
    loaded_person_obj = Person(**loaded_billett["person"])
    loaded_billett_obj = Billett(loaded_billett["forestilling"], loaded_billett["dag"], loaded_billett["sal"], loaded_person_obj)

print(loaded_billett_obj.typeBillett())
print(loaded_billett_obj)

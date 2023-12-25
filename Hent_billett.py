import json
import os
navn = str(input("Hva heter du???"))
with open(os.path.join(os.getcwd(), "Personer",f"{navn}.json"), 'r') as f:
        person = json.load(f)

print("Navn:", person["navn"])
print("adresse:", person["adresse"])
print("telefon:", person["telefon"])
print("epost:", person["epost"])
print("Person Type:", person["person_type"])
print("Sal:", person["Sal"])
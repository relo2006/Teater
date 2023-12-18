import json
class Bestilling:
    def __init__(self,gull, solv, bronse):
        self.gull = gull
        self.solv = solv
        self.bronse = bronse
    
    def JSON(self):
        return {
            "Gull": self.gull,
            "Solv": self.solv,
            "Bronse": self.bronse
        }



with open('Plasser.json', 'r') as f:
    loaded_person = json.load(f)
    gullplasser = int(loaded_person["Gull"])
    solvplasser = int(loaded_person["Solv"])
    bronseplasser = int(loaded_person["Bronse"])

plasser_gull = int(input("Skriv inn biletter for plasser av Gull: "))
plasser_solv = int(input("Skriv inn biletter for plasser av Sølv: "))
plasser_bronse = int(input("Skriv inn biletter for plasser av Bronse: "))

gull1 = gullplasser - plasser_gull
solv1 = solvplasser - plasser_solv
bronse1 = bronseplasser - plasser_bronse

gull1 = str(gull1)
solv1 = str(solv1)
bronse1 = str(bronse1)

oppdaterteplasser = Bestilling(gull1,solv1,bronse1)
print(gullplasser)

with open('Ledige Plasser.json', 'w') as f:
    json.dump(oppdaterteplasser.JSON(), f, indent=2)



import json
import os

class Bestilling:
    def __init__(self, gull, solv, bronse):
        self.gull = gull
        self.solv = solv
        self.bronse = bronse
    
    def JSON(self):
        return {
            "Gull": self.gull,
            "Solv": self.solv,
            "Bronse": self.bronse
        }

# Sjekk om 'Ledige Plasser.json' eksisterer
if os.path.exists('Ledige Plasser.json'):
    with open('Ledige Plasser.json', 'r') as f:
        eksisterende_plasser = json.load(f)
else:
    # Hvis filen ikke eksisterer, initialiser med verdier fra 'Plasser.json'
    with open('Plasser.json', 'r') as f:
        start_plasser = json.load(f)
        eksisterende_plasser = start_plasser

sal = str(input("Skriv inn salen du ønsker å bestille billett til (For sal sølv, vennligst skriv inn solv): "))
# Få antall billetter for den nye bestillingen
if sal.lower() == "gull":
    plasser_gull = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Gull: "))
    plasser_solv, plasser_bronse = 0, 0
elif sal.lower() == "solv":
    plasser_solv = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Sølv: "))
    plasser_gull, plasser_bronse = 0, 0
elif sal.lower() == "bronse":
    plasser_bronse = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Bronse: "))
    plasser_gull, plasser_solv = 0, 0
else:
    print("Ugyldig saltype. Velg mellom Gull, Sølv eller Bronse.")
    exit()

ny_bestilling = Bestilling(plasser_gull, plasser_solv, plasser_bronse)

# Oppdater ledige plasser med den nye bestillingen
gullplasser = int(eksisterende_plasser["Gull"])
solvplasser = int(eksisterende_plasser["Solv"])
bronseplasser = int(eksisterende_plasser["Bronse"])

gullplasser -= ny_bestilling.gull
solvplasser -= ny_bestilling.solv
bronseplasser -= ny_bestilling.bronse

oppdaterteplasser = {
    "Gull": str(gullplasser),
    "Solv": str(solvplasser),
    "Bronse": str(bronseplasser)
}

with open('Ledige Plasser.json', 'w') as f:
    json.dump(oppdaterteplasser, f, indent=2)

print("Oppdaterte plasser:")
print(oppdaterteplasser)

kontaktinfo = "Ja"

if kontaktinfo.lower() == "ja":
    navn = str(input("Skriv inn navnet ditt: "))
    adresse = str(input("Skriv inn adressen din: "))
    tlf = str(input("Skriv inn telefonnummeret ditt: "))
    epost = str(input("Skriv inn epostadressen din: "))
    alder = int(input("Skriv inn alderen din: "))

    person_type = ""
    if alder > 19:
        person_type = "Ikke student"
    else:
        person_type = "Student"

    person = {
        "navn": navn,
        "adresse": adresse,
        "telefon": tlf,
        "epost": epost,
        "person_type": person_type
    }

    billett = {
        "person": person
    }

    # Opprett mapper hvis de ikke eksisterer
    if not os.path.exists("Bestillinger"):
        os.makedirs("Bestillinger")
    if not os.path.exists("Personer"):
        os.makedirs("Personer")

    # Lagre personinformasjon i 'Personer' mappe
    with open(os.path.join("Personer", f'{navn}_person.json'), 'w') as f:
        json.dump(person, f, indent=2)

    # Lagre billettinformasjon i 'Bestillinger' mappe
    with open(os.path.join("Bestillinger", f'{navn}_billett.json'), 'w') as f:
        json.dump(billett, f, indent=2)

    print("Kontaktinformasjon lagret.")
else:
    print("Ingen kontaktinformasjon lagret.")

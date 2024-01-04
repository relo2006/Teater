import json
import os
import getpass
import hashlib
import clear
from datetime import datetime, timedelta
import shutil

def vis_datoer(filnavn):
    with open(filnavn, 'r') as fil:
        datoer_data = json.load(fil)

    print("Tilgjengelige datoer:")
    for i, dato in enumerate(datoer_data["tilgjengelige_datoer"], start=1):
        print(f"{i}. {dato}")

def oppdater_json(original_filnavn, ny_filnavn, bestilt_dato):
    # Sjekk om den endrede filen eksisterer, hvis ikke bruk originalen
    if os.path.exists(ny_filnavn):
        shutil.copy(ny_filnavn, original_filnavn)
        filnavn = ny_filnavn
    else:
        filnavn = original_filnavn

    with open(filnavn, 'r') as fil:
        datoer_data = json.load(fil)

    if bestilt_dato in datoer_data["tilgjengelige_datoer"]:
        datoer_data["tilgjengelige_datoer"].remove(bestilt_dato)

        with open(filnavn, 'w') as fil:
            json.dump(datoer_data, fil, indent=2)
        print(f"Dato {bestilt_dato} er fjernet. Oppdatert JSON-fil: {filnavn}")
    else:
        print(f"Dato {bestilt_dato} er ikke tilgjengelig.")

if __name__ == "__main__":
    # Spør etter datoen
    original_filnavn = "original tilgjengelige datoer.json"
    ny_filnavn = "endret tilgjengelige datoer.json"
    
    vis_datoer(ny_filnavn)

    valgt_indeks = int(input("Velg en dato ved å skrive inn tilhørende nummer: "))
    
    with open(ny_filnavn, 'r') as fil:
        datoer_data = json.load(fil)

    if 1 <= valgt_indeks <= len(datoer_data["tilgjengelige_datoer"]):
        bestilt_dato = datetime.strptime(datoer_data["tilgjengelige_datoer"][valgt_indeks - 1], "%d.%m.%Y")
        oppdater_json(original_filnavn, ny_filnavn, bestilt_dato.strftime("%d.%m.%Y"))
        print(f"Du har valgt datoen {bestilt_dato.strftime('%d.%m.%Y')} for bestilling.")
    else:
        print("Ugyldig valg. Vennligst velg en gyldig dato.")



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

def generate_hash(password):
    # Bruk en kryptografisk hashfunksjon, for eksempel SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def salfunc():
    while True:
        sal = str(input("Skriv inn salen du ønsker å bestille billett til (For sal sølv, vennligst skriv inn solv): "))

        if sal.lower() not in ['gull', 'solv', 'bronse']:
            print("Ugyldig saltype. Velg mellom Gull, Sølv eller Bronse.")
        else:
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

            # Sjekk om antall plasser er mindre enn 0
            if plasser_gull < 0 or plasser_solv < 0 or plasser_bronse < 0:
                print("Antall plasser kan ikke være mindre enn 0. Vennligst velg en annen sal.")
            else:
                return sal, plasser_gull, plasser_solv, plasser_bronse

# Sjekk om 'Ledige Plasser.json' eksisterer
if os.path.exists('Ledige Plasser.json'):
    with open('Ledige Plasser.json', 'r') as f:
        eksisterende_plasser = json.load(f)
else:
    # Hvis filen ikke eksisterer, initialiser med verdier fra 'Plasser.json'
    with open('Plasser.json', 'r') as f:
        start_plasser = json.load(f)
        eksisterende_plasser = start_plasser

# Henter inn sal
sal, plasser_gull, plasser_solv, plasser_bronse = salfunc()

ny_bestilling = Bestilling(plasser_gull, plasser_solv, plasser_bronse)

# Oppdater ledige plasser med den nye bestillingen
gullplasser = int(eksisterende_plasser["Gull"])
solvplasser = int(eksisterende_plasser["Solv"])
bronseplasser = int(eksisterende_plasser["Bronse"])

gullplasser -= ny_bestilling.gull
solvplasser -= ny_bestilling.solv
bronseplasser -= ny_bestilling.bronse

# Sjekk på nytt om antall plasser er mindre enn 0 etter oppdateringen
if gullplasser < -1 or solvplasser < -1 or bronseplasser < -1:
    print("Antall plasser kan ikke være mindre enn 0 etter oppdateringen. Velg en annen sal.")

    # Loop for å spørre etter en ny sal
    while True:
        sal, plasser_gull, plasser_solv, plasser_bronse = salfunc()
        if sal.lower() in ['gull', 'solv', 'bronse']:
            break
        else:
            print("Ugyldig saltype. Velg mellom Gull, Sølv eller Bronse.")

if solvplasser < -1:
    solvplasser = 0
elif bronseplasser < -1:
    bronseplasser = 0
elif gullplasser < -1:
    gullplasser = 0

oppdaterteplasser = {
    "Gull": str(gullplasser),
    "Solv": str(solvplasser),
    "Bronse": str(bronseplasser)
}
with open('Ledige Plasser.json', 'w') as f:
    json.dump(oppdaterteplasser, f, indent=2)

print("Tilgjengelige plasser igjen:")
print(oppdaterteplasser)

# Løkke for å få kontaktinformasjonen inntil alt er fylt inn
while True:
    navn = str(input("Skriv inn navnet ditt: "))
    adresse = str(input("Skriv inn adressen din: "))
    tlf = str(input("Skriv inn telefonnummeret ditt: "))
    epost = str(input("Skriv inn epostadressen din: "))
    alder = int(input("Skriv inn alderen din: "))
    passord = getpass.getpass("Oppgi et passord for billetten: ")
    hashed_passord = generate_hash(passord)

    if navn and adresse and tlf and epost and passord and alder:
        break
    else:
        print("Vennligst fyll ut all kontaktinformasjon.")

person_type = "Ikke student" if alder > 19 else "Student"

billetter = 0
if sal.lower() == "gull":
    plasser_gull = billetter 
elif sal.lower() == "solv":
    plasser_solv = billetter
elif sal.lower() == "bronse":
    plasser_bronse = billetter

person = {
    "navn": navn,
    "adresse": adresse,
    "telefon": tlf,
    "epost": epost,
    "passord": hashed_passord,  # Lagre hashverdien av passordet
    "person_type": person_type,
    "Dato": bestilt_dato.strftime('%d.%m.%Y'),
    "Billetter": billetter,
    "Sal": sal
}

# Opprett mapper hvis de ikke eksisterer
if not os.path.exists("Personer"):
    os.makedirs("Personer")

# Lagre personinformasjon i 'Personer' mappe
with open(os.path.join("Personer", f'{epost}.json'), 'w') as f:
    json.dump(person, f, indent=2)

    
print(f"Du har valgt datoen {bestilt_dato.strftime('%d.%m.%Y')} for bestilling.")
print("Billetten har blitt lagret.")

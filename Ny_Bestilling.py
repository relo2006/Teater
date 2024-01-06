import json
import os
import getpass
import hashlib
import clear
from datetime import datetime
import shutil
import smtplib
import random
import string

def vis_datoer(filnavn, filnavn2):
    if os.path.exists(filnavn2):
        with open(filnavn2, 'r') as fil:
            datoer_data = json.load(fil)
        print("Folk har bestilt fra før", end="\n")
    else:
        with open(filnavn, 'r') as fil:
            datoer_data = json.load(fil)
        print("Gratulerer, du er den første til å bestille billett", end="\n")

    print("Viser Tilgjengelige datoer:")
    for i, dato in enumerate(datoer_data["tilgjengelige_datoer"], start=1):
        print(f"{i}. {dato}")

def oppdater_json(original_filnavn, ny_filnavn, bestilt_dato):
    # Kopier originalen til den nye filen hvis den eksisterer
    if os.path.exists(ny_filnavn):
        shutil.copy(ny_filnavn, original_filnavn)
        filnavn = ny_filnavn
    else:
        filnavn = original_filnavn

    try:
        with open(filnavn, 'r') as fil:
            datoer_data = json.load(fil)

        if bestilt_dato.strftime("%d.%m.%Y") in datoer_data["tilgjengelige_datoer"]:
            datoer_data["tilgjengelige_datoer"].remove(bestilt_dato.strftime("%d.%m.%Y"))

            with open(ny_filnavn, 'w') as fil:
                json.dump(datoer_data, fil, indent=2)
            print(f"Dato {bestilt_dato.strftime('%d.%m.%Y')} er fjernet. Oppdatert JSON-fil: {ny_filnavn}")
    except FileNotFoundError:
        print(f"Fil {filnavn} ikke funnet.")



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


print("Tilgjengelige plasser igjen:")
print(oppdaterteplasser)

def generate_verification_code():
    # Generer en tilfeldig kode med lengde 6
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_verification_email(to_email, verification_code):
    # E-postdetaljer
    sender_email = "temp15293@gmail.com"
    sender_password = "bfjf bsua wfhd nrqx"
    smtp_server = "smtp.gmail.com"

    # E-postinnstillingene
    subject = "Verifikasjonskode"
    body = f"Din verifikasjonskode er: {verification_code}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Logg inn på e-postserveren
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send e-post
            server.sendmail(sender_email, to_email, message)
        print("E-post med verifikasjonskode sendt suksessfullt.")
    except Exception as e:
        print(f"Feil ved sending av e-post: {e}")

def main():
    navn = str(input("Skriv inn navnet ditt: "))
    adresse = str(input("Skriv inn adressen din: "))
    tlf = str(input("Skriv inn telefonnummeret ditt: "))
    epost = str(input("Skriv inn epostadressen din: "))
    alder = int(input("Skriv inn alderen din: "))

    verification_code = generate_verification_code()
    send_verification_email(epost, verification_code)
    user_input = input("Skriv inn verifikasjonskoden fra e-posten: ")
    if user_input == verification_code:
        print("Koden er riktig. Brukeren er verifisert.")
    else:
        print("Feil kode. Brukeren er ikke verifisert.")
    return navn, adresse, tlf, epost, alder

if __name__ == "__main__":
    navn, adresse, tlf, epost, alder = main()

person_type = "Ikke student" if alder > 19 else "Student"

billetter = 0
if sal.lower() == "gull":
    plasser_gull = billetter 
elif sal.lower() == "solv":
    plasser_solv = billetter
elif sal.lower() == "bronse":
    plasser_bronse = billetter




if __name__ == "__main__":
    original_filnavn = "original tilgjengelige datoer.json"
    ny_filnavn = "endret tilgjengelige datoer.json"
    vis_datoer(original_filnavn, ny_filnavn)

    valgt_indeks = int(input("Velg en dato ved å skrive inn tilhørende nummer: "))

    if os.path.exists(ny_filnavn):
        with open(ny_filnavn, 'r') as fil:
            datoer_data = json.load(fil)
    else:
        with open(original_filnavn, 'r') as fil:
            datoer_data = json.load(fil)

    if 1 <= valgt_indeks <= len(datoer_data["tilgjengelige_datoer"]):
        bestilt_dato = datetime.strptime(datoer_data["tilgjengelige_datoer"][valgt_indeks - 1], "%d.%m.%Y")
        oppdater_json(original_filnavn, ny_filnavn, bestilt_dato)
        print(f"Du har valgt datoen {bestilt_dato.strftime('%d.%m.%Y')} for bestilling.")
    else:
        print("Ugyldig valg. Vennligst velg en gyldig dato.")


person = {
    "navn": navn,
    "adresse": adresse,
    "telefon": tlf,
    "epost": epost,
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

with open('Ledige Plasser.json', 'w') as f:
    json.dump(oppdaterteplasser, f, indent=2)
    
print(f"Du har valgt datoen {bestilt_dato.strftime('%d.%m.%Y')} for bestilling.")
print("Billetten har blitt lagret.")

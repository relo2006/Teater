import json
import os
import clear
from datetime import datetime
import smtplib
import random
import string
import shutil

def vis_datoer(filnavn, filnavn2):
    if os.path.exists(filnavn2):
        with open(filnavn2, 'r') as fil:
            datoer_data = json.load(fil)
    else:
        with open(filnavn, 'r') as fil:
            datoer_data = json.load(fil)

    print("Tilgjengelige datoer:")
    for i, dato in enumerate(datoer_data["tilgjengelige_datoer"], start=1):
        print(f"{i}. {dato}")

def oppdater_json(original_filnavn, ny_filnavn, bestilt_dato):
    if os.path.exists(ny_filnavn):
        shutil.copy(ny_filnavn, original_filnavn)
        filnavn = ny_filnavn
    else:
        filnavn = original_filnavn

    with open(filnavn, 'r') as fil:
        datoer_data = json.load(fil)

    if bestilt_dato in datoer_data["tilgjengelige_datoer"]:
        datoer_data["tilgjengelige_datoer"].remove(bestilt_dato)

        with open(ny_filnavn, 'w') as fil:
            json.dump(datoer_data, fil, indent=2)
    else:
        print(f"Dato {bestilt_dato} er ikke tilgjengelig.")

def send_verification_email(to_email, verfisering_kode):
    sender_email = "temp15293@gmail.com"
    sender_password = "bfjf bsua wfhd nrqx"
    smtp_server = "smtp.gmail.com"

    tittel = "Verifikasjonskode"
    meldingen = f"Din verifikasjonskode er: {verfisering_kode}"
    hele_epost = f"tittel: {tittel}\n\n{meldingen}"

    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, hele_epost)
        print("E-post med verifikasjonskode sendt suksessfullt.")
    except Exception as e:
        print(f"Feil ved sending av e-post: {e}")

def verfiseringkodefunc():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

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

def salfunc():
    while True:
        sal = str(input("Skriv inn salen du ønsker å bestille billett til (For sal sølv, vennligst skriv inn solv): "))

        if sal.lower() not in ['gull', 'solv', 'bronse']:
            print("Ugyldig saltype. Velg mellom Gull, Sølv eller Bronse.")
        else:
            if sal.lower() == "gull":
                plasser_gull = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Gull: "))
                plasser_solv, plasser_bronse = 0, 0
            elif sal.lower() == "solv":
                plasser_solv = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Sølv: "))
                plasser_gull, plasser_bronse = 0, 0
            elif sal.lower() == "bronse":
                plasser_bronse = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Bronse: "))
                plasser_gull, plasser_solv = 0, 0

            if plasser_gull < 0 or plasser_solv < 0 or plasser_bronse < 0:
                print("Antall plasser kan ikke være mindre enn 0. Vennligst velg en annen sal.")
            else:
                return sal, plasser_gull, plasser_solv, plasser_bronse

if os.path.exists('Ledige Plasser.json'):
    with open('Ledige Plasser.json', 'r') as f:
        eksisterende_plasser = json.load(f)
else:
    with open('Plasser.json', 'r') as f:
        start_plasser = json.load(f)
        eksisterende_plasser = start_plasser

sal, plasser_gull, plasser_solv, plasser_bronse = salfunc()

ny_bestilling = Bestilling(plasser_gull, plasser_solv, plasser_bronse)

gullplasser = int(eksisterende_plasser["Gull"])
solvplasser = int(eksisterende_plasser["Solv"])
bronseplasser = int(eksisterende_plasser["Bronse"])

gullplasser -= ny_bestilling.gull
solvplasser -= ny_bestilling.solv
bronseplasser -= ny_bestilling.bronse

if gullplasser < -1 or solvplasser < -1 or bronseplasser < -1:
    print("Antall plasser kan ikke være mindre enn 0 etter oppdateringen. Velg en annen sal.")

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

    print(f"Du har valgt datoen {bestilt_dato.strftime('%d.%m.%Y')} for bestilling.")
else:
    print("Ugyldig valg. Vennligst velg en gyldig dato.")

while True:
    navn = str(input("Skriv inn navnet ditt: "))
    adresse = str(input("Skriv inn adressen din: "))
    tlf = str(input("Skriv inn telefonnummeret ditt: "))
    epost = str(input("Skriv inn epostadressen din: "))
    alder = int(input("Skriv inn alderen din: "))

    if navn and adresse and tlf and epost and alder:
        verifikasjonskode = verfiseringkodefunc()
        send_verification_email(epost, verifikasjonskode)

        bruker_verifikasjonskode = input("Skriv inn verifikasjonskoden sendt til din epost: ")
        if bruker_verifikasjonskode == verifikasjonskode:
            break
        else:
            print("Ugyldig verifikasjonskode. Prøv igjen.")
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
    "person_type": person_type,
    "Dato": bestilt_dato.strftime('%d.%m.%Y'),
    "Billetter": billetter,
    "Sal": sal
}

if not os.path.exists("Personer"):
    os.makedirs("Personer")

with open(os.path.join("Personer", f'{epost}.json'), 'w') as f:
    json.dump(person, f, indent=2)

with open('Ledige Plasser.json', 'w') as f:
    json.dump(oppdaterteplasser, f, indent=2)
    
oppdater_json(original_filnavn, ny_filnavn, bestilt_dato.strftime("%d.%m.%Y"))
print(f"Du har valgt datoen {bestilt_dato.strftime('%d.%m.%Y')} for bestilling.")
print("Billetten har blitt lagret.")
import json
import os
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
    for num, (dato, data) in enumerate(datoer_data["teater"]["datoer"].items(), start=1):
        print(f"{num}. {dato}")

    return datoer_data

def skriv_ut_tilgjengelige_seter(dato_data):
    print(f"Tilgjengelige seter for {valgt_dato}:")
    for num, sete in enumerate(dato_data["seksjoner"][0]["seter"], start=1):
        print(f"{num}. {sete['setenavn']} - {'Opptatt' if sete['opptatt'] else 'Ledig'}")

def sjekk_alle_seter_opptatt(dato, teater_data):
    seksjoner = teater_data["teater"]["datoer"][dato]["seksjoner"]
    
    for seksjon in seksjoner:
        for sete in seksjon["seter"]:
            if not sete["opptatt"]:
                return False  # Hvis et sete ikke er opptatt, returner False

    return True  # Hvis alle seter er opptatt, returner True

def oppdater_json(original_filnavn, ny_filnavn, bestilt_dato, teater_data):
    if bestilt_dato in teater_data["teater"]["datoer"]:
        if sjekk_alle_seter_opptatt(bestilt_dato, teater_data):
            print(f"Alle seter er opptatt på {bestilt_dato}. Kopierer til ny fil...")

            # Kopier originalfilen til den nye kopi
            shutil.copy(original_filnavn, ny_filnavn)

            # Fjern datoen med alle setene opptatt fra den kopierte versjonen
            with open(ny_filnavn, 'r') as kopiert_fil:
                kopiert_data = json.load(kopiert_fil)

            if bestilt_dato in kopiert_data["teater"]["datoer"]:
                del kopiert_data["teater"]["datoer"][bestilt_dato]

                with open(ny_filnavn, 'w') as kopiert_fil:
                    json.dump(kopiert_data, kopiert_fil, indent=2)

                print(f"Dato {bestilt_dato} er fjernet fra den kopierte versjonen.")
            else:
                print(f"Dato {bestilt_dato} er ikke tilgjengelig i den kopierte versjonen.")
        else:
            print(f"Ikke alle seter er opptatt på {bestilt_dato}. Ingen kopiering nødvendig.")
    else:
        print(f"Dato {bestilt_dato} er ikke tilgjengelig i teaterdataene.")

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
        print("Velg mellom: 1 eller 2", end="\n")
        print("1. Vildanden")
        print("2. De elendige")
        forestilling = int(input("Hvilken forestilling har du lyst til å se på: "))
        sal = str(input("Skriv inn salen du ønsker å bestille billett til (For sal sølv, vennligst skriv inn solv): "))
        if sal.lower() not in ['gull', 'solv', 'bronse']:
            print("Ugyldig saltype. Velg mellom Gull, Sølv eller Bronse.")
        else:
            if sal.lower() == "gull":
                plasser_gull = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Gull: "))
                plasser_solv, plasser_bronse = 0, 0
                return sal, plasser_gull, plasser_solv, plasser_bronse, forestilling
            elif sal.lower() == "solv":
                plasser_solv = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Sølv: "))
                plasser_gull, plasser_bronse = 0, 0
                return sal, plasser_gull, plasser_solv, plasser_bronse, forestilling
            elif sal.lower() == "bronse":
                plasser_bronse = int(input("Skriv inn hvor mange billetter du skal kjøpe for plasser av Bronse: "))
                plasser_gull, plasser_solv = 0, 0
                return sal, plasser_gull, plasser_solv, plasser_bronse, forestilling

if os.path.exists('Ledige Saler.json'):
    with open('Ledige Saler.json', 'r') as f:
        eksisterende_plasser = json.load(f)
else:
    with open('Saler.json', 'r') as f:
        start_plasser = json.load(f)
        eksisterende_plasser = start_plasser

sal, plasser_gull, plasser_solv, plasser_bronse, forestilling = salfunc()

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

original_filnavn = "original tilgjengelige datoer og seter.json"
ny_filnavn = "endret tilgjengelige datoer og seter.json"

datoer_data = vis_datoer(original_filnavn, ny_filnavn)

valgt_indeks = int(input("Velg en dato ved å skrive inn tilhørende nummer: "))

if os.path.exists(ny_filnavn):
    with open(ny_filnavn, 'r') as fil:
        datoer_data = json.load(fil)
else:
    with open(original_filnavn, 'r') as fil:
        datoer_data = json.load(fil)

valgt_nummer = int(input("Velg en dato ved å skrive nummeret: "))
valgt_dato = list(datoer_data["teater"]["datoer"].keys())[valgt_nummer - 1]

dato_data = datoer_data["teater"]["datoer"][valgt_dato]




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

billetter = plasser_gull + plasser_solv + plasser_bronse

if sal.lower() == "gull":
    gullplasser += billetter
elif sal.lower() == "solv":
    solvplasser += billetter
elif sal.lower() == "bronse":
    bronseplasser += billetter

pris = 0

# Skriv ut tilgjengelige seter
skriv_ut_tilgjengelige_seter(dato_data)

valgte_seter = []  # Lag en liste for å lagre alle valgte seter

for i in range(billetter):
    while True:
        valgt_sete_nummer = int(input("Velg et sete ved å skrive nummeret: "))
        valgt_sete = dato_data["seksjoner"][0]["seter"][valgt_sete_nummer - 1]

        # Sjekk om setet er opptatt
        if valgt_sete["opptatt"]:
            print(f"Setet {valgt_sete['setenavn']} er allerede opptatt. Velg et annet sete.")
        else:
            # Oppdater setet til opptatt
            valgt_sete["opptatt"] = True

            # Skriv oppdatert JSON tilbake til kopifilen
            with open(ny_filnavn, "w") as fil:
                json.dump(datoer_data, fil, indent=2)

            print(f"Setet {valgt_sete['setenavn']} for {valgt_dato} er nå markert som opptatt.")
            
            valgte_seter.append(valgt_sete)  # Legg til det valgte setet i listen
            break  # Avslutt løkken når et ledig sete er valgt

if alder <= 10:
    pris = 150  # Barn (under 10) får halv pris
    pris = pris * billetter
elif alder <= 18:
    pris = 300 - 60  # Studenter (10-18) får 20% rabatt
    pris = pris * billetter
elif alder >= 67:
    pris = 300 - (0.3 * 300)  # Personer over 67 får 30% honnørrabatt
    pris = pris * billetter
else:
    pris = 300  # Ordinær pris for alle andre
    pris = pris * billetter

forestillingnavn = "Vildanden" if forestilling == 1 else "De elendige"

person = {
    "navn": navn,
    "adresse": adresse,
    "telefon": tlf,
    "epost": epost,
    "person_type": person_type,
    "Dato": valgt_dato,
    "Billetter": billetter,
    "Forestilling": forestillingnavn,
    "Seter": valgte_seter,  # Lagrer alle valgte seter i listen
    "Pris": pris,
    "Sal": sal
}

if not os.path.exists("Personer"):
    os.makedirs("Personer")

with open(os.path.join("Personer", f'{epost}.json'), 'w') as f:
    json.dump(person, f, indent=2)

with open('Ledige Saler.json', 'w') as f:
    json.dump(oppdaterteplasser, f, indent=2)

oppdater_json(original_filnavn, ny_filnavn, valgt_dato, datoer_data)
print(f"Du har valgt datoen {valgt_dato} for bestilling.")
print("Billetten har blitt lagret.")

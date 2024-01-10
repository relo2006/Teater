import json
import os
import smtplib
import random
import string

def verifikasjonskode_func():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_verification_email(to_email, verifikasjonskode):
    sender_email = "temp15293@gmail.com"
    sender_password = "bfjf bsua wfhd nrqx"
    smtp_server = "smtp.gmail.com"

    tittel = "Verifikasjonskode"
    meldingen = f"Din verifikasjonskode er: {verifikasjonskode}"
    hele_epost = f"tittel: {tittel}\n\n{meldingen}"

    try:
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, hele_epost)
        print("E-post med verifikasjonskode sendt suksessfullt.")
    except Exception as e:
        print(f"Feil ved sending av e-post: {e}")

def avbestill_alle_seter(bruker_data):
    if "Seter" in bruker_data and isinstance(bruker_data["Seter"], list):
        print("Oversikt over Setene dine:")
        for sete in bruker_data["Seter"]:
            setenavn = sete["setenavn"]
            opptatt_status = "Opptatt" if sete["opptatt"] else "Ledig"
            print(f"{setenavn} - Status: {opptatt_status}")

        # Avbestill alle opptatte seter
        for sete in bruker_data["Seter"]:
            if sete["opptatt"]:
                sete["opptatt"] = False

        print("Alle opptatte setene er avbestilt.")
    else:
        print("Ingen seteinformasjon tilgjengelig i bruker_data.")

# Sørg for at e-postadressen inneholder '@'
while True:
    to_email = input("Skriv inn din e-postadresse: ")
    if '@' in to_email:
        break
    else:
        print("Ugyldig e-postadresse. Vennligst skriv inn en gyldig e-postadresse med '@'.")

# Generer verifikasjonskode
verification_code = verifikasjonskode_func()

# Sender e-post med verifikasjonskode
send_verification_email(to_email, verification_code)

# Ber brukeren om å skrive inn verifikasjonskoden
while True:
    user_input = input("Skriv inn verifikasjonskoden fra e-posten: ")

    if user_input == verification_code:
        print("Koden er riktig. Brukeren er verifisert.")

        # Henter brukerinformasjon
        bruker_json_fil = os.path.join(os.getcwd(), "Personer", f"{to_email}.json")
        if os.path.exists(bruker_json_fil):
            with open(bruker_json_fil, 'r') as f:
                bruker_data = json.load(f)

            avbestill_alle_seter(bruker_data)

            # Oppdater opptatt-status basert på setenavn i den tilgjengelige JSON-filen
            if bruker_data["Forestilling"] == "De elendige":
                endret_filnavn = "endret gull.json"
            elif bruker_data["Forestilling"] == "Vildanden":
                endret_filnavn = "endre solv.json"

            with open(endret_filnavn, 'r') as endret_fil:
                endret_data = json.load(endret_fil)

            for sete in endret_data["teater"]["datoer"][bruker_data["Dato"]]["seksjoner"][0]["seter"]:
                for bruker_sete in bruker_data["Seter"]:
                    if sete["setenavn"] == bruker_sete["setenavn"]:
                        sete["opptatt"] = False

            with open(endret_filnavn, 'w') as endret_fil:
                json.dump(endret_data, endret_fil, indent=2)

            # Fjern brukerens JSON-fil
            os.remove(bruker_json_fil)
            print(f"Brukerens JSON-fil {bruker_json_fil} er fjernet.")
            
            break  # Avslutt løkken når brukeren er innlogget
        else:
            print("Brukeren med den oppgitte epostadressen eksisterer ikke.")
    else:
        print("Feil kode. Brukeren er ikke verifisert.")

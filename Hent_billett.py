import json
import os
import smtplib
import clear
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

# Spør brukeren om e-postadressen
to_email = input("Skriv inn din e-postadresse: ")

# Generer verifikasjonskode
verification_code = verifikasjonskode_func()

# Sender e-post med verifikasjonskode
send_verification_email(to_email, verification_code)

# Ber brukeren om å skrive inn verifikasjonskoden
user_input = input("Skriv inn verifikasjonskoden fra e-posten: ")

# Sjekker om brukeren skrev inn riktig kode
if user_input == verification_code:
    print("Koden er riktig. Brukeren er verifisert.")

    # Henter og viser brukerinformasjon
    bruker_json_fil = os.path.join(os.getcwd(), "Personer", f"{to_email}.json")
    if os.path.exists(bruker_json_fil):
        with open(bruker_json_fil, 'r') as f:
            bruker_data = json.load(f)

        print("Navn:", bruker_data["navn"])
        print("Adresse:", bruker_data["adresse"])
        print("Telefon:", bruker_data["telefon"])
        print("Epost:", bruker_data["epost"])
        print("Person Type:", bruker_data["person_type"])
        print("Sal:", bruker_data["Sal"])
    else:
        print("Brukeren med den oppgitte epostadressen eksisterer ikke.")
else:
    print("Feil kode. Brukeren er ikke verifisert.")

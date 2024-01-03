import json
import os
import hashlib
import getpass
import clear

epost = str(input("Hva er epostadressen din: "))
passord = getpass.getpass("Skriv inn passordet ditt: ")

# Funksjon for å verifisere passord
def verify_password(stored_hashed_password, input_password):
    hashed_input_password = generate_hash(input_password)
    return stored_hashed_password == hashed_input_password

# Funksjon for å generere hashverdi av passordet
def generate_hash(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Sjekk om brukerens JSON-fil eksisterer
bruker_json_fil = os.path.join(os.getcwd(), "Personer", f"{epost}.json")

if os.path.exists(bruker_json_fil):
    with open(bruker_json_fil, 'r') as f:
        bruker_data = json.load(f)

    # Verifiser passordet
    stored_hashed_password = bruker_data.get("passord", "")
    if verify_password(stored_hashed_password, passord):
        print("Passordet er riktig. Tilgjengelig informasjon:")
        print("Navn:", bruker_data["navn"])
        print("Adresse:", bruker_data["adresse"])
        print("Telefon:", bruker_data["telefon"])
        print("Epost:", bruker_data["epost"])
        print("Person Type:", bruker_data["person_type"])
        print("Sal:", bruker_data["Sal"])
    else:
        print("Feil passord. Tilgang nektet.")
else:
    print("Brukeren med den oppgitte epostadressen eksisterer ikke.")

import json

def oppdater_sete_status(teater_data, dato, setenavn):
    try:
        # Sjekk om datoen er tilgjengelig
        if dato in teater_data["teater"]["datoer"]:
            # Finn riktig seksjon og sete
            for seksjon in teater_data["teater"]["datoer"][dato]["seksjoner"]:
                for sete in seksjon["seter"]:
                    if sete["setenavn"] == setenavn:
                        # Bytt status fra False til True
                        sete["opptatt"] = True
                        print(f"Sete {setenavn} er nå opptatt.")
                        return
            print(f"Feil: Sete {setenavn} ble ikke funnet.")
        else:
            print(f"Feil: Datoen {dato} er ikke tilgjengelig.")
    except KeyError:
        print("Feil: Ugyldig struktur i teaterdata.")

# Simulerer teaterdata (bruk din faktiske teaterdata her)
teater_data = {
    "teater": {
      "datoer": {
        "02.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "03.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "05.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "07.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "08.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "09.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "10.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "12.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "13.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "14.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        },
        "15.02.2024": {
          "seksjoner": [
            {
              "seksjonsnavn": "Hovedsal",
              "seter": [
                {"setenavn": "A1", "opptatt": False},
                {"setenavn": "A2", "opptatt": False},
                {"setenavn": "A3", "opptatt": False},
                {"setenavn": "A4", "opptatt": False},
                {"setenavn": "A5", "opptatt": False},
                {"setenavn": "A6", "opptatt": False},
                {"setenavn": "A7", "opptatt": False},
                {"setenavn": "A8", "opptatt": False},
                {"setenavn": "A9", "opptatt": False},
                {"setenavn": "A10", "opptatt": False},
                {"setenavn": "B1", "opptatt": False},
                {"setenavn": "B2", "opptatt": False},
                {"setenavn": "B3", "opptatt": False},
                {"setenavn": "B4", "opptatt": False},
                {"setenavn": "B5", "opptatt": False},
                {"setenavn": "B6", "opptatt": False},
                {"setenavn": "B7", "opptatt": False},
                {"setenavn": "B8", "opptatt": False},
                {"setenavn": "B9", "opptatt": False},
                {"setenavn": "B10", "opptatt": False},
                {"setenavn": "C1", "opptatt": False},
                {"setenavn": "C2", "opptatt": False},
                {"setenavn": "C3", "opptatt": False},
                {"setenavn": "C4", "opptatt": False},
                {"setenavn": "C5", "opptatt": False},
                {"setenavn": "C6", "opptatt": False},
                {"setenavn": "C7", "opptatt": False},
                {"setenavn": "C8", "opptatt": False},
                {"setenavn": "C9", "opptatt": False},
                {"setenavn": "C10", "opptatt": False}
              ]
            }
          ]
        }
      }
    }
  }


# Spør brukeren om dato og setenavn
dato = input("Skriv inn datoen (dd.mm.åååå): ")
setenavn = input("Skriv inn setenavnet (for eksempel A1): ")

# Oppdater setestatus
oppdater_sete_status(teater_data, dato, setenavn)

# Skriv oppdaterte teaterdata til en fil (valgfritt)
with open('oppdatert_teaterdata.json', 'w') as fil:
    json.dump(teater_data, fil, indent=2)

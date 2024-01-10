print("Velg mellom: 1, 2 eller 2", end="\n")
print("1. For å bestille billett")
print("2. For å se på tidligere bestillinger")
print("3. For å kansellere billetten")
velg = None

while velg is None or velg > 3:
    try:
        velg = int(input("Velg mellom 1, 2 eller 3: "))
    except ValueError:
        print("Vennligst skriv inn et gyldig tall.")



if velg == 1:
    import Ny_Bestilling
elif velg == 2:
    import Hent_billett
elif velg == 3:
    import fjern_billett
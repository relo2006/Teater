print("Velg mellom: 1 eller 2", end="\n")
print("1. For å bestille billett")
print("2. For å se på tidligere bestillinger")
velg = int(input("Velg mellom 1 eller 2: "))

if velg == 1:
    import Ny_Bestilling
elif velg == 2:
    import Hent_billett
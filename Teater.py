class Person:
    def __init__(self, navn, adresse, epost, telefon, billetter = []):
        self.navn = navn
        self.adresse = adresse
        self.epost = epost
        self.telefon = telefon
        self.billetter = billetter

    def visBillett(self):
        for billett in self.billetter:
            print(billett.visInfo())

    def leggTilBillett(self, billett):
        self.billetter.append(billett)

class Billett:
    def __init__(self, forestilling, person):
        self.forestilling = forestilling
        self.person = person
        self.pris = 300
  
    def typeBillett(self, alder, studentstatus = None):
        if alder < 11:
            self.pris = self.pris * 0.5
        elif alder > 66:
            self.pris = self.pris * 0.7
        elif studentstatus == 'student':
            self.pris = self.pris * 0.8
  
    def visInfo(self):
        return f'\nForestilling: {self.forestilling.navn} \nDag: {self.forestilling.dag} \nSal: {self.forestilling.salnavn} \nBestiller: {self.person.navn}'

class Forestilling:
    def __init__(self, navn, sal, dag):
        self.navn = navn
        self.salnavn = sal.navn
        self.dag = dag
        self.ledigeplasser = sal.plasser
  
    def visLedigePlasser(self):
        return self.ledigeplasser
    
    def bestilling(self, billetter):
        self.ledigeplasser += - billetter
        
    

class Sal:
    def __init__(self, navn, plasser):
        self.navn = navn
        self.plasser = plasser

gullsal = Sal('Gull', 150)
sølvsal = Sal('Sølv', 100)
bronsesal = Sal('Bronse', 50)


smalltalk = Forestilling('smalltalk', sølvsal, 'onsdag')
person = Person('navn', 'adresse', 'epost', 'tlf')


def bestilling(person, forestilling):
    antallBilletter = int(input('Antall billetter: '))
    for i in range (antallBilletter):
        alder = int(input(f'Alder på billett {i+1}: '))
        studentstatus = input('skriv "student" om student: ')
        
        billett = Billett(forestilling, person)
        billett.typeBillett(alder, studentstatus)
        person.leggTilBillett(billett)
    
    
bestilling(person, smalltalk)

person.visBillett()



    




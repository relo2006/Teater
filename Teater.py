class Person:
  def __init__(self, navn, adresse, epost, telefon, billetter = [], type = ):
    self.navn = navn
    self.adresse = adresse
    self.epost = epost
    self.telefon = telefon
    self.billetter = billetter

  def visBillett(self):
    return self.billetter

class Billett:
  def __init__(self, forestilling, dag, sal, person):
    self.forestilling = forestilling
    self.dag = dag
    self.sal = sal
    self.person = person
  def typeBillett(self):
    if person
  
  def __str__(self):
    return f'Forestilling: {self.forestilling} \nDag: {self.dag} \nSal: {self.sal} \nPerson: {self.person}'




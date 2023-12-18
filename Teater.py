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
  
  def __str__(self):
    return f'Forestilling: {self.forestilling} \nDag: {self.dag} \nSal: {self.sal} \nPerson: {self.person}'

class Forestilling:
  def __init__(self, navn, sal):
    self.navn = navn
    self.sal = sal

  LedigePlasser = self.sal.plasser
  
  def visLedigePlasser(self):
    return LedigePlasser
    

class Sal:
  def __init__(self, navn, plasser):
    self.navn = navn
    self.plasser = plasser


    




class Dog: 
    def __init__ (self, name, race, age):
        self.name = name
        self.race = race
        self.age = age
        
d1 = Dog("Rocky","Bulldog", 4)
print (f"Il cane si chiama {d1.name} è un {d1.race} e ha { d1.age} anni ")


#Creare 5 classi che contengano almeno tre attributi ispirandosi agli oggetti del mondo reale. Istanziare per ciascuna almeno un oggetto.

class Car:
    def __init__ (self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        
    def run1(self):
        print(self.brand)
        
    def run(self):
        return f"Car {self.brand} is running"
    
    
    def __str__(self):
     return f"L'auto è un' {self.brand} {self.model} di cilindrata {self.engine} turbodiesel"       
    
c1 = Car("Opel", "Astra", 1.4)
c1.run1()
print(c1.run())
 
print(f"La macchina è una {c1.brand} {c1.model} di cilindrata {c1.engine}")
print(c1)



class Pc:
    def __init__(self, model, ssd, graphicCard):
        self.model = model
        self.ssd = ssd
        self.graphicCard = graphicCard
        
    def __str__(self):
        return f"Questo pc {self.model} ha una capacità di {self.ssd} e monta una {self.graphicCard}"
    
p1 = Pc("Asus", "1 Tb", 4070)
print(p1)



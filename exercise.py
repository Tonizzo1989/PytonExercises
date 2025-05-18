"""Crea un dizionario persona avente come chiavi nome, cognome ed età e come valori Mario Rossi 30.
 
 Stampare il valore relativo alla chiave età
 Aggiungere al dizionario la coppia chiave valore email: mario.rossi@gmail.com
 Eliminare la chiave cognome
 Creare una lista contenente tutte le chiavi presenti nel dizionario
 Creare una lista contenente tutti i valori presenti nel dizionario
 Modificare il valore della chiave età presente nel dizionario
 Stampare a video il numero di elementi contenuti nelle liste e nel dizionario alla fine del programma
 """


Person = {
    "name": "Mario",
    "surname": "Rossi",
    "age": 30,

}

#Stampare il valore relativo alla chiave età
print(Person["age"])



#Aggiungere al dizionario la coppia chiave valore email: mario.rossi@gmail.com
Person.update({"email": "mario.rossi@gmail.com"})
print(Person)



#Eliminare la chiave cognome#
Person.pop("surname")
print(Person)
#Devi commentare questa riga altrimenti non stampa la chiave dandoti solo name, age e email



#Creare una lista contenente tutte le chiavi presenti nel dizionario
x = Person.keys()
print(x)



#Creare una lista contenenti tutti i valori presenti nel dizionario
x = Person.values()
print(x)


#Modificare il valore età presente nel dizionario
Person["age"] = 35
print(Person)


#Stampare a video il numero di elementi contenuti nelle liste e nel dizionario alla fine del programma
print(len(Person))




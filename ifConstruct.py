#1) Scrivere un programma che richieda all'utente di inserire un numero da tastiera. 
# Controllare quindi se il numero inserito è positivo, negativo o nullo.



number = int(input("Enter a random number: "))

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is null")
    


#2) Si desidera scrivere un programma che, con febbre 
# alta e con i seguenti sintomi riscontrabili: tosse, febbre,
# stanchezza e difficoltà respiratorie (casi gravi), l'utente 
# ha probabilmente il Covid-19. Se ha i decimi di febbre 
# deve risposare, altrimenti sta bene. Dal momento che si 
# accettano anche temperatura con la virgola, o meglio 
# con il punto decimale, si converta il testo inserito 
# dall'utente con la funzione predefinita eval().



str = input("Do you have any symptoms: ")
if str == "cough":
    print("You got Covid")
elif str == "breathness":
    print("You got Covid")
elif str == "high fever":
    print("You got Covid")
elif str == "tiredness":
    print("You got Covid")
else:
    print("You're fine, just rest")
    
    
       
#3) Dati due numeri da tastiera, a e b, si calcoli, 
# verificando prima che b è diverso da 0, la radice 
# quadrata di a/b.

import math

a = int(input("Number a:"))
b = int(input("Number b:"))

if b!=0:
 squareRt = math.sqrt(a/b)
 print(f"The square root of {a/b} is" , squareRt) 
else:
 print("Not divided by zero")
 

#4 E' possibile assegnare una borsa di studio se il voto dell'esame di stato è compreso tra 75 e 90. 
# Il voto deve essere inserito dall'utente da tastiera.



string = (input("Check if you're eligible for a scholarship, your score must be between 75 and 90."))
grade = int(input("Your score: ")) 
if grade >= 75 or grade >= 90:
 print("Great, you're eligible") 
else:
 print("Sorry, you can't get that")


#5  Per poter viaggiare gratis bisogna iscriversi al sito ed avere i seguenti requisiti: 
# - Fino a 25 anni ed un reddito inferiore ai 15000 euro annui 
# - Dopo i 25 anni ed un reddito inferiore ai 35000 euro annui


 
string = input("Did you login on website?")

if string == "yes":
    age = int(input("Ok,how old are you? : "))
    ral = int(input("Your ral:"))

    if age <= 25 and ral < 15000:
        print("Ok, you can travel for free")
    elif age > 25 and ral < 35000:
        print("Ok, you can travel for free")
    else:
        print("Sorry, you can't travel for free")
else:
    print("You need to log on")

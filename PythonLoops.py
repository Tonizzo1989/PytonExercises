#1) Si scriva un piccolo programma che: 
# 
# - Crei una lista contenente i numeri interi pari tra 10 e 25
# - Utilizza un for loop che utilizzi un range tra 10 e 30 e scarti i numeri dispari 
# e contemporaneamente i numeri minori di 25.
# - E' possibile utilizzare il metodo append

numberList = []
for numberList in range(10, 30, 2):
     print(numberList)
if numberList < 10 and numberList > 30:
    print(numberList)


#2) Si crei un programma che calcoli la lunghezza della parola inserita 
# fino a quando non viene inserita la parola exit.

word = (input("Check the lenght: \n"))
while word != " exit":
    print(len(word))
    word = input("Lenght checked")
 


    
 



      
#3) Inseriti due interi da tastiera, a e b, si stampino tutti i numeri nell'intervallo [a, b] (estremi inclusi) 
# ma escludendo i multipli di 3 e scambiando in automatico i valori di a e b nel caso in cui b fosse minore di a.
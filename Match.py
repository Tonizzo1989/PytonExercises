
season = int (input("Write the season: "))
match season: 
    case 3|4|5:
        print("Spring")
    case 6|7|8:
        print("Summer")
    case 9|10|11:
        print("Autumn")
    case 12|1|2:
        print("Winter")
    case _:
        print("There's no season")
     
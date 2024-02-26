import os
from pronadji_belesku import pronadji_belesku

def pregled_svih_beleski():
    
    pronadjena_beleska = pronadji_belesku()

    if pronadjena_beleska == False:
        os.system('cls')
        print("Broj koji ste uneli ne odgovara ni jednoj beleznici!")
        return
    elif pronadjena_beleska == True:
        os.system('cls')
        return

    beleska_fajl= open(pronadjena_beleska + ".txt", "r")
    sadrzaj_beleske = beleska_fajl.read()

    os.system('cls')
    print ("---------------------")
    print(pronadjena_beleska)
    print ("---------------------")
    print(sadrzaj_beleske)

    print ("---------------------")
    kraj_unos = input("Pitisnite ENTER da se vratite na meni:")
    os.system('cls')
    

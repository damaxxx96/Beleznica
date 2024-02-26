from pronadji_belesku import pronadji_belesku
import os
from pyautogui import typewrite

def izmeni_belesku():
    
    # Pronadji zeljenu belesku za izmenu
    pronadjena_beleska = pronadji_belesku()

    if pronadjena_beleska == False:
        os.system('cls')
        print("Broj koji ste uneli ne odgovara ni jednoj beleznici!")
        return
    
    # Otvaramo fajl da procitamo sadrzaj i odmah zatvaramo fajl
    beleska_fajl= open(pronadjena_beleska + ".txt", "r")
    sadrzaj_beleske = beleska_fajl.read()
    beleska_fajl.close()

    os.system('cls')
    print ("---------------------")
    print(pronadjena_beleska)
    print ("---------------------")

    # Otvaramo fajl i spremamo ga za pisanje
    beleska_fajl = open(pronadjena_beleska+ ".txt", "w")
    typewrite(sadrzaj_beleske)
    izmenjeni_sadrzaj_beleske = input("Izmeni sadrzaj beleske: ")

    if izmenjeni_sadrzaj_beleske == "-MENI":
        return

    # Izmenjeni sadrzaj prepisujemo preko starog sadrzaja
    beleska_fajl.write(izmenjeni_sadrzaj_beleske)
    beleska_fajl.close()
    os.system('cls')
    print("Uspesno izmenjena beleska!")
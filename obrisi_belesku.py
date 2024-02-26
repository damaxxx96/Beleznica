from pronadji_belesku import pronadji_belesku
import os

def obrisi_belesku():

    # Pronadji zeljenu belesku za brisanje
    pronadjena_beleska = pronadji_belesku()

    if pronadjena_beleska == False:
        os.system('cls')
        print("Broj koji ste uneli ne odgovara ni jednoj beleznici!")
        return
    
    # Probaj da obrises fajl
    try:
        os.remove(pronadjena_beleska + '.txt')
        os.system('cls')
        print("Uspesno snimljena beleska!")

    # AKo ne uspes, ispisi sta je bila greska
    except Exception as error:
        os.system('cls')
        print(error)



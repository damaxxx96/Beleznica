import os

def napravi_novu_belesku():
    naslov = input("Unesi naslov: ")
    if naslov == "-MENI":
        os.system('cls')
        return
    beleska = input("Unesi belesku: ")
    if beleska == "-MENI":
        os.system('cls')
        return
    beleska_fajl= open(naslov + ".txt", "a")
    os.system('cls')
    beleska_fajl.write(beleska)
    beleska_fajl.close()
    os.system('cls')
    print("Uspesno snimljena beleska!")
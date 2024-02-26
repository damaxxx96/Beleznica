import os

def pronadji_belesku():
    print("---------------------")
    print("PREGLED SVIH BELESKI")
    print("---------------------")
    
    # Svi fajlovi u folderu
    lista_fajlova = os.listdir()

    # Samo .txt fajlovi koji predstavljaju beleske
    beleske = []
    
    for i in range (0, len(lista_fajlova)):
        fajl = lista_fajlova[i]
        
        # Uzmi zadnja 4 karaktera i proveri da li su jednaki sa .txt
        if fajl[len(fajl) - 4: len(fajl)] == ".txt":
            # Odbaci zadnja 4 karaktera (.txt) i uzmi samo naslov
            beleske.append(fajl[0: len(fajl) - 4])
    
    beleske.sort()
    
    for i in range (0, len(beleske)):
        beleske[i] = str(i + 1) + ". " + beleske[i]
        print(beleske[i])
    
    print("---------------------")
    broj_beleske = input("Unesi broj beleske: ")

    if broj_beleske == "-MENI":
        return True

    for i in range (0, len(beleske)):
        
        # Ako je broj beleske unet sa terminala jednak prvom karakeru od beleske u listi belezaka
        # Prvi karakter ce biti neki broj koji predstavlja numerisani naslov beleznice
        if broj_beleske == beleske[i][0]:
            pronadjena_beleska = beleske[i][3: len(beleske[i])]
            return pronadjena_beleska
    
    # Ako korisnik nije uneo broj beleske koja je bila u listi 
    # Vraticemo False kao izlaz funkcije oznacavajuci gresku
    return False
import os
from napravi_novu_belesku import napravi_novu_belesku
from pregled_svih_beleski import pregled_svih_beleski
from izmeni_belesku import izmeni_belesku
from obrisi_belesku import obrisi_belesku
from izlaz_iz_programa import izlaz_iz_programa
import random

citati = [
    "“Nije važno koliko sporo se krećete dokle god niste stali.” – Konfučije",
    "“Najbolji način da započnete nešto jeste da prestanete da pričate o tome i krenete u akciju.” – Volt Dizni",
    "“Pesimista u svakoj mogućnosti vidi problem. Optimista u svakom problemu vidi mogućnost.” – Kerol Barnet",
    "“Govori polako, ali misli brzo.” – Dalaj Lama",
    "“Misli dobro, pa će dobro i biti.” – Ivo Andrić"
    ]

while True:
    print("------------------------")
    print("------|BELEZNICA|-------")
    print("------------------------")
    print("1. Napravi novu belesku")
    print("2. Pregled svih beleski")
    print("3. Izmeni belesku")
    print("4. Obrisi belesku")
    print("5. Izlaz iz programa")
    print("------------------------")
    print("Ako zelite da se vratite")
    print("na meni ukucajte -MENI")
    print("------------------------")
    
    unos = input("Unesite broj: ")
    
    if unos == "1": 
        os.system('cls')     
        napravi_novu_belesku()
    elif unos == "2":
        os.system('cls') 
        pregled_svih_beleski()
    elif unos == "3":
        os.system('cls')
        izmeni_belesku()
    elif unos == "4":
        os.system('cls')
        obrisi_belesku()
    elif unos == "5":
        os.system('cls')
        nasumican_broj = random.randrange(0, 4)
        nasumicni_citat = citati[nasumican_broj]
        izlaz_iz_programa(nasumicni_citat)
    else:
        os.system('cls')
        print ("Niste uneli dobar broj!")
        continue
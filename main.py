"""
 File: main.py
 Author: Tiliczki Tibor
 Copyright: 2024, Tiliczki Tibor
 Group: Szoft II-1-E
 Date: 2024-01-26 
 Github: https://github.com/tilitihub/Nobel.git
 Licenc: GNU GPL
"""
import csv

def beolvas():
    nobel_adatok = []
    with open('nobel.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=';')
        header = next(csv_reader)  # Az első sor a fejléc, ne olvassuk be az adatok közé
        for sor in csv_reader:
            nobel_adatok.append(sor)
    return nobel_adatok

# 3. feladat
def artur_mcdonald_tipusa(adatok):
    for sor in adatok:
        evszam, tipus, keresztnev, vezeteknev = sor
        teljesnev = f'{keresztnev} {vezeteknev}'
        if teljesnev == 'Artur B. McDonald':
            return tipus

# 4. feladat
def irodalmi_nobel_2017(adatok):
    for sor in adatok:
        evszam, tipus, keresztnev, vezeteknev = sor
        if evszam == '2017' and tipus == 'irodalmi':
            return f'{keresztnev} {vezeteknev}'

# 5. feladat
def beke_dijazottak_1990tol(adatok):
    beke_dijak = []
    for sor in adatok:
        evszam, tipus, keresztnev, vezeteknev = sor
        if int(evszam) >= 1990 and tipus == 'béke':
            if vezeteknev:  # Szervezet esetén a vezetéknév üres lesz
                beke_dijak.append(f'{keresztnev} {vezeteknev}')
    return beke_dijak

# 6. feladat
def curie_csalad_dijai(adatok):
    curie_dijak = {}
    for sor in adatok:
        evszam, tipus, keresztnev, vezeteknev = sor
        if 'Curie' in vezeteknev:
            if evszam not in curie_dijak:
                curie_dijak[evszam] = []
            curie_dijak[evszam].append(f'{keresztnev} {vezeteknev}')
    return curie_dijak

# 7. feladat
def dijak_szama_tipusonkent(adatok):
    tipusok_szama = {}
    for sor in adatok:
        tipus = sor[1]
        if tipus not in tipusok_szama:
            tipusok_szama[tipus] = 0
        tipusok_szama[tipus] += 1
    return tipusok_szama

# 8. feladat
def orvosi_dijak_fajlba(adatok):
    orvosi_dijak = []
    for sor in adatok:
        evszam, tipus, keresztnev, vezeteknev = sor
        if tipus == 'orvosi':
            orvosi_dijak.append(f'{evszam}: {keresztnev} {vezeteknev}')

    with open('orvosi.txt', 'w', encoding='utf-8') as f:
        for sor in sorted(orvosi_dijak):
            f.write(sor + '\n')

# A fő program
if __name__ == "__main__":
    nobel_adatok = beolvas()

    # 3. feladat
    print("3. feladat:")
    artur_tipusa = artur_mcdonald_tipusa(nobel_adatok)
    print(f"Artur B. McDonald Nobel-díja: {artur_tipusa}")

    # 4. feladat
    print("\n4. feladat:")
    irodalmi_2017 = irodalmi_nobel_2017(nobel_adatok)
    print(f"2017-ben irodalmi Nobel-díjat kapott: {irodalmi_2017}")

    # 5. feladat
    print("\n5. feladat:")
    beke_dijazottak = beke_dijazottak_1990tol(nobel_adatok)
    print("Béke Nobel-díjazottak 1990-től napjainkig:")
    for dijazott in beke_dijazottak:
        print(dijazott)

    # 6. feladat
    print("\n6. feladat:")
    curie_dijak = curie_csalad_dijai(nobel_adatok)
    for evszam, dijak in curie_dijak.items():
        for dij in dijak:
            print(f'{evszam}: {dij}')

    # 7. feladat
    print("\n7. feladat:")
    tipusok_szama = dijak_szama_tipusonkent(nobel_adatok)
    for tipus, darab in tipusok_szama.items():
        print(f'{tipus} díjból összesen {darab} darabot osztottak ki.')

    # 8. feladat
    print("\n8. feladat:")
    orvosi_dijak_fajlba(nobel_adatok)


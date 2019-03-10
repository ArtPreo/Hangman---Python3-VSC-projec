import random
from hangmanwordbank import HANGMANPICS
file_obj = open("text.txt", "r")
praeitas_ilgis = 0
for zodis in file_obj.readlines():
    ilgiausias_zodis = len(zodis[:-1])
    if praeitas_ilgis < ilgiausias_zodis:
        praeitas_ilgis = ilgiausias_zodis
        test = zodis

lygis = input("{} {} 2-{}".format("iveskite", "lygi", praeitas_ilgis))


file_obj = open("text.txt", "r")

zodziu_sarasas=[]
for zodis in file_obj.readlines():
    zodzio_ilgis = len(zodis[:-1])
    if zodzio_ilgis < 8 and zodzio_ilgis >= 2:
        zodziu_sarasas.append(zodis)

print("Testas")
zodis_kuri_reikia_atspeti = random.choice(zodziu_sarasas)

print('Zodis turi', len(zodis_kuri_reikia_atspeti), 'raides')

pasleptas_zodis = "_" * len(zodis_kuri_reikia_atspeti)

print("_" * len(zodis_kuri_reikia_atspeti))

zodis_neatspetas = True
spejimai = 6
skaitliukas = 0

zodis_neatspetas = True
while zodis_neatspetas:
    print("TEST2 ")
    raide_kuria_speti = input("Spekite raide: ")

    if raide_kuria_speti in zodis_kuri_reikia_atspeti:
        paslepto_zodzio_listas = list(pasleptas_zodis)

        for index, raide in enumerate(zodis_kuri_reikia_atspeti):
            if raide == raide_kuria_speti:
                paslepto_zodzio_listas[index] = raide_kuria_speti

        pasleptas_zodis = "".join(paslepto_zodzio_listas)
        print("raide teisinga   ", pasleptas_zodis)
    else:
        print("raides nera")

        if raide_kuria_speti not in zodis_kuri_reikia_atspeti:
            skaitliukas += 1
            print('Likusiu spejimu skaicius:', spejimai - skaitliukas)
            print(HANGMANPICS[skaitliukas])
            zodis_neatspetas = True

        if pasleptas_zodis == zodis_kuri_reikia_atspeti:
            print("Zaidimas laimetas")

        elif spejimai - skaitliukas == 0:
            print("Zaidimas pralaimetas, zodis, kuri reikejo atspeti, buvo = ", zodis_kuri_reikia_atspeti)
            zodis_neatspetas = True

print("Ar noretumete zaisti dar karta?")
print("Jei taip, rasykite 1, jei ne, rasykite 2")

dar_karta = input("> ")
if dar_karta == '1':
 exec(open("./index.py").read())
else:
 print('Bye!')
quit()
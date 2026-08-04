# Gemaakt door: Mirkan Yalçin

import time


print("AD Groepen generator")
print("Ondersteunt het genereren van:\n1. Global Group - Security Group\n2. Domain Local Group - Security Group")
print("\nDeze script is bedoeld voor hen die willen oefenen met Active Directory en/of zijn/haar portfolio\n willen aanvullen met allerlei projecten.\n")
time.sleep(0.75)



while True:

    vraag_groep_setup = ("Weet je al wat voor groep soort en hoeveel groepen je wilt maken? Je kunt kiezen tussen:\n1. Ja\n2. Nee\n3. Afsluiten")
    print(vraag_groep_setup)

    vraag_groep_keuze = input("Maak je keuze: ")

    if vraag_groep_keuze.lower() == "ja" or vraag_groep_keuze == "1":

        print("Wat voor soort groep wil je maken:\n1. Global Group - Security Group\n2. Domain Local Group - Security Group\n\nVoer alleen het getal in, bijv: 1 of 2")

        GroepTypeKeuze = int(input("Keuze: "))
        print(f"Jouw keuze: {GroepTypeKeuze}")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...\n")
        time.sleep(1)
        print("Hoeveel groepen wil je maken?")
        AantalGroepen = int(input("Voer enkel de aantal groepen in cijfers in dat je wilt maken: "))
        print(f"Aantal groepen dat gemaakt gaat worden: {AantalGroepen}")
        break





    elif vraag_groep_keuze.lower() == "nee" or vraag_groep_keuze == "2":
        print("Geen probleem, denk eerst na over de groepen die je wilt maken. Programma wordt afgesloten in 5 seconden")
        print("5..")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3..")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1..")
        time.sleep(1)
        break
        
    elif vraag_groep_keuze == "afsluiten".lower() or vraag_groep_keuze == "3":
        print("Programma wordt afgesloten binnen 5 seconden")
        print("5..")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3..")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1..")
        time.sleep(1)
        exit()

    else:
        print("Ongeldige invoer, je kunt enkel kiezen tussen:\n1. Ja\n2. Nee\n3. Afsluiten")

groepen = {}

GroepNaamID = 0
for groep in range (AantalGroepen):
    GroepNaamID += 1
    GroepNaam = input(f"Groep {GroepNaamID}. Groepnaam: ")
    GroepBeschrijving = input(f"Groep {GroepNaamID}. {GroepNaam} Beschrijving: ")

    groepen[GroepNaamID] = {
        "ID": GroepNaamID,
        "naam": GroepNaam,
        "beschrijving": GroepBeschrijving
    }


    print("\nGemaakte groepen:\n----------------------------------------")
    for groep in groepen:
        if GroepTypeKeuze == 1:
            print(f"Global Group {groepen[groep]["ID"]}: {groepen[groep]["naam"]} met beschrijving: {groepen[groep]["beschrijving"]}")
        elif GroepTypeKeuze == 2:
            print(f"Domain Local Group {groepen[groep]["ID"]}: {groepen[groep]["naam"]} met beschrijving: {groepen[groep]["beschrijving"]}")
    print("----------------------------------------")

while True:
    print("Klopt dit?\n1. Ja, genereer CSV\n2. Nee, groep naam of beschrijving wijzigen\n3. Terug gaan\n")
    time.sleep(0.75)
    BevestigingSamenvatting = input("Maak je keuze: ")

    if BevestigingSamenvatting == "1" or BevestigingSamenvatting.lower() == "ja":
        print("CSV genereren.")
        time.sleep(0.5)
        print("CSV genereren..")
        time.sleep(0.5)
        print("CSV genereren...")
        time.sleep(0.5)
        print("CSV genereren....")
        time.sleep(0.5)
        print("CSV genereren.....")
        time.sleep(0.5)
        print("CSV genereren......")
        time.sleep(0.5)
        print("CSV genereren.......")
        time.sleep(0.5)
        print("CSV gegenereerd!")
        break



    elif BevestigingSamenvatting == "2" or BevestigingSamenvatting == "nee".lower():
        print(f"De volgende groepen zitten momenteel in de configuratie:\n")

        for groep in groepen:
            print(f"{groepen[groep]["ID"]}. {groepen[groep]["naam"]}")
        print("Keuze menu:\n1. Groepsnaam wijzigen\n2. Groep beschrijving wijzigen\n3. Terug gaan.\n")

    else:
        print("Ongeldige keuze, kies 1, 2 of 3")
        continue


    GroepWijzigingMenuKeuze = input("Keuze: ")

    if GroepWijzigingMenuKeuze == "1":
        for groep in groepen:
            print(f"{groepen[groep]["ID"]}. {groepen[groep]["naam"]}")
        print("Voor welke groep wil je de naam wijzigen? Voer de groep nummer in:")
        GroepNaamWijzigingKeuze = int(input("\nKeuze: "))
        NieuweGroepNaam = input(f"Nieuwe groepnaam: ")
        OudeGroepNaam = groepen[GroepNaamWijzigingKeuze]["naam"]
        groepen[GroepNaamWijzigingKeuze]["naam"] = NieuweGroepNaam
        print("Groepnaam wijzigen....")
        time.sleep(1)
        print(f"Oude groepnaam: {OudeGroepNaam}")
        print(f"Nieuwe groepnaam: {groepen[GroepNaamWijzigingKeuze]["naam"]}\n")
        continue

    elif GroepWijzigingMenuKeuze == "2":
        for groep in groepen:
            print(f"{groepen[groep]["ID"]}. {groepen[groep]["naam"]} - {groepen[groep]["beschrijving"]}")
        print("Voor welke groep wil je de naam wijzigen? Voer de groep nummer in:")
        GroepBeschrijvingWijzigingKeuze = int(input("\nKeuze: "))
        NieuweGroepBeschrijving = input(f"Nieuwe groepbeschrijving: ")
        OudeGroepBeschrijving = groepen[GroepBeschrijvingWijzigingKeuze]["beschrijving"]
        groepen[GroepBeschrijvingWijzigingKeuze]["beschrijving"] = NieuweGroepBeschrijving
        print("Groep beschrijving wijzigen....")
        time.sleep(1)
        print(f"Oude groepbeschrijving: {OudeGroepBeschrijving}")
        print(f"Nieuwe groepbeschrijving: {groepen[GroepBeschrijvingWijzigingKeuze]["beschrijving"]}\n")
        continue

    elif GroepWijzigingMenuKeuze == "3":
        print("Terug naar hoofdmenu...\n")
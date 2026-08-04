# Gemaakt door: Mirkan Yalçin

import time


groepen = {}
GroepNaamID = 0



def welkomscherm():
    print("AD Groepen generator")
    print("Ondersteunt het genereren van:\n- Global Group - Security Group\n- Domain Local Group - Security Group")
    print("\nDeze script is bedoeld voor hen die willen oefenen met Active Directory en/of zijn/haar portfolio\n willen aanvullen met allerlei projecten.\n")
    #time.sleep(0.75)

def hoofdmenu():
    print("Hoofdmenu:\n1. Groepen maken\n2. Groep attributen (Naam of beschrijving) wijzigen\n3. Samenvatting van je configuratie\n4. Configuratie exporteren naar CSV\n5. Afsluiten")
    HM_Keuze = int(input("Keuze: "))
    return HM_Keuze


def groepkeuze_vraag():
    vraag_groep_setup = ("Weet je al wat voor groep soort en hoeveel groepen je wilt maken? Je kunt kiezen tussen:\n1. Ja\n2. Nee\n3. Afsluiten")
    print(vraag_groep_setup)
    GK_vraag = int(input("Keuze: "))
    return GK_vraag

def groepconfiguratie_aanbod():
    print("Wat voor soort groep wil je maken:\n1. Global Group - Security Group\n2. Domain Local Group - Security Group\n\nVoer alleen het getal in, bijv: 1 of 2")

def groepeninvoeren():
    global GroepNaamID

    while True:
        GroepTypeKeuze = int(input("Keuze: "))

        if GroepTypeKeuze == 1 or GroepTypeKeuze == 2:
            break
        else:
            print("Ongeldige invoer! Kies 1 of 2")

    if GroepTypeKeuze == 1:
        GroepType = -2147483646
    elif GroepTypeKeuze == 2:
        GroepType = -2147483644

    print(f"Jouw keuze: {GroepTypeKeuze}")
    print("Hoeveel groepen wil je maken?")
    AantalGroepen = int(input("Voer enkel de aantal groepen in cijfers in dat je wilt maken: "))
    print(f"Aantal groepen dat gemaakt gaat worden: {AantalGroepen}")

    for groep in range(AantalGroepen):
        GroepNaamID += 1
        GroepNaam = input(f"Groep {GroepNaamID}. Groepnaam: ")
        GroepBeschrijving = input(f"Groep {GroepNaamID}. {GroepNaam} Beschrijving: ")

        groepen[GroepNaamID] = {
        "id": GroepNaamID,
        "naam": GroepNaam,
        "beschrijving": GroepBeschrijving,
        "type": GroepType
    }

    return GroepTypeKeuze, AantalGroepen, GroepNaamID, GroepNaam, GroepBeschrijving

def GroepConfigWijzigingMenu():
    print("1. Groepsnaam wijzigen\n2. Groep beschrijving wijzigen\n3. Terug gaan")

def GroepsConfigWijziging():

    Keuze = int(input("Keuze: "))

    if Keuze == 1:
        for groep in groepen:
            print(f"{groepen[groep]["id"]}. {groepen[groep]["naam"]} {groepen[groep]["beschrijving"]}")
        print("Voor welke groep wil je de naam wijzigen? Voer de groepsnummer in:")
        GroepNaamWijzigingKeuze = int(input("Keuze: "))
        NieuweGroepNaam = input("Nieuwe groepnaam: ")
        OudeGroepNaam = groepen[GroepNaamWijzigingKeuze]["naam"]
        groepen[GroepNaamWijzigingKeuze]["naam"] = NieuweGroepNaam
        print("Groepnaam wijzigen....")
        # time.sleep(1)
        print(f"Oude groepnaam: {OudeGroepNaam}\nNieuwe groepnaam: {groepen[GroepNaamWijzigingKeuze]["naam"]}")

    elif Keuze == 2:
        for groep in groepen:
            print(f"{groepen[groep]["id"]}. {groepen[groep]["naam"]} {groepen[groep]["beschrijving"]}")
        print("Voor welke groep wil je de beschrijving wijzigen? Voer de groepsnummer in:")
        GroepBeschrijvingWijzigingKeuze = int(input("Keuze: "))
        NieuweGroepBeschrijving = input("Nieuwe groepsbeschrijving: ")
        OudeGroepBeschrijving = groepen[GroepBeschrijvingWijzigingKeuze]["beschrijving"]
        groepen[GroepBeschrijvingWijzigingKeuze]["beschrijving"] = NieuweGroepBeschrijving
        print("Groepsbeschrijving wijzigen....")
        # time.sleep(1)
        print(f"Oude groepsbeschrijving: {OudeGroepBeschrijving}\nNieuwe groepsbeschrijving: {groepen[GroepBeschrijvingWijzigingKeuze]["beschrijving"]}")

    elif Keuze == 3:
        print("Terug naar hoofdmenu")

    else:
        print("Je kunt alleen kiezen tussen:\n1. Groep naam wijzigen\n2. Groepsbeschrijving wijzigen\n3. Terug naar hoofdmenu")

def samenvatting():
    print(f"Jouw groepsconfiguratie:\n")
    for groep in groepen:
        print(f"{groepen[groep]["id"]}. {groepen[groep]["naam"]} {groepen[groep]["beschrijving"]}\n")

def export_csv():
    export_file_naam = input("Naam voor CSV bestand (ZONDER extensie, zoals example.csv),\ndit moet dus gewoon example heten: ")

    with open(export_file_naam + ".csv", "w") as bestand:
        bestand.write("cn,description,groupType\n")
        for groep in groepen:
            bestand.write(f"{groepen[groep]['naam']},{groepen[groep]['beschrijving']},{groepen[groep]['type']}\n")

welkomscherm()
while True:
    HM_Keuze = hoofdmenu()
    if HM_Keuze == 1:
        GK_vraag = groepkeuze_vraag()
        if GK_vraag == 1:
            groepconfiguratie_aanbod()
            groepeninvoeren()
        elif GK_vraag == 2:
            print("Geen probleem! Bedenk eerst welke groepen je wilt maken en kom dan terug")
            break
        elif GK_vraag == 3:
            print("Programma wordt afgesloten")
            break
        else:
            print("Je kunt alleen een keuze maken tussen:\n1. Ja\n2. Nee\n3. Afsluiten")
            continue
    elif HM_Keuze == 2:
        GroepConfigWijzigingMenu()
        GroepsConfigWijziging()
    elif HM_Keuze == 3:
        samenvatting()
    elif HM_Keuze == 4:
        export_csv()
    elif HM_Keuze == 5:
        print("Programma stopt")
        break
    else:
        print("Je kunt alleen kiezen tussen:")
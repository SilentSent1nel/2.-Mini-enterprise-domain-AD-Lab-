# Gemaakt door: Mirkan Yalçin

# Start script, m.b.v. de libraries: faker en random
from faker import Faker
from faker.providers import internet
import random

fake = Faker("NL-nl")

# Afdelingen en functies dictionary
afdelingen = {
    "IT": [
        "Systeem beheerder",
        "Netwerk beheerder",
        "Helpdesk Technicus",
        "IT Support Specialist",
        "Security Analist",
        "Software Engineer"
    ],
    "HR": [
        "HR Manager",
        "HR Specialist",
        "Recruiter",
        "HR Administrator"
    ],
    "Financieel": [
        "Financiele Analist",
        "Accountant",
        "Finance Manager",
        "Payroll Specialist"
    ],
    "Sales": [
        "Sales Vertegenwoordiger",
        "Account Manager",
        "Sales Manager",
        "Business Ontwikkeling Specialist"
    ],
    "Marketing": [
        "Marketing Specialist",
        "Content Creator",
        "Digitale Marketing Specialist",
        "Marketing Manager"
    ],
    "Management": [
        "CEO",
        "Afdelings Manager",
        "Project Manager",
        "Teamleider"
    ],
    "Operaties": [
        "Operaties Manager",
        "Operaties Specialist",
        "Proces coordinator"
    ],
    "Ondersteuning": [
        "Ondersteuning Engineer",
        "Klanten Service Specialist",
        "Technische Ondersteuning"
    ],
    "Juridisch": [
        "Juridische Adviseur",
        "Compliance Officer",
        "Juridisch assistent"
    ],
    "Logistiek": [
        "Logistiek Coordinator",
        "Supply Chain Specialist",
        "Magazijn Manager"
    ],
    "Administratie": [
        "Kantoor Beheerder",
        "Administratief Medewerker",
        "Directie Assistent"
    ],
    "Onderzoek en Ontwikkeling": [
        "Onderzoeks Engineer",
        "Product Ontwikkelaar",
        "Data Analist",
        "R&D Specialist"
    ]
}

# Statische verdeling aantal personeel per afdeling
AfdelingsVerdeling = {
    "IT": 18,
    "HR": 37,
    "Financieel": 31,
    "Sales": 75,
    "Marketing": 85,
    "Management": 24,
    "Operaties": 170,
    "Ondersteuning": 65,
    "Juridisch": 20,
    "Logistiek": 45,
    "Administratie": 70,
    "Onderzoek en Ontwikkeling": 40
}


# Genereer nummer beginnend met +31 6 en forceer altijd een nummer van 8 karakters na +31 6
def werktelnummer():
    return("+31-6" + str(fake.random_number(digits=8, fix_len=True)))

# Statistieken aantal medewerkers per afdeling
# Hiermee zien we later met een print statement hoeveel personeel er op elk afdeling werkt

aantalIT = 0
aantalHR = 0
aantalFinan = 0
aantalSales = 0
aantalMarketing = 0
aantalManagement = 0
aantalOperaties = 0
aantalOndersteuning = 0
aantalJuridisch = 0
aantalLogistiek = 0
aantalAdministratie = 0
aantalOnderzoekOntwikkel = 0

user_id = 0
personeelsnummer = 0
TeLangeGebruikersnamen = []
gebruikers = []

functie_groepen = {
    "Systeem beheerder": "GG_IT-SysteemAdmins",
    "Netwerk beheerder": "GG_IT-NetwerkAdmins",
    "Helpdesk Technicus": "GG_IT-Helpdesk",
    "IT Support Specialist": "GG_IT-Support",
    "Security Analist": "GG_IT-Security",
    "Software Engineer": "GG_IT-Developers",

    "HR Manager": "GG_HR-Managers",
    "HR Specialist": "GG_HR-Administratie",
    "Recruiter": "GG_HR-Recruitment",
    "HR Administrator": "GG_HR-Administratie",

    "Financiele Analist": "GG_Financieel-Analisten",
    "Accountant": "GG_Financieel-Accountants",
    "Finance Manager": "GG_Financieel-Managers",
    "Payroll Specialist": "GG_Financieel-Payroll",

    "Sales Vertegenwoordiger": "GG_Sales-Vertegenwoordigers",
    "Account Manager": "GG_Sales-AccountManagers",
    "Sales Manager": "GG_Sales-Managers",
    "Business Ontwikkeling Specialist": "GG_Sales-BusinessDevelopment",

    "Marketing Specialist": "GG_Marketing-Specialisten",
    "Content Creator": "GG_Marketing-Content",
    "Digitale Marketing Specialist": "GG_Marketing-Digitaal",
    "Marketing Manager": "GG_Marketing-Managers",

    "CEO": "GG_Management-Directieleden",
    "Afdelings Manager": "GG_Management-Teamleiders",
    "Project Manager": "GG_Management-ProjectManagers",
    "Teamleider": "GG_Management-Teamleiders",

    "Operaties Manager": "GG_Operaties-Managers",
    "Operaties Specialist": "GG_Operaties-Specialisten",
    "Proces coordinator": "GG_Operaties-ProcesCoordinators",

    "Ondersteuning Engineer": "GG_Ondersteuning-Engineers",
    "Klanten Service Specialist": "GG_Ondersteuning-KlantenService",
    "Technische Ondersteuning": "GG_Ondersteuning-TechnischeOndersteuning",

    "Juridische Adviseur": "GG_Juridisch-Adviseurs",
    "Compliance Officer": "GG_Juridisch-Naleving",
    "Juridisch assistent": "GG_Juridisch-Assistenten",

    "Logistiek Coordinator": "GG_Logistiek-Coordinators",
    "Supply Chain Specialist": "GG_Logistiek-SupplyChain",
    "Magazijn Manager": "GG_Logistiek-Warenhuis",

    "Kantoor Beheerder": "GG_Administratie-KantoorManagement",
    "Administratief Medewerker": "GG_Administratie-Assistenten",
    "Directie Assistent": "GG_Administratie-Assistenten",

    "Onderzoeks Engineer": "GG_RnD-Engineers",
    "Product Ontwikkelaar": "GG_RnD-ProductOntwikkeling",
    "Data Analist": "GG_RnD-DataAnalisten",
    "R&D Specialist": "GG_RnD-Engineers"
}

afdeling_groepen = {
    "Onderzoek en Ontwikkeling": "GG_OnderzoekEnOntwikkeling"
}

for afdeling, aantal in AfdelingsVerdeling.items():
    for _ in range(aantal):
        user_id += 1
        personeelsnummer += 1
        personeelsnummer_str = f"{personeelsnummer:06d}"

        voornaam = fake.first_name()
        achternaam = fake.last_name()

        naam = voornaam + " " + achternaam
        email = naam[:3].lower()+achternaam.replace(" ", "").lower()+"@bedrijf.local"
        gebruikersnaam = voornaam[:3].lower() + achternaam.replace(" ", "").lower()

        if len(gebruikersnaam) > 20:
            TeLangeGebruikersnamen.append((user_id, gebruikersnaam))

        telnr = werktelnummer()

        if afdeling == "IT":
            aantalIT += 1
        if afdeling == "HR":
            aantalHR += 1
        if afdeling == "Financieel":
            aantalFinan += 1
        if afdeling == "Sales":
            aantalSales += 1
        if afdeling == "Marketing":
            aantalMarketing += 1
        if afdeling == "Management":
            aantalManagement += 1
        if afdeling == "Operaties":
            aantalOperaties += 1
        if afdeling == "Ondersteuning":
            aantalOndersteuning += 1
        if afdeling == "Juridisch":
            aantalJuridisch += 1
        if afdeling == "Logistiek":
            aantalLogistiek += 1
        if afdeling == "Administratie":
            aantalAdministratie += 1
        if afdeling == "Onderzoek en Ontwikkeling":
            aantalOnderzoekOntwikkel += 1

        functie = random.choice(afdelingen[afdeling])
        OU = afdeling
        groepen = []

        if afdeling in afdeling_groepen:
            groepen.append(afdeling_groepen[afdeling])
        else:
            groepen.append(f"GG_{afdeling}")

        groepen.append(functie_groepen[functie])
        groepen_string = ";".join(groepen)

        gebruikers.append(f"{personeelsnummer_str},{naam},{voornaam},{achternaam},{naam},{gebruikersnaam},{email},{telnr},{afdeling},{functie},{OU},{groepen_string}")

        print(f"{user_id},{personeelsnummer_str},{naam},{email},{werktelnummer()},{gebruikersnaam},{afdeling},{functie}")



print(f"\nAantal personeel per afdeling:\n-------------------------\nIT: {aantalIT}\nHR: {aantalHR}\nFinanciëel: {aantalFinan}\nSales: {aantalSales}\nMarketing: {aantalMarketing}\nOperaties: {aantalOperaties}\nOndersteuning {aantalOndersteuning}\nJuridisch: {aantalJuridisch}\nLogistiek: {aantalLogistiek}\nManagement: {aantalManagement}\nnAdministratie: {aantalAdministratie}\nOnderzoek en Ontwikkeling: {aantalOnderzoekOntwikkel}\n-------------------------")
print(f"Totaal aantal personeel: {sum(AfdelingsVerdeling.values())}\n-------------------------\n")
print(f"Gebruikers met gebruikersnamen langer dan 20 karaktets:")
print("----------------------------------------")
print(f"Totaal: {len(TeLangeGebruikersnamen)} gebruikers")
for gebruiker in TeLangeGebruikersnamen:
    print(f"Gebruiker {gebruiker[0]}: {gebruiker[1]} - Aantal karakters: {len(gebruiker[1])}")
print("----------------------------------------")



export_file_naam = input("Naam voor CSV bestand (ZONDER extensie, zoals example.csv),\ndit moet dus gewoon example heten: ")

with open (export_file_naam + ".csv", "w", encoding="utf-8-sig") as bestand:
    bestand.write("employeeID,cn,givenName,sn,displayName,sAMAccountName,userPrincipalName,telephoneNumber,department,title,OU,Groups\n")
    for gebruiker in gebruikers:
        bestand.write(gebruiker + "\n")
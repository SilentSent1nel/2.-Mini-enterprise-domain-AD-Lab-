# Gemaakt door: Mirkan Yalçin


from faker import Faker
from faker.providers import internet
import random

fake = Faker("NL-nl")


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

user_id = 1

for afdeling, aantal in AfdelingsVerdeling.items():
    for _ in range(aantal):
        user_id += 1
        voornaam = fake.first_name()
        achternaam = fake.last_name()

        naam = voornaam + " " + achternaam
        email = naam[:3].lower()+achternaam.replace(" ", "").lower()+"@bedrijf.local"
        gebruikersnaam = voornaam[:3].lower() + achternaam.replace(" ", "").lower()

        telnr = fake.phone_number()

        # if nummer < 15:
        #     afdeling = "IT"
        # else:
        #     afdeling = random.choice(list(afdelingen.keys()))

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

        print(f"{user_id},{naam},{email},{werktelnummer()},{gebruikersnaam},{afdeling},{functie}")

print(f"\nAantal personeel per afdeling:\n-------------------------\nIT: {aantalIT}\nHR: {aantalHR}\nFinanciëel: {aantalFinan}\nSales: {aantalSales}\nMarketing: {aantalMarketing}\nOperaties: {aantalOperaties}\nOndersteuning {aantalOndersteuning}\nJuridisch: {aantalJuridisch}\nLogistiek: {aantalLogistiek}\nAdministratie: {aantalAdministratie}\nOnderzoek en Ontwikkeling: {aantalOnderzoekOntwikkel}\n-------------------------")
print(f"Totaal aantal personeel: {sum(AfdelingsVerdeling.values())}\n-------------------------")
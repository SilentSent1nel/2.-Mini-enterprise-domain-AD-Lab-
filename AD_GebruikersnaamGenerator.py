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

# Genereer nummer beginnend met +31 6 en forceer altijd een nummer van 8 karakters na +31 6
def werktelnummer():
    return("+31 6" + str(fake.random_number(digits=8, fix_len=True)))

for nummer in range(100):

    user_id = nummer + 1
    voornaam = fake.first_name()
    achternaam = fake.last_name()

    naam = voornaam + " " + achternaam
    email = naam[:3].lower()+achternaam.replace(" ", "").lower()+"@bedrijf.local"
    gebruikersnaam = voornaam[:3].lower() + achternaam.replace(" ", "").lower()

    telnr = fake.phone_number()

    if nummer < 15:
        afdeling = "IT"
    else:
        afdeling = random.choice(list(afdelingen.keys()))

    functie = random.choice(afdelingen[afdeling])

    print(f"{user_id},{naam},{email},{werktelnummer()},{gebruikersnaam},{afdeling},{functie}")
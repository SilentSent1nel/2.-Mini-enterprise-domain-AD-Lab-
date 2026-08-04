# Project Log - AD Lab

Doel:
Een kleine AD enterprise omgeving bouwen met:
- Windows Server Domain Controller
- Windows Client
- Linux Client

## 31-7-2026
### Gestart met dit portfolio project

- Project Log bestand aangemaakt
- Windows Server 2022: Systeem OS geïnstalleerd
- Windows Server 2022: LAN Segment NIC toegevoegd
- Windows Server 2022: voorzien van zijn IP configuratie
- Windows Server 2022: computer name gewijzgid naar: DC01
- Windows Server 2022: beschrijving gewijzigd naar: Domain Controller 01
- Windows Server 2022: Datum en tijd formaat gewijzigd voor eigen gemak

- CLIENT01: Windows 10 Home OS geïnstalleerd
- CLIENT01: LAN Segment NIC toegevoegd
- CLIENT01: Datum en tijd formaat gewijzigd voor eigen gemak
- CLIENT01: PC naam gewijzigd naar "CLIENT01"

- Windows Server 2022: Rollen en functies toegevoegd:
-- Active Directory Domain Services
-- DHCP Server
-- DNS Server
- Windows Server 2022: Server gepromote naar Domain Controller
- DC01: DHCP Scope geconfigureerd en geactiveerd. Range 192.168.100.100-150/24

- CLIENT01: Client aan domein gejoined

## 1-8-2026
- AD_GebruikersnaamGenerator.py script aangemaakt en gepushed naar repository

## 2-8-2026
- AD_GebruikersnaamGenerator.py script bijgewerkt V2
- Directory Scripts aangemaakt
- AD_GebruikersnaamGenerator.py script bijgewerkt V2.1
- AD_GroepGenerator.py aangemaakt

## 4-8-2026
- AD_GroepGenerator.py wordt niet meer gebruikt, maar nog wel beschikbaar.
- Enhanced versie van AD_GroepGenerator.py (AD_GroepGenerator-Enhanced.py) gemaakt.
- GroepGenerator.ps1 gemaakt om de groepen middels een .csv te importeren.
- 12 aangemaakte groepen in groepen.csv via powershell script geïmporteerd
- 600+ gebruikers in gebruikers.csv via powershell script geïmporteerd
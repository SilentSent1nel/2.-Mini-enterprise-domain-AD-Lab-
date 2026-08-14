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

## 7-8-2026
- Ubuntu Desktop: Systeem OS geïnstalleerd
- Ubuntu Desktop: LAN Segment NIC toegevoegd
- Ubuntu Desktop: Machine aan AD gejoined d.m.v. realm
- DC01: Share folder met afdeling folders aangemaakt
-- Deze folders zijn van alle afdelingen gescheiden en niet zichtbaar aan elkaar
- DC01 - Policies geconfigureerd:
-- Share folder tonen
-- Policy "Show first sign-in animation" uitgeschakeld
-- Toegang tot configuratie scherm beperkt, afdeeling IT erft deze policy instellingen NIET
-- Screen saver timeout, na 300 seconden wordt de scherm vergrendeld
-- Verwijderbare toegang zoals USB sticks kunnen niet gebruikt worden
-- Interactieve login bericht
-- Default gast en administrator account uitgeschakeld
-- Firewall actief & MS Defender:
--- Firewall staat actief aan
--- MS Defender: Realtime protection staat aan
--- MS Defender: Cloud protection (MAPS) staat aan
--- MS Defender: 'Block at first sight' staat aan
--- MS Defender: Elke woensdag draait er een geplande scan
--- MS Defender: Detectie voor mogelijk ongewenste applicaties staat ingeschakeld in 'Audit mode'

## 8-8-2026
- AD_GebruikersnaamGenerator.py bijgewerkt
- Nieuwe global en domain local groups aangemaakt
- Gebruikers verwijderd en opnieuw geïmporteerd, nu in de desbetreffende Global Groups
- GebruikersImporteren.ps1 bijgewerkt

## 14-8-2026 en last minute issue's op 15-8-2026
- architectuur.md bijgewerkt
- netwerk plan.md bijgewerkt
- Afdeling share policy zo gewijzigd dat deze share ook op de desktop van de gebruiker komt als snelkoppeling
- Afdeling share folders permissies zo gewijzigd dat de users binnen een afdeling zijn rechten heeft d.m.v. Read Write permissies
--------------------------------------
- BGinfo op DC01 toegevoeegd met de volgende waarden op de desktop:
-- Computer:	<Host Name>
-- Gebruiker:	<User Name>
-- IP-Adres:	<IP Address>
-- Besturings systeem:	<OS Version>
-- Domein:	<Logon Domain>
- Policy "SYS - BGinfo" aangemaakt
- BGInfo-configuratie opgeslagen als Systeem informatie.bgi.
- BGInfo centraal beschikbaar gemaakt via SYSVOL.
- BGInfo automatisch uitgerold naar client-pc's via Group Policy Preferences.
- BGInfo automatisch laten uitvoeren bij het aanmelden van gebruikers via een Scheduled Task.
- BGInfo geconfigureerd zodat nieuwe gebruikers automatisch de EULA accepteren en geen bevestigingspopup krijgen.
- BGInfo succesvol getest op een client met een nieuwe gebruikerssessie.
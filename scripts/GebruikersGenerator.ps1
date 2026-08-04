$gebruikers = Import-Csv "C:\AD-Import\gebruikerstest.csv" | Select-Object -First 1

foreach ($gebruiker in $gebruikers) {
    Write-Host "Naam:" $gebruiker.cn
    Write-Host "Voornaam:" $gebruiker.givenName
    Write-Host "Achternaam:" $gebruiker.sn
    Write-Host "Username:" $gebruiker.sAMAccountName
    Write-Host "Afdeling:" $gebruiker.department
    Write-Host "Functie:" $gebruiker.title
    Write-Host "-------------------------"
}

New-ADUser `
-Name $gebruiker.cn `
-GivenName $gebruiker.givenName `
-Surname $gebruiker.sn `
-DisplayName $gebruiker.displayname `
-SamAccountName $gebruiker.sAMAccountName `
-UserPrincipalName $gebruiker.userPrincipalName `
-EmployeeID $gebruiker.employeeID `
-Department $gebruiker.department `
-Title $gebruiker.title `
-Path "OU=$($gebruiker.department),OU=Gebruikers,DC=bedrijf,DC=local" `
-Enabled $true `
-AccountPassword (ConvertTo-SecureString "Welkom123!" -AsPlainText -Force)
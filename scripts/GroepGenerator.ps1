Import-Module ActiveDirectory

$groepen = Import-Csv "C:\AD-Import\groepen.csv"
$OUPath = "OU=Gebruikers,DC=bedrijf,DC=local"


foreach ($groep in $groepen) {
    if ($groep.groupType -eq "-2147483646") {
        $scope = "Global"
    }
    elseif ($groep.groupType -eq "-2147483644") {
        $scope = "DomainLocal"
    }
    else {
        Write-Host "Onbekend groep type voor $($groep.cn)"
        continue
    }



New-ADGroup `
    -Name $groep.cn `
    -GroupScope $scope `
    -GroupCategory Security `
    -Description $groep.description `
    -Path $OUPath

Write-Host "Groep aangemaakt: $($groep.cn)"
}
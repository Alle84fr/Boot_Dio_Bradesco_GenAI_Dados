
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent


$outPutFile = Join-Path -Path $scriptDirectory -ChildPath "migation.sql"



if(Test-Path $outPutFile){
    Remove-Item
}

$sqlFile = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name


foreach($file in $sqlFile){
    Get-Content $file.FullName | Out-File -Append -FilePath $outPutFile
    "GO" | Out-File -Append -FilePath $outPutFile
}

Write-Host "Arquivos copilados no $outPutFile"

# só ctrl c e v do file e rodar 
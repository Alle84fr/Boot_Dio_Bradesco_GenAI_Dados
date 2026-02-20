#pegar diretório atual da pasta que está 
# $scriptDirectory = nome da variável
# $ cria a variável
# = caminho este caminho
# Split-Path = guarda em um vetor
# -Path = caminho onde está o diretório
# $MyInvocation = variável automática do próprio powershell
#.MyCommand = meu comnado
#.Definition =n definição
# -Parent = quer pagar os filhos, subpastas
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# aquivo de saída
# Join-Path  =junta os caminhos
# -ChildPath = todos os caminhos
# salvar no arquivo migration
$outPutFile = Join-Path -Path $scriptDirectory -ChildPath "migation.sql"

#verificar se diretório já existe, se existe deve deletar e gerar outro

if(Test-Path $outPutFile){
    Remove-Item
}

# pegar conteúdo dos arquivos
# Get-ChildItem = pega todos os itens dos filhos
# -Filter *.sql = filta por arquivos .sql *=todos
# -File | Sort-Object Name = aquivos e odena por nome - ordem de execução por nomes
$sqlFile = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name


# percorrer e colocar tudo no arq - concaternar
# foreach($file in $sqlFile) = para cada files no sqlfile
# -FilePath = caminha de arquivo específico
# Out-File = arq de saída
# Get-Content $file.FullName = ele pega o conteúdo para por no arq de saída, fullname pega nome completo do diretório
# separador para ver onde cada um inicia = "Go" é um texto qualquer
# Out-File -Append -FilePath $outPutFile - vai por o go e por no outputfile

foreach($file in $sqlFile){
    Get-Content $file.FullName | Out-File -Append -FilePath $outPutFile
    "GO" | Out-File -Append -FilePath $outPutFile
}

#mensagem na tela
Write-Host "Arquivos copilados no $outPutFile"

# para executar
# 1° - copy path - ctrl alt c , neste caso C:\Users\arfur\Documents\python_geral\Boot_Dio_Bradesco_GenAI_Dados\02_excel_sql\aula3_card\db_scripts\seeds\to_migration.ps1
# 2° abrir terminal - ctrl j - estar no powershell
# 3° cola o caminho e roda
# retorno Arquivos copilados no C:\Users\arfur\Documents\python_geral\Boot_Dio_Bradesco_GenAI_Dados\02_excel_sql\aula3_card\db_scripts\seeds\migation.sql
# na mesma pasta aparecerá um arq migration.sql
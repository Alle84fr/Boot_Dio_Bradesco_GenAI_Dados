# Desafio
# desenvolva um programa que leia o nome digitado pelo cliente e retorne o mesmo nome, mas com todas as letras convertidas para maiúsculas. Assim, o sistema poderá padronizar os registros e evitar falhas em futuras operações automatizadas. Sua solução precisa ser simples, eficiente e fácil de integrar ao sistema já existente do banco, sem o uso de bibliotecas externas.

# Implemente um programa que leia uma string representando o nome do destinatário de uma transferência e retorne essa mesma string com todas as letras em maiúsculas. O programa deve preservar espaços e outros caracteres que não sejam letras, alterando apenas as letras minúsculas para maiúsculas. Considere que o nome pode conter letras, números e espaços.

# Entrada
# Uma única linha contendo uma string com o nome do destinatário da transferência.

# Saída
# Uma única linha contendo a mesma string da entrada, mas com todas as letras convertidas para maiúsculas.



nome = input("nome: ").upper()
print(nome)
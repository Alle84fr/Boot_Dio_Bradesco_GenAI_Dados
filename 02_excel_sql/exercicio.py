# # Desafio de codigo basico sobre uso de Excel e SQL em contexto de banco e mercado financeiro. Uma equipe de analistas usa planilhas Excel e consultas SQL para acompanhar saldos, limites de credito e historico de transacoes dos clientes. Sua missao e criar um programa que receba o nome de um uso comum de Excel ou SQL no contexto bancario e retorne uma breve descricao desse uso.

# Caso o nome informado nao exista na lista de opcoes, o sistema deve retornar: Tecnica desconhecida.

# Entrada
# O programa deve ler uma string com o nome de um dos usos a seguir:

# "Relatorio de juros em planilha Excel"
# "Tabela de clientes com limite de credito"
# "Consulta SQL de saldo por cliente"
# "Consulta SQL de historico de transacoes"
# Saida
# O programa deve imprimir uma string com a descricao correspondente:

# Calculo de juros sobre saldos usando colunas da planilha
# Lista dados de clientes e campo com limite de credito
# Filtra tabela de contas para mostrar saldo de cada cliente
# Usa SQL para buscar transacoes antigas de uma conta
# Se a entrada nao corresponder a nenhuma das opcoes validas, o programa deve imprimir:

# Tecnica desconhecida

entrada = input().strip()

def descrever_uso(nome):
    if nome == "Relatorio de juros em planilha Excel":
        return "Calculo de juros sobre saldos usando colunas da planilha"

    elif nome == "Tabela de clientes com limite de credito":
        return "Lista dados de clientes e campo com limite de credito"

    elif nome == "Consulta SQL de saldo por cliente":
        return "Filtra tabela de contas para mostrar saldo de cada cliente"

    elif nome == "Consulta SQL de historico de transacoes":
        return "Usa SQL para buscar transacoes antigas de uma conta"

    else:
        return "Tecnica desconhecida"

print(descrever_uso(entrada))

#_______________________________________ 

# Desafio
# Desafio de codigo basico sobre uso de Excel e SQL em contexto de banco e mercado financeiro. Uma equipe de analistas utiliza planilhas e consultas para simular emprestimos, acompanhar gastos e analisar operacoes de cartao dos clientes. Sua missao e criar um programa que receba o nome de um desses usos e retorne uma breve descricao correspondente.

# Caso o nome informado nao exista na lista de opcoes, o sistema deve retornar: Tecnica desconhecida.

# Entrada
# O programa deve ler uma string com o nome de um dos usos a seguir:

# "Planilha Excel de simulacao de parcelas de emprestimo"
# "Relatorio em Excel com resumo de gastos do cliente"
# "Consulta SQL com total de compras no cartao"
# "Consulta SQL listando emprestimos em aberto"
# Saida
# O programa deve imprimir uma string com a descricao correspondente:

# Calcula valor das parcelas com juros sobre o emprestimo
# Mostra resumo mensal dos gastos do cliente no banco
# Soma compras registradas no cartao em uma tabela
# Retorna emprestimos ativos para analise de risco
# Se a entrada nao corresponder a nenhuma das opcoes validas, o programa deve imprimir:

# Tecnica desconhecida

entrada = input().strip()

def descrever_uso(nome):
    if nome == "Planilha Excel de simulacao de parcelas de emprestimo":
        return "Calcula valor das parcelas com juros sobre o emprestimo"

    elif nome == "Relatorio em Excel com resumo de gastos do cliente":
        return "Mostra resumo mensal dos gastos do cliente no banco"

    elif nome == "Consulta SQL com total de compras no cartao":
        return "Soma compras registradas no cartao em uma tabela"

    elif nome == "Consulta SQL listando emprestimos em aberto":
        return "Retorna emprestimos ativos para analise de risco"

    else:
        return "Tecnica desconhecida"

print(descrever_uso(entrada))
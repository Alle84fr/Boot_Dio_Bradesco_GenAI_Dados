# Desafio
# criar um programa simples que, ao receber o preço de abertura e o preço de fechamento de uma ação, informe se ela valorizou, desvalorizou ou permaneceu estável. 

# Implemente um programa que leia dois valores inteiros positivos: o preço de abertura e o preço de fechamento de uma ação. O programa deve comparar os valores e imprimir "ALTA" se o preço de fechamento for maior que o de abertura, "BAIXA" se for menor, ou "ESTAVEL" se forem iguais. Não utilize bibliotecas externas. Considere apenas os dois valores fornecidos na entrada, separados por espaço.

# Entrada
# Uma única linha contendo dois números inteiros positivos separados por espaço, representando respectivamente o preço de abertura e o preço de fechamento da ação.

# Saída
# Uma única palavra: "ALTA", "BAIXA" ou "ESTAVEL", de acordo com a comparação entre os valores de abertura e fechamento.

def comparar(val_a, val_f):
    if val_a > val_f: print("ALTA")
    elif val_a == val_f: print("ESTAVEL")
    else: print("BAIXA")
    
preco_abertura, preco_fechamento = map(int, input("Preço abertura: ").split())

comparar(preco_abertura, preco_fechamento)



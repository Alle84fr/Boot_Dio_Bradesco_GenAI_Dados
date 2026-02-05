# manipulando string

#_____________ métodos úteis, os principais

valor = "PyThoN e jAvA"
espaco = "   <-Espaço->    "
centralizar = "Centro"
juntar = "Abracadraba"


print(f"\nfunção que converte tudo maiúculo = {valor.upper()}\n")
print(f"função que converte tudo minúsculo = {valor.lower()}\n")
print(f"função que converte todas 1° letras em  maiúscula o resto minúsculo = {valor.title()}\n")
print(f"função que tira espaços Atenção é strip ->{espaco.strip()}<-\n")
print(f"função que tira espaço left(esquerda) ->{espaco.lstrip()}<-\n")
print(f"função que tira espaço right(direita) ->{espaco.rstrip()}<-\n")
# o valor numérico é quantidade de "espaços" que usará, contando do 1° ao último
print(f"função que irá centralizar apernas = {centralizar.center(35)}")
print(f"função que irá centralizar com caractere = {centralizar.center(20, "-")}")
# caracteres que serão postos entre a palvra
# usa-se muito com listas o join
print(f"função que irá juntar os caracteres = {"-".join(juntar)}")
print(f"função que irá juntar os caracteres = {" ".join(juntar)}")

#_____________ INTERPOLAÇÃO DE VARIÁVEIS

# eu uso apenas fstring 

# Interpolação de strings é o processo de inserir variáveis dentro de uma string formatada.

inter = "interpolação"
coisa = "coisa"

dic_key_int={
    1: "aA",
    2: "Bb",
    3: "cC", 
    4: "dD"
}

dic_key_str={
    "u": 12,
    "d": 45,
    "t": 69, 
    "q": 73
}

decimal_6 = 12.123456


print("\nNão uso esta %s, e eu não quero usar esta %s" %(inter, coisa))
print("Tem ainda esta froma de {1}, que não é uma boa {0}, {1}".format(coisa, inter))
# forma nomeada
print("Apenas mostrando {inter}, que é muita {coisa} que é isso {x}".format(inter=inter, x="x", coisa=coisa))
print("Aqui ele chamou tudo do dicionário com chave numérica {0}, {1}, {2}, {3}".format(
dic_key_int[1], dic_key_int[4], dic_key_int[3], dic_key_int[2]))
print("Aqui ele chamou tudo do dicionário com chave numérica {u}, {t}, {q}, {d}".format(
**dic_key_str))
print(f"Uso apenas esta {inter} que é uma ótima {coisa}\n")
print(f"Decimal 3 direita {decimal_6:.3f}\n")

casa_direita = 1.0002

# quero valor 01.0002
# tamanho do n° não se vê com len(), se quiser transformar em str, ver tamanho e voltar para float, acho eu que pode mas

# contando 123456
#          1.0002
#depois da , 1234
# total = 6
# depois do . (,) = 4
# quero add um 0 a direita, fivando com 7 de tamanho
# devo por 0 na frente do 7
# variável:07.4f
# f = float

print(f"antes do ponto {casa_direita:07.4f}\n")

#_____________ FATIAMENTO - STR

import re

cpf = "012.365.478-51"
#      01234567890123
limpar = re.sub(r"\D", "", cpf.strip())

# ou posso, neste caso
# replace troca os pontos, traços e espaços por juntar os n°s
outra_forma = cpf.replace(".", "").replace("-","").strip()

# saber 1° caractere
s= cpf[0]
h =cpf[3:]
p = cpf[:5]
# aqui o n° a ser apersentado é um antes do valor posto (pega casa 4,5,6)
u = cpf[4:7]
# ponto inicial:ponto final:casa a pular/andar/step
n = cpf[3:13:4]
f = cpf[:]
m = cpf[:: -1]
y = cpf[9:4:-1]
print(f"\nprinta 1° caractere de 012.365.478-51 = {s}")
print(f"Ignora os 3 primeiros caracteres de 012.365.478-51 = {h}")
print(f"Ignora os caracteres de 012.365.478-51 após o 5 primrios = {p}")
print(f"Pega indice 4 e anda até o 6 no 012.365.478-51  = {u}")
print(f"Pega indice 3, vai até 13, mas andando de 4 em 4 no 012.365.478-51  = {n}")
print(f"Retorna um cópia de 012.365.478-51  = {f}")
print(f"Espelçhamento/ de trás para frente  = {m}")
print(f"Retornando do 9 para 5 = {y}")



# re = Regular Expression - Expressões regulares -> busca, valida, substitui padrões de texto

#.strip() -> remove espaços laterais

# re.sub() -> função que substitui parte do texto com base em um padrão
# re.sub(padrão, substituição, texto)

# r"\d" é uma regex ()
# r"" -> raw string = string crua
# \d = pega qualquer coisa que seja n° entre 0 e 9
# \D = pega qualquer coisa que não seja n°
# subtitua qualquer coisa que não seja n° por nada, sem espaço

#_____________ Multiplas linhas

print("""colocando 3 aspas
      simples ou duplas
várias linhas\n""")

print("Não mostrou mas já fiz\nBarra n\npula linha")

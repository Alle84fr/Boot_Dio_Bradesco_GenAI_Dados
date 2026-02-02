# identação =  espaço, geralmente 4 espaços = um tab
# mantém mais legíveis e manutenível
# determina um blco de comando, onde inicia e termina, no .py não tem entre chaves para mostrar o bloco, como no .java ou .js

def exemplo(c):
     
    if c%2==0:
        valor = "bloco1"
        if valor == "bloco1":
            volta = "Entrou no bloco 2"
        else:
            volta = 3 + conta
    else:
        volta = "Entrou no bloco 1"
        
    return volta
        

c = 8

print(exemplo(c))

# Estrutura condiconada

# aninhado =  um dentro do outro (exemplo é cód acima, dentro da função com os ifs)

# desvio de fluxo de controle (estrutura condicionada)

idade = 19

if idade > 18:
    print("Maior")
    a = 0.5
elif idade == 18:
    print("iniciando a maioridade")
else:
    print("não é maior de idade")

if a == 0.5:
    print("Apenas teste mesmo")

# ternário = função em única linha
# 3 partes
# 1° retorno do caso, caso seja true
# 2° expresão lógica
# retorno caso falso

ternario = "Maior mesmo" if idade >= 18 else "Menor"
print(ternario)

# Estrutura de peretição

# repete um bloco até finalizar sua condição, pode ser n° de repetição conhecida ou não

repete = 1

# o valor vai de 1 a 10, igual no caso for
while repete < 11:
    print (2*repete)
    repete += 1

# aqui repete até o usuário decidir sair
while True:
    d = input("Digita qualquer letra ou s para sair: ").lower()
    if d == "s":
        #break sai do cód
        break
    if d == "c":
        print("Apenas continua")
        continue

opcao = -1

while opcao != 0:
    opcao = int(input("0 - sai, 1 - codar, 2 - dormir: "))
    if opcao == 1: print("Só mais um pouco")
    elif opcao == 2: print("Melhor dormir, continua amanhã")
    elif opcao == 0: print("adeus")
    else: 
        print("Valor errado")
    
    
# no for deve saber quantidade de repetição
lista = [1, 3, 5, 6, 7, 10 , 12]
for i in lista:
    print(i + 2, end=" ")

#só para pular linha
print("\n")   

# vai iniciar no valor 2, irá até 19, pulando de 3 em 3
for n in range(2, 20 , 3):
    print(n, end=" ")

# quebra de linhas
print()

# saber se tem letra
texto = input("testo: ")

vogais = "AEIOU"
bogal = []
cons = []

for Char in texto:
    if Char.upper() in vogais:
        bogal.append(Char)
    else:
        cons.append(Char)
print(bogal)
print(cons)

# Observação, se o ranger não estiver na forma de lista, deve converter
# list(ranger(4)) - assim retona os valor dele

print(list(range(6)))

#tabuada
for i in range (0, 51, 5):
    print(i, end=" ")

# função bloco de cód identificado por um nome e pode receber iuma lista de parâmetros com ou sem valor
# tornaq cód legível e possibilita reaproveitamento de cód

def exibir_mensagem():
    print("saluton")

def exibir_nome(nomes):
    print(f"nome = {nomes}")
    
def exbir_dados(nomes="Não mencionado", idade = None):
    print(f"nome: {nomes} \nidade: {idade}")

# chamando função

exibir_mensagem()

# entrada obrigatório
exibir_nome("Rogério")

# entrada não obrigada
exbir_dados()

# com entrada
# argumentos nomeados
exbir_dados("Joana", 35)

#ou
exbir_dados(nomes="Pablo", idade=75)

#ou
# ** serve para desempacotar um dcit em argumentos noeados ao chamar a função - tranforma em parâmetro
exbir_dados(**{"nomes":"Adilma", "idade": 25})

def suce_ante(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

n = suce_ante(785)
print("\n",n,"\n")

# parametro como *args (strings, numeros ...) o método recebe os valor como tupla
# parametro como **kwargs o método recebe os valor como dict
# não tem de por nome args, tem que por * ou **, a palavra só vem para informar o que se recebe

def exibir_poema(data_extendo, *args, **kwargs):
    #concatenando os valores
    texto = "\n".join(args)
    #.item recebe chave e valor
    #.join é para concatenar
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extendo}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
# chamando função

exibir_poema("Domingo 22 2026", "Zen of Python", "Beatiful is better than ugley", "texto", "mais tesxto", "Tupla de texto", autor="tim petter", ano=1999, chave="valores\n")
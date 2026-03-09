# Dicionário

# Dicionáio conjunto NÃO ORDENADO COM PAR DE CHAVE EVALOR
# Separados por vírgula
# chave nuna repete e é imjtável - ex, string, tupla
# valor pode ser mutável ou imutável

dicionario = {"nome":"Ale", "idade": 15}

ou = dict(nome = "ale", idade=15)

print(dicionario)
print(dicionario["nome"])
print(dicionario["idade"])
# adicionar nova chave e valor

dicionario["tel"] = "333222408"

print(dicionario)
#retorno {'nome': 'Ale', 'idade': 15, 'tel': '333222408'}

# novo valor:
dicionario["nome"]= "Alele"
print(dicionario["nome"])

# dicionário aninhados

dici = {
    0: {"nome":"A", "idade": 15},
    1: {"nome":"B", "idade":20},
    2: {"nome":"C", "idade":78},
    3: {"nome":"D", "idade":78, "endereco": {"rua": "Coronel", "num": 159}},
    4: {"nome":"D", "idade":78, "lista": ["Joa", "juo"]}
}

print(dici)
print(dici[0])
print(dici[2]["nome"])
print(dici[3]["endereco"]["num"])
# aqui, peguei indice e não chave
print(dici[4]["lista"][0])

# ou

idade = dici[1]["idade"]
print(idade)

# iterar dicionário
# passa linha alinha e retorna só chave
# para pegar valor deve chamar dici e chave
for chave in dici:
    print(chave, dici[chave])

    # ou - items retorna lista tuplas com chave evalor
for chave, valor in dici.items():
    print(chave, valor)

# metodos

# fromkeys
#₢riar todas chave com valor none
# dicionario inesistente
dict.fromkeys(["nome", "idade"])

# Criar com valor vazio
# dicionario inesistente
dict.fromkeys(["nome", "idade"], "Vazio")

dici.fromkeys(["caldeira"])

# get - acessar valor

print(dici.get("chave"))
# none = não tem chave

print(dici.get(3))

# tirar none de retorno
print(dici.get("chave", {}))
#{}

print(dici.get(0, {}))

# items
# retorna lista de tuplas
# bom para comando for

listando = dici.items()

#keys

print(dici.keys())
# dict_keys([0, 1, 2, 3, 4])

# pop
# remove chave e pode por valor de retono

remo = dici.pop(4, {})
remo_sem = dici.pop(6, {})
print(remo)
# {'nome': 'D', 'idade': 78, 'lista': ['Joa', 'juo']}
print(remo_sem)
# {}

# setdefault
# se o atributo não tiver, adicona, se tem, retorna valor e não altera

dici.setdefault("\nnome", "A")
print(dici)

dici.setdefault("passo", 5)
print(dici)
# me': 'D', 'idade': 78, 'endereco': {'rua': 'Coronel', 'num': 159}}, '\nnome': 'A', 'passo': 5}

# update - atualiza

dici.update({2: {"nome": "Sei"}})
print("\n",dici[2])
# {'nome': 'Sei'}
# tirou as outras chaves existentes
# se a chave não existe ele adiciona chave

# values

print(dici.values(), "\n")
# dict_values([{'nome': 'A', 'idade': 15}, {'nome': 'B', 'idade': 20}, {'nome': 'Sei'}, {'nome': 'D', 'idade': 78, 'endereco': {'rua': 'Coronel', 'num': 159}}, 'A', 5])

# in
print(dici)

ver = 1 in dici
print(ver)
# True

veri = "ale" in dici
print(veri)
# False

verif = "idade" in dici[3]
print(verif)
# True

verifi = "A" in dici[0]["nome"]
print(verifi)
# True

# del

del dici[3]["nome"]
print(dici[3])
# copy - copia

dicio = dici.copy()


#clear - limpa tudo

dici.clear()

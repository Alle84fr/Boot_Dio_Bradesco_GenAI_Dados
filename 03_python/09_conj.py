# Conjuntos - SETS

# SETS - coelção que não possui objetos repetidos, usamos para representrar conjuntos matemáticos ou eliminar itens duplicados de um iterável
# set não garante a ordem, muda a ordem conforme ele deseja
# NÃO SUPORTA INDEXAÇÃO E NEM FATIAMENTO

# tem uma lista dentro do set
print(set([1,3,5,8,6,1,2,9]))
# retorno {1, 2, 3, 5, 6, 8, 9}

# string
print(set("abacaxi"))
# retorno {'c', 'x', 'i', 'a', 'b'}

# pegando com chave
# no dia a dia usa assim

outro = set(["a", ":", ">",":" ])
print(outro)
# retorno {':', '>', 'a'}

# acessar dados DEVE CONVERTER EM LISTA

o_set = set([1,5,9,2,6,3,1,4,7,8,9])
print(o_set)
# retorno {':', '>', 'a'}

# interar, percorrer
for i in o_set:
    print(i, end=" ")

# enumeeate
for i, v in enumerate(o_set):
    print(f"indice {i} com valor {v}")

# # erro ao tentar acessa por índice
#     print(o_set[0])
#           ~~~~~^^^
# TypeError: 'set' object is not subscriptable
convert_list = list(o_set)
print(convert_list[4])

# métodos da classe set

conj1 = {1,2}
conj2 = {2,3,4}

# união
a = conj1.union(conj2)
print(f"União, junção .union {a}")

#intersection
b = conj1.intersection(conj2)
print(f"Apenas iguais, intersecção {b}")

# diferença
c = conj2.difference(conj1)
print(f"Apenas valores diferentes {c}")

#symmetric differencee
c_c = conj1.symmetric_difference(conj2)
print(f"Pega todas os diferentes {c_c}")

#subconjunto
d = conj2.issubset(conj1)
print(f"Está contido {b}")

#não se conectam
conj3 = {9,7}

e = conj2.isdisjoint(conj3)
print(f"Não tem ligação {e}")

#add
# SÓ ADD SE ESTE VALOR NÃO EXISTIR
conj3.add(2)
print(conj3)

#clear limpa tudo
conj3.clear()
print(conj3)
# retorno set()

#copy - gera uma cópia
conj1.copy()

# discard
# SE NÃO TEM O VALOR EXISTENTE ELE NÃO DÁ ERRO, FAZ NADA

conj4 = {5,9,7,3,6,4}

conj4.discard(9)
print(conj4)

# pop - vai tirando valor da lista da esquerda ára direita

print(conj4.pop())
# retorno 3
print(conj4)
# {4, 5, 6, 7}
print(conj4.pop())
# retorno 4
print(conj4)
# { 5, 6, 7}

# remove
# coloca o valor a ser removido
conj4.remove(6)
print(conj4)

# Se não tiver o valor dá erro
# conj4.remove(0)
#     ~~~~~~~~~~~~^^^
# KeyError: 0

# len - mostra tamanho
print(len(conj4))

# VERIFICAR SE TEM UM VALOR  - in
print(1 in conj4)
# retorno false

print(5 in conj4)
# retorno true
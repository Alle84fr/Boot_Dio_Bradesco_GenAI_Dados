<h1>Listas</h1>

https://github.com/digitalinnovationone/trilha-python-dio

branch 01

<h3>Lista - list</h3>

- sequência ordenada por indices
- qualquer tipo de objeto
- mutável

<b>criando lista</b>

lista_vazia = []
retorno - []

lista_contrutor_chars = list("python")
retorno - ['p', 'y', 't', 'h', 'o', 'n']

lista_funcao_range = list(range(10))
retorno - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = ["AA", 123, 15.5, "cavalo", True]
retorno - ['AA', 123, 15.5, 'cavalo', True]

<b>acesso direto</b>

lista_contrutor_chars[0]
return p

lista_contrutor_chars[4]
return o

lista_funcao_range[-1]
return 9

lista_funcao_range[-6]
return 4

<b>lista aninhada</b>

Estrutura, matrix bidimencinal - lista, tuplas, dict dentro de lista, tupla e dicionário

matrix_bid = [
&nbsp;&nbsp;&nbsp;&nbsp;["lista1", 12, "p"],
&nbsp;&nbsp;&nbsp;&nbsp;["lista2", 13, 8.4],
&nbsp;&nbsp;&nbsp;&nbsp;["lista3", 15, False]
]

print(matrix_bid[0])
return: ['lista1', 12, 'p']

print(matrix_bid[1][1])
return: 13

print(matrix_bid[2][-1])
return: False

<b>Fatiamento</b>

extrair conjunto de valores de uma sequência
(índice_inicial:índice_final:pulo)

fatia = list("fatiamento")

print(fatia[2:])
return:['t', 'i', 'a', 'm', 'e', 'n', 't', 'o']
inicia no índice 2

print(fatia[:2])
return:['f', 'a']
inicia no 0 e termina no 2

print(fatia[2:5])
return:['t', 'i', 'a']
inicia no 2 e termina no 5 (pegando o 4 e ignorando 5)

print(fatia[0:6:2])
return: ['f', 't', 'a']
inicia no zero, pula 1, pega o próximo, e assim vai

print(fatia[::])
return:['f', 'a', 't', 'i', 'a', 'm', 'e', 'n', 't', 'o']
pega todos na ordem normal

print(fatia[::-1])
return:['o', 't', 'n', 'e', 'm', 'a', 'i', 't', 'a', 'f']
pega todos de trás para frente

<b>Enumerate</b>

qual índice dentro de um for

for i, f in enumerate(fatia):
    print(f"índice :{i} valor: {f}")

<b>Compreensão de lista</b>

Oferece uma sintaxe mais curta
cria nova lista com base nos valores de uma lista existente
cria nova lista aplicando alguma modificação nos elementos

num = [1,9,8,12,69,7,0]
pares = []

for i in num:
&nbsp;&nbsp;&nbsp;&nbsp;if i%2 == 0:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pares.append(i)

print(f"par {pares}")
return: par [8, 12, 0]

<span style="color: red;">.append()</span> adiciona à lista

outra forma

pares = [n for n in num if n%2 ==0]
1° n = é o retorno
2° interação - toda parte do for
(1 e 2 são obrigatórios)
3° filtro if

outro exemplo
quadrado = [n **2 for n in num]
return: [1, 81, 64, 144, 4761, 49, 0]

<b>métodos</b>

- <span style="color: red;">.append()</span> adiciona 
ex: num.append(58)

- <span style="color: red;">.clear()</span> limpar a lista - esvazia
ex: num.clear()

- <span style="color: red;">.copy()</span> copia uma lista igual, mas em outra instãncia, então não está vinculada a mundanças da lista original
ex: num.copy()

- <span style="color: red;">.count()</span> quantas vezes um objeto aparece
ex: num.count("A")

- <span style="color: red;">.extend()</span> se tem uma lista e quer add novos elementos de outra lista
Não elimina valores duplicados
ex: num.extend(["java","c#"])

- <span style="color: red;">.index()</span>
qual primeira ocorrência de um obj 
ex: num.index("A")

- <span style="color: red;">.pop()</span>
lista é pilha, adiconado acaba indo para o "fim" da lista (topo da pilha)
tira último elemento add ou pode tirar pegando índice
ex: num.pop( )
ex: num.pop(2)

- <span style="color: red;">.reverse()</span>
espelhar lista
ex: num.reverse( )

- <span style="color: red;">.sort()</span>
ordena as listas
ex: num..sort()
ex: num..sort(reverse=True) - inverte a lista
ex: num..sort(key=lamda x: len(x)) - ordenar por tamanho da palavra
lambda é uma função anônima = não tem nome
x é argumento da lista 
ex: num.sort(key=lamda x: len(x), reverse=True) - aqui inverte

- <span style="color: red;">.len()</span>
tira tamanho, quantidade de elemntos
ex: num.remove("p")

- <span style="color: red;">.sorted()</span>
ordena lista
ex: num.sorted()



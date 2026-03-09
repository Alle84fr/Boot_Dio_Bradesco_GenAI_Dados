# tuplas

# tuplas/ TUPLE são estruturas de dados IMUTÁVEL
# armazena qualter tipo de objeto
# pode criar estrutura bidimencional (tabeas)
# acessa por índice

# tuplas são imutáveis, os objetos podem ser mutáveis

frutas = ("laranja", "pêssego", "abacate",)

# se por tuple na frente, cada letra é um obje
letras = tuple("python",)

# sem tuple na frente há apenas um objeto
pais = ("termina com virgula",)

nume = (1,2,1.3,2.5,)

#para evita que o python saiba que é tuplas, POR VIRGULA NO FINAL

# acessa como se fosse lista

print(nume[2])
print(letras[3])
print(frutas[-3])
print(pais[0], "\n")

matriz = (
    ("tupla0,",1,),
    ("tupla1,",2,),
    ("tupla2,",3,)
)

print(matriz[0])
print(matriz[1][1])
print(matriz[2][-2],"\n")

#fatiamento - passa índice e ou final ou posição a pular

tupla = tuple("0123456789",)

print(f"tupla[2:] inicia no 2 {tupla[2:]} ")
print(f"tupla[:2] vai até o 2° valor {tupla[:2]} ")
print(f"tupla[1:5] inicia no 1 e termina no 5 {tupla[1:5]} ")
print(f"tupla[1:6:2] inicia no 1 e termina no 6 e pula duas casas {tupla[1:6:2]} ")
print(f"tupla[::] pega tudo {tupla[::]} ")
print(f"tupla[::-1] pega tudo ao contrário{tupla[::-1]} \n")

percorree = ("a", "A", "b", "B", "c", "C")

for i in percorree:
    print(f"Aletra é {i}")

# enumerete
for indice, valor in enumerate(percorree):
    print(f"o índice é {indice} = {valor}")

#ver erro ao tentar interar
erro = (1,2,3,0,2,4,2,8,)
#  erro[0] = 0
# TypeError: 'tuple' object does not support item assignment

# classe tuple - não tem add e update

#count

print("\n",erro.count(2))
print(erro.count(9))
#index
print(erro.index(8))
# tamanho
print(len(erro))
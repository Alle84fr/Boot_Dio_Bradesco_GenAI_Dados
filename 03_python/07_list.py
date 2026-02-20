lista_vazia = []

lista_contrutor_chars = list("python")

lista_funcao_range = list(range(10))

lista = ["AA", 123, 15.5, "cavalo", True]

print(lista_vazia)
print(lista_contrutor_chars)
print(lista_funcao_range)
print(lista)

#____________________

print(lista_contrutor_chars[0])
print(lista_contrutor_chars[4])
print(lista_funcao_range[-1])
print(lista_funcao_range[-6])

#____________________

matrix_bid = [
    ["lista1", 12, "p"],
    ["lista2", 13, 8.4],
    ["lista3", 15, False]
]

print(matrix_bid[0])
print(matrix_bid[1][1])
print(matrix_bid[2][-1])

#____________________

fatia = list("fatiamento")

print(fatia[2:])
print(fatia[:2])
print(fatia[2:5])
print(fatia[0:6:2])
print(fatia[::])
print(fatia[::-1])

for i in fatia:
    print(f"Fatiando {i}")

#____________________

for i, f in enumerate(fatia):
    print(f"índice :{i} valor: {f}")
    
#____________________

num = [1,9,8,12,69,7,0]
pares = []

for i in num:
    if i%2 == 0:
        pares.append(i)

print(f"par {pares}")

quadrado = [n **2 for n in num]

print(quadrado)

#____________________

original = [1,6,89,"qs","up"]

outra_igual = original.copy()

print(original)
print(outra_igual)

original = [1,6,89,"q","u","u", 5, 9, "U"]

print(original)
print(outra_igual)

contar = original.count("u")

print(contar)

#____________________

lingua = ["python", "java", "CSS"]
outros = ["HTML", "SQL", "java"]
lingua.extend(outros)

print(lingua)

#____________________

print(lingua.index("java"))

#print(lingua.index("Java")) 
#return ValueError: 'Java' is not in list
# porque é case sensível

#____________________

tira= [2,4,6,9,10,12,14,16,17]

print(f"tirei o último que é {tira.pop()}")
print(f"tirei o 4° n° que é {tira.pop(3)}")
print(tira)

#____________________

tira.remove(12)
print(tira)

#____________________

tira.reverse()
print(tira)

#____________________

ordena = ["chave", "key", "galo","noventa","seis","chupeta"]

ordena.sort()

print(ordena)

ordena.sort(key=lambda x: len(x))

print(ordena)
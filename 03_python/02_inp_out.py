nome = input("nome: ")
print(nome)

idade = int(input("idade: "))
print(idade)

print(f"Originalmente o final de um print possui um \ n, o equivalente ou println do kotlin/java")
print("""Se quiser não pular linha entre print, no final deve por , end=' ', que separará por espaço vazio
Se quiser um - entre print pode por end='-'
\ n no início ou no meio ou fim indicala pular linha (linha em branco)sep = sepra geralmente com espaço em branco, mas se por # ele separa por eles
Pode usar separado e end no final juntos""")

a = 1
b = 1 + 1
c = 1 + 2
d = 1 + 3
e = 1 + 9

print(f"\n{a}", end="-")
print(f"{b}", end="-")
print(f"{c}", end="-")
print(f"{d}", end="-")
print(f"{e}\n")

print(a, b, c, d, e, sep=" # ")


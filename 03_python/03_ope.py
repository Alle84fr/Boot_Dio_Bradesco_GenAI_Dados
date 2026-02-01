prod_1 = 40
prod_2 = 20

print("\nOperador aritmédico")
print(f"soma {prod_1 + prod_2}")
print(f"subtração {prod_1 - prod_2}")
print(f"multiplicação {prod_1 * prod_2}")
print(f"divisão {prod_1 / prod_2}")
print(f"divisão inteiro {prod_1 // prod_2}")
print(f"resto da divisão {prod_1 % prod_2}")
print(f"elevado {prod_1 * prod_2}")
print(f"ordem {prod_1 * prod_2-(prod_2 + prod_2)/5**2}\n")

#------------------

a = 1
b = 1.0
c = 12

print("\nOperador comparação - bool")
print(f" igual {a == b}")
print(f" diferente {a != b}")
print(f" maior igual {c >= a}")
print(f" menor igual {c <= a}")
print(f" maior {c > a}")
print(f" menor {c < a}")

#------------------

print("\nOperador atribuição")
print(f" atribuição simples = (recebe) a recebe = 10")
print(f" atribuição com soma += (igual saldo que soma algo)")
print(f" pode fazer com todos os operadores de comparação")

saldo = 510

if saldo <100: saldo += 100
elif saldo == 500: saldo /= 5
else: saldo **= 3

# saldo é maior que 100 então if é falso, pula
# saldo é diferente de 500, false, pula
# saldo é maior que 500
# 510 * 510 * 510 = 132651000
print(saldo)

#------------------

print("\nOperador lógico")

print("and / e, só é verdade de todos forem verdade")
print("or / ou, é verdade alguns deles forem verdade,se todos falsos, falso")
print("not / negação, nega o valor")

q1 = (1 < (10+2)) and (12 == 12)
q2 = (1 > (10+2)) and (12 == 12)
q3 = (1 > (10+2)) or (12 == 12)
q4 = (1 > (10+2)) or (12 != 12)
q5 = ((1 > (10+2)) or (12 != 12)) and (1 <= 1)

print("v e v")
print(q1)
print("f e v")
print(q2)
print("f ou v")
print(q3)
print("f ou f")
print(q4)
print("(f ou f)e(v)")
print("f e v")
print(q5)

#------------------

print("\nOperador identidade")

print("Se os objetos ocupam a mesma posição na mamória, tem a mesma 'etiqueta', se vem da mesma 'caixa'")
print("Não vê se são mesmo tipo, vê se  estão na mesma memória")

curso = "Py"
linguagem = curso
ide = "VSCode"
curto = "py"

print("\is, é")
print(f"Curso está no mesmo espaço de memória que linguagem - {curso is linguagem } ")
print("\is not, não é")
print(f"Curso não está no mesmo espaço de memória que linguagem - {curso is linguagem } ")
print("\is, é")
print(f"Curso está no mesmo espaço de memória que ide - {curso is ide } ")
print("\is, é")
print(f"Curso está no mesmo espaço de memória que curto - {curso is curto } ")

#------------------

print("\nOperador associação")

print("Se um valor está presente em uma sequência")

seq1 = "Abracadabra"
seq2 = ["cavalo", "anta", "burro"]
seq3 = ("tupla", 10, 25.3)

print("in = está presente")
print("not in = não está presente")

print(f"b está na string {seq1} - {"b" in seq1}")
print(f"y está na string {seq1} - {"y" in seq1}")
print(f"C está na string {seq1} - {"C" in seq1}")
print(f"cavalo não está na lista {seq2} - {"cavalo" not in seq2}")
print(f"25 não está na tupla {seq3} - {25 not in seq3}")


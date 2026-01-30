# algoritmo = receita, sequencia de passos para chegar a um objetivo

# extensão do python é .py

print("Salum Mondo!")
print("_"*10)
print(dir())
print("_"*10)
print(dir(100))
print("_"*10)
print(help())


nome, sobrenome = "Adalbetunes", "Solva"

idade_max = 18

VALOR_PI = 3,141592653589793

print(f"{nome} com sobrenome {sobrenome} idade {idade_max} com pi de {VALOR_PI}")

# mudando valor da variável
nome = "Gurumira"

idade_max = 87

print(f"{nome} com sobrenome {sobrenome} idade {idade_max} com pi de {VALOR_PI}")

# conversão de tipos

inteiro = 1
flote = 1.5
strinng = "1"

print("\n", type(inteiro))
# <class 'int'>
print("\n", type(flote))
#  <class 'float'>
print("\n", type(strinng))
#  <class 'str'>

# inteiro para decimal

int_to_float = float(inteiro)
divisao_to_float = 1/2

print("\n", type(int_to_float))
# <class 'float'>
print("\n", type(divisao_to_float))
# <class 'float'>

float_to_int = int(flote)

print("\n", type(float_to_int))
# <class 'int'>

string_to_int = int(strinng)

print("\n", type(string_to_int))
# <class 'int'>

int_to_string = str(inteiro)

print("\n", type(int_to_string))
#  <class 'str'>
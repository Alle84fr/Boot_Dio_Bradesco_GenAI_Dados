<h1>Python</h1>

prof: 
linkedin = @guicarvalho 
github = Github
repsitório - guicarvalho/trilha-python-di

<h2>Origem</h2>

ano desenvolvimento: 1989
ano do lançamento; 1991
1° versão pública: 0.9.0

programador: Guido Van Rossun
objetivo: continuidade na linguagem ABC(da CWI)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fácil e intuitiva
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cód abertor (todos podem contribuir)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;adequada parav tarefas diárias e produtivas
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inteligível

Em 1995 lança versão 1.2. O vínculo com centro de pesquisa Van Rossum acaba e a equipe vai para BenOpen.com

Em 2000 nasce a versão List Comprehensions - melhoria no coletor de lixo

Em 2001 nasce a PSF (Python Software Foundation) que a partir do 2.1 possui todo o código, documentação e especificações da linguagem

Em 2008 lança 3.0 que nelhorou problemas de linguagem e a performance

<h2>Características</h2>

- tipagem DINÂMICA E FORTE
- multiplataforma
- multiparadigma
- grande comunidade

<h2>Ambiente usado</h2>

<b>linguagem de programação</b> = Python

verificar se tem python no terminal

<span style="color: green;">python -V
python3 -v</span>

Neste momento minha versão é Python 3.13.3

<b>ide</b> = Visual Studio Code

Meu Version: 1.108.2 (user setup) e Node.js: 22.21.1

<b>extensões</b>

- autoDocstring: VSCode Python Docstring Generator
- python
- Visual Studio IntelliCode (não dá mais para instalar)

<h2>Tipos</h2>

Define caracteristicas, comportamento e valores de um objeto

tipos padrão

| tipos built-in | oque são | ex |
| --- | ---| --- |
|string - str | texto | "Char", 'String' | 
| integer - int | numéricos inteiro | 1, 1.569 |
| float - float | numéricos decimal | 1.0, 1.569.01 |
| complex - complex() | numéricos complexo | 5j |
| list - [] | sequência | lista = ["A", 1] |
| tuple - () | sequência | tuple = ("imutável", "varios tipos")
| range - range() | sequência | for i in range(5):|
| dict - {} | mapa | dico = {"chave_1": 123, "chave_2": 234}
| set - {} | coleção | sem ordem, muável, sem valores repetidos - sete = {1,2,3} * |
| set - frozenset() | coleção | imutável - fs = frozenset([1,2,3])
| booleano - bool | Verdade ou Falso | True False
| byte | binário | 0 255 |
| bytearray | binário | | 
| memoryview| binário | |

<h2>Tipo interativo</h2>

Executa e vê na hora o resultado

Inicinado

Executar no terminal

para abrir terminal ctrl j

para limpar terminal ctrl L ou cls

<span style="color: green;">python + enter</span>
Codificar no próprio terminal, ao apertar enter o resultado aparecerá sem a necessida de print
para sair <span style="color: green;">exit()</span>
para textes rápido, ex; ver como está funcinado a classe, função etc

<span style="color: green;">python -i nome_file.extensão</span>
ex: python -i .\03_python\01_prog.py  
roda o file em questão
para sair <span style="color: green;">exit()</span>

função <span style="color: green;">dir()</span> 
- não possui argumentos - retorna lista do bloco - dir()
retorno de print(dir())
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
&nbsp;
- possui argumentos - retorna lista de astributos válidos - dir(100)
retorno de print(dir(100))
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__'....

função <span style="color: green;">help()</span> 

Quais argumentos recebe, parâmentros, módulos, funções, classes, métodos, vriáveis ...

aparecerá uma mensagem Welcome....
help> aqui o que quer saber e aperta enter

para sair <span style="color: green;">q</span> 

<h2>Variáveis e Constante</h2>

Variável = conteiner que armazena um valor, seja string, lista ou classe

É uma unidade de memória que guarda um valor, e é volátil

O <b>INTERPRETADOR</b> do python, ao rodar, analisa o dado, na hora, e refencia o tipo referente

É MUTÁVEL

Constante = variável IMUTÁVEL, ex o valor de pi, nunca mudará durante a ezxecução

Em java usa-se a palavra reservada <i>final</i> -> final int idade = 18;

Em python não temos este métodos fortemente tipado,então uma forma de diferenciar é colocar o nome da variável toda em caixa alta

ex:

idade = 1 - mutável, pode mudar dirante o decorrer do cód
IDADE = 1  - convenção diz para que não mudar, pode ser mudada, mas não deve mudar

variável - snake case - idade_mairidade

nome deve dizer o que o dado se refere

iniciar com minuscula

não iniciar com n°s

não usar caracteres especiais

obs - camel case não é muito usado em .py, é mais java e js nomeVariável

<h2>Conversão de tipos</h2>

<b>concatenização</b>, junção de strings, n°s, listas ....

ex:
a = "Ana"
b = "Rosas"

print (a + b)

sai Ana Rosa

outra forma de concatenar é usar a f-string

f"nome {a} {b}"

<i> exemplos direto no file 03/python/01_prog.py</i>

<b>erros de conversão</b>

ValueError : could not convert string to float

ex:
valor = "um"
converte = float(valor)

<h2>Função entrada e saída</h2>

Input - entrada, receber

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originalmente é do tipo str, deve-se converter para outro tipo se desejar

output - saída, exibir

<i> exemplos direto no file 03/python/02_inp_out.py</i>




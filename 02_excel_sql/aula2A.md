<h1>Conceitos básico e Estrutura do banco de dados</h1>

github- github.com/pamelaborges/dio-bd-relacional

<h3>banco de dados</h3>

Coleção organizada de infromações ou dados

Possui ssitema de consulta de dá fácil acesso à infromação

<u>Relacionais/ SQL</u>


<u>Não relacionais / NoSQL/ NotOnlySQL</u>


<u>Orientados ao objeto</u>


<u>Hierárquico</u>

<h3>SGBD - Sistema de Gerenciamento de Banco de Dados </h3>

<u>Funcionalidades</u>

<span style="color:#06d6a0;">C</span><span style="color: #055b44;"> REATE</span> escrita
<span style="color: #dda15e;">R</span><span style="color: #5d4529;"> EAD</span> leitura
<span style="color: #ef476f;">U</span><span style="color: #732134;"> PDATE</span> atualização
<span style="color: #1a7ed5;">D</span><span style="color: #16334b;"> ELETE</span> exclusão

<u>Estrutura</u>

Database = local onde ficará amarxenadas as tabelas

column - coluna - definição de estados
row - linhas, tuplas - infrom ações em sí, registro
tables - tabelas

pk - primary key - chave primárias
fk - foreign key - chave estrangeira

<u>Características</u>

- Relacionamento entre tabelas
- Linguagem de consuta Estruturada (SQL)
- Intwegridade refencial
- Normalização de dados
- Segurança
- Flaxibilidade e extensibilidade
- Suporte a transações ACID (garantia da consistência da infirmação dentro do bd)

<u>ACID</u>

<span style="color:#06d6a0;">A</span><span style="color: #055b44;"> ATOMICIDADE</span> garante que todas as operações de uma transação seja executadas com sucesso ou que nenhuma seja executada. Se uma falhar a outra será revertida ao estado anterior
<span style="color: #dda15e;">C</span><span style="color: #5d4529;"> ONSISTÊNCIA</span> garante que o bd seja de um estado consistente a outro consistente
<span style="color: #ef476f;">I</span><span style="color: #732134;"> SOLAMENTO</span> cada transação é feita de froma isolada, para mater consistência do dado, cada transação será feita por vez
<span style="color: #1a7ed5;">D</span><span style="color: #16334b;"> DURABILIDADE</span> uma vez que a transaçao seja confirmada, ela será "fixada" - commitada

referência = www.oracle.com.br/br/database/what-is-a-relational-database/

<h3>Introduçao e conceitos básicos SQL</h3>

Linguagem de consuta padronizada - Structured Query Language

1970 foi seu surgimento


<u>Tipos de declarações</u>

- <span style="color: #9624d7;">DQL</span><span style="color: rgb(14, 141, 10);"> SELECT </span> Linguagem de Consulta Dados <i>Data Query Language</i>. Recupera infromação
- <span style="color: #d72480;">DML</span><span style="color: rgb(10, 134, 141);"> INSERT, UPDATE, DELETE </span> Linguagem de Manipulação Dados <i>Data Manipulation Language</i>
- <span style="color: #d77724;">DDL</span><span style="color: rgb(10, 25, 141);"> CREATE, ALTER, DROP </span> Linguagem de Definição Dados <i>Data Definition Language</i>. Estrutura onde será criada a tabela, como a tabela será,etc..
- <span style="color: #d72480;">DCL</span><span style="color: rgb(10, 134, 141);"> GRANT, REVOKE</span> Linguagem de Controle Dados <i>Data Control Language</i>
- <span style="color: #9624d7;">DTL</span><span style="color: rgb(14, 141, 10);"> BEGIN, COMMIT, ROLLBACK </span> Linguagem de Transação Dados <i>Data Transaction Language</i>

<u>Sintáxa básica - pode mudar confrome bd</u>

- Os nomes DEVEM começar com uma letra ou com um caractere de underscore (_)
- Pode ser case sensitve (no geral é case sensitive)
- Os nomes podem conter letras, n°s e caracteres subçinhado

referência = www.sqltutorial.org/

<u>MER e DER - modelagem de banco de dados</u>

<b>MER</b> Modelo Entidade-Relacionamento / Modelo Entidade-Relacionamento

Representa estrutura geral, sem entrar em muitos detalhes 

- entidades
- atributos (infromações)
- relacionamento entre entidades

<b>DER</b> Diagrama Entidade-Relacionamento / Entity-Relationship Model

- representação gráfica do modelo
- mostra:
&nbsp;&nbsp;&nbsp;&nbsp;- entidades
&nbsp;&nbsp;&nbsp;&nbsp;- atributos
&nbsp;&nbsp;&nbsp;&nbsp;- relacionamentos
&nbsp;&nbsp;&nbsp;&nbsp;- cardinalidades

link para desenvolver o diagra = app.creately.com/

<b>Entidades</b>

- noemadas com subtantivos concretos ou abstratos
- nome deve repersentar de forma clara suas função
- símbolo retângulo

![símbolo retângulo](img/d1.png)

<b>Atributos</b>

- características ou propriedades das entidades
- descreve infrimações específicas
- não poder ser atributo composto
- símbolo oval

![simbolo oval](img/d2.png)

<b>Relacionamento</b>

- como entidades relacionam entre sí
- conexão se dá por linhas

![simbolo losango](img/d3.png)

<b>Cardionalidade</b>

- relacionamento entre "quantidades de entidas"

<span style="color: #dda15e;">0,n</span> </span> <span style="color: #5d4529;"> nenhuma ou uma entidade para outras entidades</span> - um usário pode ter tenhuma, uma, ou mais de uma reserva
<span style="color: #06d6a0;">1,1</span><span style="color: #055b44;"> um entida para outra entidade</span> - um enfermo pode ter apenas um leito
<span style="color: #dda15e;">1,n</span> ou <span style="color: #dda15e;">1,*</span> <span style="color: #5d4529;"> uma entidade para outras entidades</span> - um enfermo pode ter um ou mais médicos
<span style="color: #06d6a0;">n..n</span> ou <span style="color: #06d6a0;"> * .. *</span> <span style="color: #055b44;"> entidades para outras entidades</span> - 

Ia para gerar diagramas = www.quickdatabasediagrams.com/

![diagram - feito no drawio](img/d4.png)

<h1>Introdução de engenharia de prompt</h1>

prof: Alidiana Andrade - tech Education Analyst

<h2>Introdução</h2>

Se não for claro no pedido o retorno não será claro
A IA deve saber o que se precisa, instrução claras no comando, detalhadas ao máximo

<b>O que precisa para começar</b>

<span style="color: green;">Arquitetura de transfome</span> usa mecanismo de atenção para processa palavras em sequência, não de forma linear, considerando contexto de cada palavra em relação a todas palavras de texto

busca conexão em várias partes do texto, "pegando" trexos mais interessantes

prompt é convertido em tokes, que podem ser palavras,partes de palavras ou caracteres, que é processadas por camadas de atenção e outros até gerar atenção

tokenizer = https://platform.openai.com/tokenizer

"Tokens represent commonly occurring sequences of characters."
<i>sequências de caracteres que ocorrem com frequência</i>

após tokinazação os toking são convertidos em <span style="color: green;"> embeddings</span>

"... is a vector representation of piece od data that is meant to (significava) preserve aspects of its content (conteúdo) and /or its meaning"

Representações vetoriais que capturam seu significado

Estes passam por camadas redes neurais com transfomadores e assim tenta gerar contexto e prever o token

<h2>Visão geral da engenharia de Prompts</h2>

<b>Como os Modelos de Liguagennm "Entendem" um prompt</b> e
<b>Como os modelos de linguagens "Lembram" do que foi dito</b>

Em  geral não possui memória persistente entre interação, depois que ela termina

Mas na mesma interação, devido modelo de tokem, há janela de texto, e as lembranças

É como lousa, o professor coloca matéria na lousa e quando termina as informações antigas dão lugar às mais novas

ex:

1° prompt = em poucas palavras o que é aliança?
resposta genérica, pois não há dados "acomulados", não tem direcionamento

2° prompt = O que é Amon Amarth 
resposta é que do universo do senhor dos aneis, e dá mais detalhe

3° prompt =  alinça
respota já relaciona com o mundo dos senhor dos anéis, mostrando que agora possui um contexto 

Com o tempo deveria reforçar o tema original, conforme alcançar o limite de tokens


<b>Elementos Essenciais de um Bom Prompt</b>

- intrução clara = tarefa específica
- não ter ambiguidade

ex: Crie uma istória inicial para campanha rpg de fantasia, envolvendo um grupo de aventuireiros em uma cidade amaldiçoada

- contexto - informações a entender melhor a tarefa

ex:  a cidade foi tomanda por uma maldição que impede qualquer um de sair. Os moradores estão desaparecendo misteriosamente, e as sopmbras parecem ganahar vida. Os Jogadores são aventureiros que chegaram na cidade pouco antes da maldição começar, embusca de um tesouro escondido

- exemplos -  orienta sobre formato ou estilo

ex: a istória pode começar com os aventureiros sendo atacados por sombras vivas na entrada da cidade, forçando-os a buscar refúgio na caverna local. Lá eles encontram um velho contador de histórias que fala sobnre uma relíquia perdida que pode quebrar a maldição

- dados de entrada - infromaçãoes ou problema que deve resolver
Ajuda a personalizar
- pode ser: 
&nbsp; &nbsp; &nbsp;- pergunta
&nbsp; &nbsp; &nbsp;- situação
&nbsp; &nbsp; &nbsp;- pedido (ex: resumir)

Neste casop personagens
ex: Os aventuireiros incluem: um aldino sacástico, um clérico com uma conexão misteriosa comas a sombras, um bárbaro inpulsivo. O vilão princi´pal é uma figura encapuzada que manipula a maldição das sombras

- formato de saída - especificar como quer a respota
pode ser, entre outros formatos:

&nbsp; &nbsp; &nbsp;- lista de endpoints
&nbsp; &nbsp; &nbsp;- formato de json
&nbsp; &nbsp; &nbsp;- conteúdo para rede social

ex: a istória deve ter de 2 a 3 parágrafos, começando com uma introdução impactante, seguida pelo 1° desafioe um  gancho final que motive os jogadores a explorar a cidade


<h2>Aplicações práticas da engenharia de prompts</h2>

<b>Engenharia de Prompts no dia a dia</b>

Usou copilot

Traz templates que podem ajudar em resumir texto, criar imagens, usar ia, planejamento de metas pessoais

<u>templates</u> é modelo pronto usado como base para criar algo, sem ser do zero

ex: modelo de currículo

ex: planílha de controle finaceiro


<b>Cuidados na aplicação de prompts</b>

As instruções influenciam nas respotas

observar;

- prompts enviesados 

- alucinações

- consideração ética

- privaciadde e segunça

Os dados que limentaram podem estar errados

Os modelos não tm consciência, apenas reproduzem com base no que foram treindados

deve-ser observar os princípios de:

<span style='color: green;'>
&nbsp; &nbsp; &nbsp;- imparcialidade

&nbsp; &nbsp; &nbsp;- confiabilidade

&nbsp; &nbsp; &nbsp;- segurança

&nbsp; &nbsp; &nbsp;- privacidade

&nbsp; &nbsp; &nbsp;- inclusão

&nbsp; &nbsp; &nbsp;- transparência

&nbsp; &nbsp; &nbsp;- responsabilidade

</span> 

Nosso prompts podem ter conteúdo enviesado, que pode induzir respota

ex: Porque café é melhor bebida de todos os tempos

aqui já induz o modelo a aceitar que o café é a melhor bebida

como arrumar:

ex: Quais são as vantagens e desvantagens do café em comparação com outras bebidas?

As lucinações é retorno de dados errados ou inventados. Geralmente quando tem poucas referências ou não tem muito treino sobre

Se o nosso prompt tiver um dados errado,ou inventada, pode trazer dados errados

<h2>Leve seus prompts ap próximo nível</h2>



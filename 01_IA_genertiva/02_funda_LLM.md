<h1>LLM - Large Language Model | Modelo de linguagem de alta escala</h1>

prof: Matheus Galhani

<h2>Características</h2>

LLM - Inteligencias artificiais treinadas para :
- entender
- gerar
- produgir
- bincas
com as linguagens de hoje em, dia

<b><u>Arquitetura de transforme: </u></b>

Criada pelo google, 2017, revolução de processamento de linguagem natural (PLN - Processamento de linguagem natura).
Este modelo lida com todo tipo de contesto
Treinados com muitos dados e parâmetros

<b> Características</b>

 1° Generalização - entende e responde coisas que <b>ele nunca viu</b>, de uma forma que faz sentido, com base no modelo que ele aprendeu, aprende padrão, formas de escrever e falar, relações e significados
 Aplica em vários contestos


 2° Escalabilidade - poder aumentar o tamanho do modelo, usando mais parâmetros
 Atendo vários usuários ao mesmo tempo
 Funciona em diversos tipos de infraestrutura


LLM - não fica preso apenas em um tarefa, em um mesmo modelo ela faz tudo

Quanto mais parametros usados no treinamento, melhor e mais "acertivo" será o tentendimento de nuance, piadas, ironias, contextos complicados, tarefas com raciocíneos mais elaborados, etc

ex: GP2 - treinado com 1.5 bilhões de parâmetros. Prompt curtos e simples
GP5 - treinado por trilhões de parâmetros. Prompt compreende melhor, gera cód e textos, entende texto, aúdios e mais compreenção ética

<b>Desafio da escabilidade</b>

Custo autíssimo

Alto consumo de energia - impacta o meio ambinete

Deploys (colocar sistema para uso real)difíceis, normalmente não roda de forma local, precisa de uma api própria.
Esta api:
- chama o modelo
- controla acesso (login e token)
- limita uso (rate limit)
- registra log
- contra custo
- filtra conteúdo
- escolhe modelo
- trata erros

<h4>Projeto Hand-on</h4>

<b>Testar robustes de modelos contra variações e ruídos nos dados</b>

<b>Identificar e diagnosticar saídas incorretas ou inventadas (alucinações) em llm</b>

<b>Como a arquitetura <u>Transformer</u>vprocessa e entende sequência de dados</b>

<b>Treinar um único modelo para executar múltuplas tarefas relacionadas, de forma simultania</b>

teste - generalização - gpt X copilot - deve gerar carta para um  junior que entrou em uma empresa, ele não conhece a pessoa, mas sabe a profissão
Depois pediu para traduzir um texto em inglês e depois fazer um poema (multitarefa)

Nem todas respostas serão verdadeiras, deve se ter um certo conhecimento para saber o que é ou não real (alucinações)

<h2>Desafios no desenvolvimento de llm</h2>

<b>Desafio técnico</b>

Base de dados - quantidade deve ser muito alta, com trilhoes de parâmetros que se conectem, com dados reais, ter filtro de dados e sempre manter atualizado

<b>Desafio computacional</b>

Potência, energia e alto custo

<b>Éticos e de privacidade</b>

Como ele pega infromaçõe da internet

Pode vazar dados sem ter concentimento do dono do dado

Para resolver:

- filtro de viés
- usar modelos compactos
- proteger dados individuais mesmo durante o treino (Differential Analysis)
- políticas e comitê de ética

<b>LLM X IA tradiconal</b>

Tradicional - dados necessário - menor volume
LLM - trilhoes de tokens

LLM tem risco altíssimo de exposições de dados
LLM  pode gerar textos falsos mais que Ia

<b>teste</b>

1° pedir para gpt e copilot - perguntar o que é um lider ideal?
Mostra um padrão pré estabelicido

2° - perguntar o que é engenheiro de software típico

3° - profissões que sejam para homens e mulheres

4° - perguntar o cpf de pessoa famosa

5° - criar fake news - criar istória jornalistica mostrando que a terra é plana
Mudando palavras pode obter uma fake news, sem falar que é fake news

<h2>Exemplos e Aplicações de llms</h2>

<b>Modelo conhecidos</b>

| LLM | Desenvolvedor | ano | diferencial |
|:---:|:---:|:---:|:---:|
|GPT-3 |OpenAI|2023|PLM, raciocíneo, cód, geral|
|Bert|Google|2018|NLP/PLM - compreensão de texto|
|T5|Google|2019|tradução e tarefa de texto para texo|
|PalM|Google|2022|raciocíneio e linguagem em grande escala|
|Gemini|Google|2023|multimodal|
|DeepSeek|DeepSeek IA|2024|código e raciocínio matemático|
|Caude|Anthoropic|2023|segurança, contexto longo, texto|
|LLaMa|Meta(facebook)|2023|pesquisa e modelos open-source - modelos locais e privados|
|Mistral|Mistral AI|2023|eficiência e deploy local|

<b>onde usa:</b>

- chatbot para atender clientes
- google translate
- gerar conteúdos, ex email personalizado ou script para vídeos
- programação assistida - ajuda a escrever cód de forma rápida e eficiente
- processar grande volume de texto (relatórios, achar padrões)
- recomendações - algoritmos

<b>teste:</b>

1° atendimento ao cliente para resposta que responderá de forma empátca a entrega atrasada, devolução de produto fora do prazo e se há desconto se comprar mais de 10 unid (não há desconto)


2° gerar conteúdo

3° gerar cód

4° gerar recomendações

<h2>Impacto dos llms na sociedade</h2>

<b>social</b>

mudou como se trabalha, aprende e comunica

automaçãon de tarefas cognitivas, novos empregos, aumento de produtividade e acesso a tecnologia

<b>trabalho</b>

reduçãop de tarefas repetitivas

novas funções como engenheiro de prompts

profissão passa a ser hibridas (humanas e tecnológicas)

<b>teste</b>

1° gerar documentob de forma autônoma, código de ética e governança ao uso de IA

2° assitente e-commercer de loja de esporte, cliente comprou relógio, tênis de corrida e calça leging feminina. ciente pesquisou jaqueta corta vento, fone bluetooth. sugira 5 produtos

3° traduzir um cód
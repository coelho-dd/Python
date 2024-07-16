# !!! INTRODUÇÃO À VARIÁVEIS E INPUT !!!




# * Variáveis e seus nomes

# Um dos conceitos mais importantes no mundo da programação é o de variáveis.

# -> Uma variável é um local na memória que criamos, através do código fonte de um programa, para alocar algum valor. Isso é útil, já que com frequência precisamos manipular, editar e reutilizar de alguma forma, um mesmo valor com frequência. Portanto, quando temos o seguinte código:

x = 3.14

# estamos na verdade criando um espaço na memória do computador, que no caso se chamará 'x' e que carregará o valor 3.14. Uma variável é um espaço na memória sendo criado que carregará algum tipo de valor.

# Quanto ao nome de variáveis, existem algumas convenções entre programadores e regras específicas.

# Uma das convenções, no caso, é de utilizar variáveis descritivas ao problema. Por exemplo, a variável 'x' que criei acima não tem um nome inteligente para programas mais complexos. Claro, ele funciona como um exemplo ou em um programa muito simples como uma calculadora, mas se estivessemos montando um sistema grande para uma empresa, utilizar nomes de variáveis como 'x', 'y' e 'z', não seria algo interessante. Isso porque podemos definir variáveis com nomes descritivos que facilitam o entendimento do código. Por exemplo:

salario_medio = 1400

# Concordamos que uma variável de nome 'salario_medio' em um programa que lida com salários de uma empresa, por exemplo, ajudará mais no que diz respeito ao entendimento do código do que uma variável chamada 'x'. Essa convenção não é particular de Python, e é utilizada em todas as linguagens de programação.

# Uma outra convenção útil é a forma de se escrever o identificador(nome) de uma variável. Python segue a convenção snake_case. Ela diz que devemos escrever nomes de variáveis tudo em minúsculo, e se for um nome composto, devemos separar os espaços com um underline(_). Exemplo:

pagamento_janeiro = 1450
aniversario_fulano = 24
nome_programador = "Davi"
linguagem_favorita = "Python"
# ...

# Note que estamos substituindo os espaços por "_".

# Isso não é uma regra absoluta. As seguintes variáveis são válidas em Python:

pagamentoJaneiro = 1450
aniversarioFulano = 24
nomeProgramador = "Davi"
linguagemFavorita = "Python"

# As variáveis acima estão corretas na sintaxe Python. Porém, existe a convenção de que, em Python, utiliza-se o padrão snake_case. O padrão camelCase é utilizado em outras linguagens como JavaScript, Java, etc. Mas é claro, isso é apenas uma convenção e não uma regra... :)

# Agora, se tratando de regras, temos algumas bem definidas no que diz respeito à declaração de variáveis.

# Para facilitar a vida do interpretador, não podemos declarar variáveis com espaços em branco ou começando com números. Exemplos: 'pagamento janeiro', 'aniversario fulano', 'nome programador', 'linguagem favorita', '5x'. Todos esses identificadores estarão errados e farão com que seu programa apresente um erro. O motivo disso, como eu falei, é por causa do interpretador. Tanto com espaços em branco, quanto iniciando com números, dificulta a intepretação do código feita pelo interpretador, podendo ocorrer alguns problemas de interpretação(rs). 




# * Tipos de variáveis

# -> Um tipo de uma variávei define qual será o comportamento e os valores possíveis daquela mesma variável. Em Python, temos diversos tipos disponíveis que veremos a seguir.

# Tipos numéricos: Os tipos numéricos de Python são os valores com números inteiros ou decimais. Exemplo:

x = 1 # inteiro
y = 3.14 # decimal
z = 1.0 # decimal
w = 1000000000000 # inteiro
# ...

# Tipos lógicos: Os valores de tipos lógicos são uma representação de dois estados, verdadeiro ou falso. Então, na prática, um valor lógico será ou verdadeiro ou falso. Observe:

log1 = True
log2 = False

# Esses valores são úteis para fazer comparações entre valores, como 5 > 1(True), estabelecer uma espécie de controle sobre o programa(enquanto algo for verdadeiro, faça isso), etc...

# Tipo string: Os tipos string são representações de caracteres, palavras ou frases. Na prática, é lidar com letras e não apenas números. As strings são definidas dentro de duas aspas duplas ou simples. Exemplo:

nome = "Davi"
data = "24 de abril de 2001"
letra = 'a'
# ...

# Vale a pena mencionar que, como vemos na variável 'data' acima, mesmo números dentro das aspas são considerados e se comportam como caracteres! Isso é muito importante pelo seguinte motivo:

exemplo1 = 1
exemplo2 = "2"

# A variável 'exemplo1' tem o tipo numérico. Já a variável 'exemplo2' tem o tipo string e não numérico.

# (Uma análise mais detalhada de cada tipo de dado de Python será feita mais a frente...)




# * Entrada de dados(input)

# -> Um outro conceito importante na programação é a capacidade de fornecer dados à sua aplicação, e não apenas lidar com dados pré-programados. Isso permite que a aplicação interaja com o usuário de forma dinâmica. Um exemplo de entrada de dados é o preenchimento de um formulário na web.

# Em python, inicialmente, a forma com que fornecemos dados à aplicação é através do teclado digitando algo com a função input().
# Exemplo:

exemplo_input = input("Digite seu nome: ")
print(f"Olá, {exemplo_input}.")

# No código acima, a função input() pede que o usuário digite seu nome, e o código da função print() exibe uma mensagem personalizada para o usuário com o que ele mesmo digitou. Perceba que ele acabou de fornecer um dado para a aplicação, aonde a mesma utilizou desse dado para interagir com o usuário.

# É importante saber que, em python, um input através da função input() será sempre uma string. Portanto, se tentarmos realizar alguma operação matemática direta com o valor digitado pelo usuário, teremos um erro(já que operações matemáticas não são possíveis com strings).
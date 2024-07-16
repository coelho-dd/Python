# !!! Introdução à Linguagem Python !!!

# Python é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica.

# * Alto nível -> Na prática, uma linguagem de alto nível é uma linguagem que desconsidera alguns aspectos considerados "desnecessários" pela linguagem, normalmente acontencendo por trás dos panos automaticamente, diferente de linguagens mais baixo nível. Um exemplo disso é a administração dinâmica de memória, que em outras linguagens é feita pelo programador de forma manual, mas em Python é feita de forma automática.

# * Intepretada -> A interpretação de uma linguagem é um dos métodos para traduzir o código fonte para linguagem de máquina(binário). Esse processo utiliza um software chamado de 'interpretador', que lê o código fonte linha por linha e o executa ao mesmo tempo(o transformando em código de máquina e executando em seguida). Em contraste com esse método, existe o conceito de compilação, que é um outro software que lê todo o código fonte primeiro, o transforma em código de máquina em seguida, para só então executá-lo.

# * Tipagem dinâmica -> Uma das características mais marcantes de Python é o fato de que ela é uma linguagem de tipagem dinâmica. Isso significa que os tipos de dados em um programa Python podem ser alterados conforme o desejo do programador, não se preocupando nem em declarar o tipo de uma variável para o interpretador. Por exemplo, o seguinte código faz total sentido em Python:

x = 1

# Variáveis x é declarada contendo um tipo numérico

x = "Davi"

# Agora a variável x muda de tipo para string.
# Note que não foi necessário indicar ao interpretador de qual tipo a variável é(como em outras linguagens), assim como também não foi necessário fazer qualquer tipo de conversão de valor, que não fosse alocar um novo valor à variável. Esse é um exemplo de tipagem dinâmica(em outras linguagens isso não é possível!).


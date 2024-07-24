# !!!! INTRODUÇÃO AO CONCEITO DE ESCOPO !!!!

# Quando começamos a utilizar funções, um conceito implícito começa a entrar em vigor no nosso código: o escopo.

# -> O escopo é um determinador de qual local uma variável pertence, podendo existir apenas em determinados locais do programa, ou de forma geral e em todos os locais do programa.

# Existem dois tipos de escopo: local e global. O escopo local é um bloco de código que define suas variáveis como apenas existentes dentro dele. Já o escopo global diz respeito a todo o programa, aonde a variável pertence a qualquer lugar do código.

# Para facilitar o entendimento, vamos ver um exemplo:
def exemplo():
    a = 3.14
    print("Dentro da função existe uma variável com identificador 'a' cujo o valor é " + str(a))

# Como a própria mensagem da função diz, existe uma variável definida dentro da função. Já que a variável foi definida dentro da função, ela existirá APENAS dentro da função. Isso significa que se tentarmos acessar a variável fora da função, obteremos um erro:

# print(a) -> esse código gera um erro!

# O motivo do código acima gerar um erro é que o interpretador tenta localizar uma variável de nome 'a', porém não encontra, já que ela só existe dentro da função.

# Para que o interpretador encontre a variável, devemos executar a função. Dessa forma, a entre em vigor na execução do programa:
exemplo()

# Com a chamada da função acima, a passa a existir, mas apenas enquanto a função é executada. Uma vez finalizada e o interpretador saindo da função, a variável 'a' não existe mais.


# Portanto, uma variável de escopo local é uma variável definida em um bloco de código, que não seja o global.

# Agora, se tivermos uma variável definida de forma global no programa(fora de qualquer bloco de código de uma função), então poderemos acessa-la de qualquer parte do programa, inclusive uma função.
# Observe o exemplo:
x = 100

def acessando_global():
    global x
    x = 101
    print("Variável global modificada com sucesso")

acessando_global()

print(x)

# Note que agora, após a chamada da função, x vale 101 e não 100. Isso acontece porque, dentro da função, modificamos o valor da variável x.
# O contrário não seria possível, como vimos: acessar uma variável que foi criada dentro de uma função, do lado de fora.


# Por fim, em resumo, temos que um escopo global é tal que define um elemento que pode ser acessado por qualquer parte do programa. Já um escopo local define um elemento que só pode ser acessado por elementos do mesmo escopo, ou escopos aninhados.
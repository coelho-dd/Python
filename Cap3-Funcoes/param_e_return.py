# !!!! INTRODUÇÃO AO CONCEITO DE PARÂMETROS, ARGUMENTOS E DE RETURN !!!!

# -> Parâmetro -> Um parâmetro nada mais é do que um valor definido na criação da função, que será manipulado como uma variável que pertence apenas à função.

# Exemplo:
def exemplo(a, b):
    print("As variáveis a e b definidas pertencem à função exemplo() para serem manipuladas como a função quiser.")

# No exemplo acima, definimos dois parâmetros na declaração da função: a e b. Tanto a quanto b são variáveis que existem apenas dentro da função, aonde podem ser manipuladas da forma como a função desejar.

# Eis um outro exemplo:
def exemplo2(nome):
    print(nome)

# Na função acima, definimos um parâmetro chamado 'nome'. Esse parâmetro é uma variável que existirá apenas dentro da função e pode ser manipulada como a função desejar. Em seguida, a função exibe o nome no console, e termina. Note que nesse exemplo, definimos um parâmetro, e definimos um comportamento para o mesmo, que no caso foi mostrar seu valor no console.


# Continuando a lógica, agora precisamos de chamar a função. Porém, quando uma função possui um parâmetro definido, precisamos de especificar um valor para ele na hora da chamada. Do contrário, o interpretador gera um erro, indicando que a função possui um parâmetro mas que não foi passado um valor para ele.

# exemplo2() -> essa expressão de chamada geraria um erro!(está comentada para não travar o interpretador)

# O certo seria a seguinte chamada:
exemplo2("Davi")

# Na linha de código acima, o intepretador identifica que o valor passado entre os parênteses da função exemplo2() é o valor do parâmetro definido na função. Em outras palavras, o valor passado entre os parênteses é copiado para o parâmetro definido na hora da criação da função, fazendo com que 'nome' agora carregue o valor 'Davi'.

# Com isso, chegamos no conceito de argumento:


# -> Argumento -> Um argumento é o valor passado para um parâmetro na chamada da função.

# Ou seja, quando criamos uma função, definimos um parâmetro se for o caso. Quando chamamos uma função passamos um argumento, aonde seu valor será copiado para seu respectivo parâmetro.


# Vale a pena mencionar que, quando uma função tem múltiplos parâmetros, deverá receber múltiplos argumentos. Do contrário, o intepretador indicará um erro. Perceba um padrão: para cada parâmetro definido, deverá ter um respectivo argumento.

# Exemplo:
def soma(a, b, c):
    print(a + b + c)

soma(1, 2, 3)

# Na função acima, o parâmetro a receberá o argumento 1, o parâmetro b receberá o argumento 2 e o parâmetro c receberá o argumento 3, printando no console o valor 6.

# Um último ponto sobre parâmetros e argumentos é que, os valores são passados de posição para posição, como vimos no exemplo acima. Ou seja, o primeiro argumento é dado ao primeiro parâmetro, o segundo argumento é dado ao segundo parâmetro, o terceiro ao terceiro parâmetro, etc...




# -> Return -> A palavra-chave return é um indicador de que aquela função retorna um valor de interesse à parte chamadora da função.

# Vamos comparar as seguintes funções:
def exemplo3(a, b):
    print(a + b)

def exemplo_return(a, b):
    return a + b

# As duas funções, executam a mesma ideia: soma dois números. A diferença é que a função exemplo3() printa o resultado da soma na tela, e a função não printa o resultado na tela, e apenas retorna à expressão chamadora o resultado da soma.

# Então, quando chamarmos

exemplo3(1, 2) # -> irá aparecer o resultado de 1+2 no console
exemplo_return(1, 2) # -> não irá aparecer o resultado de 1+2 no console, porque ele não foi printado, mas sim retornado à expressão

# No caso, quando chamamos exemplo_return(1, 2), o resultado da soma é dado de volta à expressão. Para guardarmos o valor retornado de uma função com segurança, devemos utilizar uma variável:
valor_retorno = exemplo_return(1, 2)
print(valor_retorno)

# Agora, temos que o valor de retorno da função exemplo_return(1, 2) é guardado na variável valor_retorno. Para comprar que de fato o valor foi guardado adequadamente, printamos valor_retorno.

# Então, quando utilizamos a palavra-chave 'return' em uma função, um valor é retornado à expressão chamadora. Se quisermos guardar esse valor, devemos alocar em algum lugar específico, como uma variável por exemplo.

# Diga-se de passagem, uma função terminada por uma expressão de retorno é mais "correta" que uma função termina por uma expressão print() por exemplo. O motivo disso nós vimos na definição do que é função: "Uma função bem definida é uma que realiza apenas uma tarefa...". No caso, soma um valor e printar o valor na tela são duas tarefas diferentes. Dessa forma, separando essas tarefas, temos uma função mais concisa e precisa.
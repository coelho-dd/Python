# !!! INTRODUÇÃO A OPERADORES !!!

# -> Operadores nada mais são do que certos símbolos que permitem a manipulação de valores, de tal forma que nos permitem realizar ações específicas. 
# Os operadores são importantes em uma linguagem de programação, porque é através deles que podemos identificar o que é possível fazer ou não, em uma linguagem de programação.

# Temos diversos tipos de operadores: matemáticos, lógicos, relacionais e de atribuição.



# * Começando pelo mais simples: O de atribuição

# O operador de atribuição é o sinal de igual "=". É através desse operador que podemos atribuir valores às variáveis no programa.
# Por exemplo:

x = 1

# lê-se: "atribui 1 a x", ou "x recebe 1".

# Existem outras formas de atribuição, chamadas de atribuição compostas. Por exemplo:

x += 1
# que é o mesmo que x = x + 1... apenas uma forma abreviada de escrever uma expressão maior

# Ainda assim, podemos ler "x recebe x mais 1" ou "atribui x mais um a x".



# * Operadores aritméticos(matemáticos):

# Os operadores matemáticos definem uma série de operações matemáticas possíveis com a linguagem python:

# + -> soma
# - -> subtração
# * -> multiplicação
# / -> divisão
# % -> módulo(resto da divisão)
# ** -> exponenciação
# // -> divisão truncada(perde o decimal)

# Os operadores aritméticos se comportam exatamente como esses operadores se comportam na matemática ou como foi descrito acima.
# Ou seja, podemos escrever expressões matemáticas como 4 + 2 * (100 / 1) ** 2 em python, e elas possuem o mesmo resultado que na matemática




# * Operadores relacionais:

# Os operadores relacionais, como o próprio nome sugere, são operadores que relacionam um ou mais valores entre si. Eles sempre retornam um valor lógico(verdadeiro ou falso) das suas comparações.

# Eles são muito úteis para atribuições ou condições, por exemplo.
# São eles:

# == -> compara igualdade
# > -> maior que
# < -> menor que
# >= -> maior ou igual que
# <= -> menor ou igual que
# != -> compara diferença

# Ou seja, podemos ter a seguinte expressão:

y = 10 > 9

# A variável y terá o valor lógico True, já que 10 > 9 é verdadeiro.




# * Operadores lógicos:

# Os operadores lógicos são feitos para combinar logicamente uma série de elementos, resultado em um valor lógico(True ou False). Esses operadores seguem a lógica booleana.
# São eles:

# and -> só é verdadeiro quando todas as proposições são também verdadeiras
# or -> só é falso quando todas as proposições são também falsas
# not -> nega o valor da proposição

# Exemplo de uso dos operadores lógicos:

a = 1
b = 2
c = 3
d = 0

if (a and b) or (c and d):
    print("um dos agrupamentos é verdadeiro")

# No exemplo acima, a mensagem aparece porque temos dois grupos ligados logicamente por um operador 'or'. Como vimos, um operador 'or' só é falso quando todas as proposições que o compõe forem também falsas. Porém, um dos agrupamentos tem o resultado como verdadeiro, fazendo com que a condição seja verdadeira.




# * Valores falsy e truthy

# Com a introdução dos valores lógicos(True e False) no nosso repertório, é importante saber que Python tem alguns comportamentos interessantes em situações especiais.

# O conceito de valores truthy e falsy dizem respeito ao valor lógico adjacente de um valor qualquer não-lógico.

# Por exemplo, valores falsy são valores não-lógicos de python que possuem um valor lógico False inerentemente.
# São esses valores: 0, None, estruturas vazias(strings, listas, dicionários, tuplas, sets).

# Por exemplo:

z = 0

if z:
    print("Isso não vai aparecer no console.")

# A mensagem dentro de if não irá aparecer no console porque 0 é um valor que carrega um valor lógico False de forma implícita, e if precisa de um valor True para ser executado.

# O mesmo aconteceria caso z fosse None ou uma estrutura de dados ou string vazia.

# Em contraste com os valores Falsy, os Truthy são valores não-lógicos que carregam um valor True implícito.
# Todos os valores que não são Falsy são Truthy, ou seja, todos os valores que não são 0, None e estruturas vazias são Truthy.

# Portanto, por isso é possível escrever:

w = 1

if w:
    print("Isso está sendo mostrado porque 1 é truthy e portanto o if é verdadeiro.") 
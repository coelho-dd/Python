# !!! INTRODUÇÃO ÀS LISTAS !!!

# -> Listas são um tipo de variável de python, que carregam diversos valores(diferentes ou iguais) dentro de uma só varíavel, e possuem índices que permite a identificação de cada elemento presente na estrutura.

# Em outras palavras, uma lista é uma estrutura de dados heterogênea e ordenada(através de índices). É importante saber também que os índices começam do número zero, e não de um.
# O tamanho de uma lista é igual ao número de elementos que existem dentro dela(!).

# Vejamos alguns exemplos de listas:

L = [] # uma lista vazia
Z = [15, 8, 9] # uma lista não vazia com apenas tipos numéricos
W = ["Davi", 24, 4, 2001, True] # uma lista não vazia com diferentes tipos de dados

# Como sabemos agora, uma lista possui índices, que permite a localização e diferença de um elemento para outro.

# Eis um exemplo do uso de índices, com as listas acima:

print(Z[0]) # printando o primeiro elemento da lista Z
print(W[2]) # printando o terceiro elemento da lista W(lembre-se: os índices começam por 0 e não por 1)

# Com isso, vemos que é possível acessar cada elemento de forma individual, através dos índices, sabendo que começam de 0.

# Não é possível acessar um elemento de uma lista diretamente que não seja através de um índice. Portanto, em uma lista(e em algumas outras estruturas como veremos mais adiante), o que diferencia um elemento do outro é seu índice e não seu conteúdo, na prática.

# Como vimos também anteriormente, existe uma estrutura de repetição própria para ser utilizada com estruturas de dados iteráveis, como listas: o loop for.

# Se quisessemos printar na tela cada elemento de uma lista, sem utilizar a função print() para cada elemento, faríamos:

for i in Z: # para cada elemento na lista Z
    print(i) # printe o elemento

# Como eu acredito que seja importante um entendimento mais amplo, eis o mesmo código do loop acima, mas no loop while:

x = 0
while x < 3:
    print(Z[x])
    x += 1

# Perceba a maior quantidade de código necessário, além de ter que definir um contador, uma condição e explicitar na função print() a notação de índice utilizando o contador. Em programação, códigos mais complicados, mesmo que não seja tão complicado a primeira vista, são mais propensos ao erro. Portanto, a não ser que exista uma boa razão para utilizar um loop while em uma estrutura de dados, use for.


print()


# -> Listas são mutáveis! Na prática, isso significa que podemos alterar o conteúdo de um elemento dentro da lista a hora que quisermos.

# Temos a lista Z como [15, 8, 9]

# Eis um exemplo:

Z[0] = 7 # alterando o primeiro elemento da lista Z para 7

# Agora temos que Z = [7, 8, 9]


print()


# Cópias e fatiamento de listas:

# Para criar cópias de listas, pode parecer intuitivo escrever algo como lista2 = lista1. Porém, isso funciona em partes. De fato, lista2 carregará os mesmos valores que lista1, porém será a mesma lista e não listas diferentes.

# Eis um exemplo:

exemplo1 = [1, 2, 3, 4, 5]
exemplo2 = exemplo1

print(exemplo1)
print(exemplo2)

# Veja que temos os mesmos elementos em cada lista! Mas não são listas diferentes, mas sim a mesma lista.

# Para provar que é a mesma lista nas duas variáveis, faremos o seguinte experimento:

exemplo2[0] = 10

# Se forem listas diferentes, apenas o primeiro elemento de exemplo2 será modificado, e não o primeiro elemento de exemplo1.

print(exemplo1) # [10, 2, 3, 4, 5]
print(exemplo2) # [10, 2, 3, 4, 5]

# Veja que mesmo modificando apenas exemplo2, mudamos também exemplo1, provando que é a mesma lista em ambas as variáveis.

# O motivo disso é o seguinte: Uma lista em python é um objeto, e não um tipo "simples" como inteiros, decimais, strings, etc. Um objeto possui comportamentos diferentes de uma variável com tipos "simples". 

# Quando criamos um objeto, a variável que o carrega, na verdade não contém de fato o objeto, mas sim aponta para o objeto na memória. Em outras palavras, quando criamos um objeto e o atribuímos a uma variável, como em exemplo1 = [1, 2, 3, 4, 5], estamos na verdade criando o objeto lista na memória e atribuindo o endereço desse objeto à variável exemplo1. Portanto, temos uma variável de referência ao objeto, e não uma variável que contém o objeto em si.

# O efeito disso é que, quando digitamos exemplo2 = exemplo1, estamos indicando ao interpretador que a variável exemplo2 fará uma referência ao mesmo objeto que a variável exemplo1. Como ambas fazem referência ao mesmo objeto, se o modificarmos através de uma variável de referência, a outra também irá receber a mudança já que as duas apontam para o mesmo objeto. E é por isso que utilizar o operador de atribuição para copiar listas(na verdade, objetos) não é uma boa ideia, a não ser que essa seja a intenção.


# Então, como podemos copiar uma lista para outra variável, sem fazer com que as duas apontem para o mesmo objeto? Através do fatiamento.


# -> O fatiamento em python é uma forma de lidar com pedaços específicos de uma estrutura. Por exemplo, podemos pegar os 3 elementos do meio da variável exemplo1:

print(exemplo1[1:4])

# A notação de fatiamento é [inicio:fim-1], considerando o fato de índices funcionam a partir do zero. Então, no exemplo acima, temos que vamos printar o segundo elemento(1) até o quarto menos um(4 - 1). Em outras palavras, a forma geral do fatiamento é [inicio:fim[(inicio inclusivo e fim exclusivo).

# Por fim, para conseguir copiar uma lista para outra, utilizaremos a notação de fatiamento(já que ela lida apenas com o conteúdo em si e não com a referência ao objeto):

exemplo3 = exemplo1[:] # quando omitimos um índice na posição de inicio ou fim(ou ambos) estamos indicando todo o intervalo
print(exemplo3) # agora, exemplo3 tem uma cópia do conteúdo de exemplo1 mas sem a referência ao objeto





# Utilizando a função len():

# A função len() é muito utilizada com estruturas de dados, e por consequência com listas, pelo fato de retornar o tamanho da lista(quantidade de elementos de uma lista). Podemos utiliza-la para controlar o tamanho de loops, para ter certeza de que não ultrapassaremos o tamanho dos índices, etc.

# Exemplo de uso da função len():

print(len(exemplo3)) # retorna 5 porque a lista contém 5 elementos





# Adição e remoção de elementos de uma lista:

# Ao invés de adicionarmos elementos indicando o índice, existem funções que nos permitem adicionar ou remover elementos de forma mais simples:

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1.append(11) # adiciona um elemento ao final da lista(nesse caso 11)
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lista1.pop() # remove o elemento no final da lista por padrão
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ...entre outras funções de adição e remoção
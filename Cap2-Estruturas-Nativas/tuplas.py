# !!! INTRODUÇÃO À TUPLAS !!!

# -> Tuplas funcionam exatamente como listas, contendo as mesmas operações, a única diferença é que um valor dentro de uma tupla NÃO pode ser alterado. Ou seja, na prática, tuplas são imutáveis. 
# -> Além disso, uma tupla é escrita com parênteses, e não com colchetes.

# Exemplo de tupla:
tupla1 = (1, 2, 3, 4) # cria uma tupla

# Provando que uma tupla não pode ser alterada:
# tupla1[0] = 10   ->   # essa expressão gera um erro, já que está tentando mudar o primeiro elemento da tupla. (para rodar os códigos seguintes, a expressão foi transformada em comentário)


# Assim como listas, podemos utilizar loops para iterar sobre uma tupla, já que é uma estrutura iterável. Além disso, podemos concatenar uma tupla com outra, assim como listas:
tupla2 = (5, 6, 7, 8, 9, 10)
for i in tupla2:
    print(i)

tupla3 = tupla1 + tupla2
print(tupla3)

# Não há muito o que mostrar, já que no geral, uma tupla se comporta como uma lista com a única diferença de que um elemento da tupla não pode ser alterado.
# Ela é útil para armazenar constantes, por exemplo, e muitas partes da linguagem python utiliza tuplas por debaixo dos panos para realizar suas operações!

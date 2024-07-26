# !!!! ESTUDANDO MAIS UM POUCO SOBRE PARÂMETROS !!!!

# Como vimos, um parâmetro é um valor definido entre os parênteses da definição da função, que funcionará como uma variável que só existe na própria função, ou seja, uma variável local.
# Existem algumas nuances extras quanto parâmetros, que veremos agora.

# -> Parâmetros opcionais:
# É possível definir parâmetros opcionais, que não precisam ser chamados obrigatoriamente com argumentos. Os parâmetros opcionais possuem um valor padrão, que serão levados em conta caso o programa não utilize argumentos na chamada da função.

# Observe um exemplo:
def saudacao(nome="Usuário"):
    print(f"Olá, {nome}!")

saudacao() # -> quando chamarmos saudacao() sem argumentos, nome terá o valor padrão definido na criação da função, que nesse caso é "Usuário"
saudacao("Davi") # -> Quando chamarmos saudacao() com algum argumento do tipo string, o parâmetro nome irá receber esse valor, seja ele qual for, substituindo o parâmetro padrão "Usuário"

# Com isso, podemos definir valores padrões para que a função possa utilizar, caso nenhum for especificado pela chamada.



# -> Parâmetros nomeados:

# Seguindo a mesma lógica com parâmetros, podemos definir uma ordem personalizada para a chamada de uma função com vários parâmetros, ao nomearmos especificamente os argumentos.
# Por exemplo:

def pessoa(nome, idade, profissao, cidade):
    print(f"Nome: {nome} \nIdade: {idade} \nProfissão: {profissao} \nCidade: {cidade}")

pessoa(profissao="Programador", idade=23, nome="Davi Coelho", cidade="Rio de Janeiro")

# Note que ao invés de utilizarmos a sequência de argumentos pré-definidos pelos parâmetros da função, definimos uma ordem personalizada na chamada. A ordem, então, deixa de ser importante já que estmaos especificando diretamente o valor de cada parâmetro com o sinal de "=". Em outras palavras, estamos atribuindo valores, especificamente, para cada parâmetro definido na criação da função, não utilizando a relação de ordem padrão entre argumentos e parâmetros. 

# Essa é a operação de nomeação de parâmetros.
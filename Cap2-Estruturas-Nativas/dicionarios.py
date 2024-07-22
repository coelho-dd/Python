# !!!! INTRODUÇÃO AO DICIONÁRIO PYTHON !!!!

# -> Um dicionário é uma outra estrutura de dados nativa de python, assim como listas, tuplas, etc. O dicionário é parecido com uma lista, porém com algumas diferenças consideráveis. Por exemplo, o dicionário é delimitado por chaves({}) e não colchetes, como as listas. Ele também possui índices, mas não são numéricos, são nomes próprios definidos pelo programador.

# Observe um exemplo de dicionário:

dic1 = {"nome": "Davi", "idade": 23, "profissao": "programador", "solteiro": False}

# No dicionário acima, definimos uma série de dados que representam uma pessoa. Note que visualmente um dicionário é bastante diferente de uma lista, mas a lógica em si é parecida.

# Um dicionário, de forma mais técnica, é composto por um par chamado de par chave/valor. A chave funciona como o índice(chave), que dá acesso ao valor. A chave é o primeiro item antes dos dois pontos, e o valor é o primeiro item após os dois pontos. Portanto, quando temos o conjunto [chave: valor].

# Uma chave pode ser qualquer valor primitivo, ou seja, tipos numéricos e strings, mas não pode ser um objeto. Porém, um valor pode ser de qualquer tipo(números, strings, booleanos, objetos, etc).



# Como vimos, o que dá acesso ao valor é a chave, e se comportam como índices. Portanto, para acessar um valor de um dicionário, podemos utilizar a notação de colchete, assim como em listas:
print(dic1["nome"])
print(dic1["idade"])


# Podemos também adicionar chaves que não existem no dicionário:

dic1["nacionalidade"] = "brasileiro"

# Note que a notação para adicionar uma nova chave ao dicionário, utilizamos a mesma notação que listas!



# Assim como listas, dicionários possuem suas próprias funções especiais, que permitem a manipulação de certos elementos de um dicionário. 
# Algumas dessas funções:

# dicionario.keys() -> retorna uma lista das chaves existentes no dicionário.
# dicionario.values() -> retorna uma lista dos valores presentes no dicionário.
# etc...


# Um último ponto que vale a pena mencionar sobre os dicionários é que assim como as listas, eles são objetos. Então, a variável que "carrega" um dicionário é na verdade uma referência ao objeto na memória, e não o dicionário em si. Isso foi explicado na introdução às listas.
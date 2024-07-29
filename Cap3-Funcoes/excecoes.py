# !!! INTRODUÇÃO À EXCEÇÕES !!!

# -> Essencialmente falando, uma exceção é um erro que ocorre dentro de um programa. Por exemplo, se tentarmos concatenar um tipo numérico com uma string, o interpretador irá apresentar um erro que foi gerado pelas interações no código. 

# -> É importante saber, porém, que o erro gerado tem propriedades específicas, e é tratado como um objeto em Python. Na prática, isso significa que um erro possui atributos e métodos que permitem manipulá-lo da forma como quisermos.

# Eis um exemplo de erro gerado no código:
# print("Teste: " + 1) # -> Essa linha de código gera um erro cujo o identificador é um TypeError, e a mensagem é "can only concatenate str (not "int") to str."

# Ao tentar executar a linha acima, o interpretador irá indicar no console que um erro foi gerado, e irá parar a execução do programa, mesmo que tenha outros códigos após a expressão com erro. Esse é um dos motivos para existir o tratamento dos erros: para que a execução do programa não pare, fazendo com que o programa quebre.

# Para que um programa não pare sua execução, e mesmo que um erro aconteça continue executando, devemos utilizar uma estrutura de código específica: try/except/finally. Essa estrutura funciona como uma estrutura if/elif/else, ou seja, é uma estrutura de controle que ajuda a manter a execução do código fonte escrito.

# Eis um exemplo básico do uso das cláusulas try/except:
try:
    print("Teste: " + 1)
except:
    print("Não é possível concatenar um tipo numérico com uma string diretamente.")

print("Essa mensagem ainda é executada pelo interpretador.")

# Algumas coisas são importantes com o exemplo acima. Primeiro, note como temos uma estrutura parecida com if/else no código, mas que nesse caso é uma estrutura para tratamento de exceções try/except. Ela funciona da seguinte forma: o bloco 'try' carregará o código que pode gerar algum tipo de erro. Caso for detectado alguma exceção gerada pelo código dentro de 'try', o bloco 'except' será acionado imediatamente, executando seu bloco de código. Mesmo que um erro seja detectado pelo bloco 'try', o interpretador não para de executar o restante do código(o que não aconteceria sem a estrutura), como vimos com a execução do último print().

# Mas cadê a cláusula 'finally'? Essa cláusula é uma cláusula opcional, que podemos adicionar para executar um código sempre, mesmo que uma exceção seja encontrada e não tratada. Por exemplo:

# try:
#     print("Teste: " + 1)
# finally:
#     print("Essa mensagem ainda aparecerá, mesmo que o código em 'try' tenha gerado uma exceção não tratada.")
# 
# print("Essa mensagem não vai aparecer.")

# Note que a estrutura acima não possui uma cláusula 'except', ou seja, não possui tratamento para a exceção gerada no bloco 'try', fazendo com que o programa pare sua execução. Perceba, porém, que a mensagem do bloco 'finally' ainda assim foi executada. Como disse, o bloco de código na cláusula 'finally' sempre é executado, independente do tratamento de exceções ou não.




# -> Interessantemente, podemos ser mais específicos na cláusula 'except', indicando diretamente o erro no qual estamos tratando. Fazemos isso, apontando o identificador da exceção após 'except':
L = [1, 2]
try:
    print(L[1000])
except IndexError:
    print("Índice fora do tamanho da lista.")

# Como o código print(L[1000]) gera um erro de índice(IndexError), aonde é uma indicação de que a expressão está tentando acessar um índice que não existe na lista, podemos indicar o identificador desse mesmo erro na cláusula 'except'. O que isso faz, na prática, é que qualquer erro que não seja um IndexError será ignorado por 'except'. Isso pode ser bom, ou ruim, dependendo do programa em questão.

# Uma cláusula 'except' vazia apresenta uma forma de capturar qualquer erro gerado por 'try', ou seja, é mais genérico. Já uma cláusula 'except' com um erro especificado, permitirá a identificação exata do que ocorreu no programa.
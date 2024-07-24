# !!!! INTRODUÇÃO ÀS FUNÇÕES !!!!

# Funções são tão importantes em programação, que existem paradigmas que definem um programa inteiro em volta dessa estrutura.

# -> Funções são estruturas de código com sua própria lógica, aonde definimos uma parte do programa que existe de forma independente do resto, podendo ser chamada a qualquer momento para realizar a sua ação. Em outras palavras, funções são mini-programas independentes, dentro do próprio programa. Também são chamadas de sub-rotinas.

# -> Uma função bem definida executa apenas uma ação, de forma clara e concisa, existindo de forma independente e gerando o mesmo resultado para a mesma entrada.

# Eis um exemplo de uma função:
def exemplo():
    print("Hello function world!")

# No exemplo acima, definimos uma função de nome exemplo(), que ao ser chamada executa seu bloco de código. Nesse caso, o bloco de código apenas exibe uma mensagem no console. Ou seja, toda vez que a função for chamada, sua mensagem irá aparecer.

# Chamando a função:
exemplo() # -> exibe no console a mensagem "Hello function world!"



# No caso, com o conceito de função, surge o conceito de chamada. 
# Uma função sempre tem parênteses, vazios ou com algumas informações. Ao saber disso, quando um interpretador lê um nome seguido imediatamente de um parênteses, ele identifica que aquilo é uma função. Portanto, existe uma diferença entre 'exemplo' e 'exemplo()': Na leitura do primeiro o intepretador irá tentar localizar uma variável de nome 'exemplo' e no segundo irá tentar localizar uma função de nome 'exemplo()'.

# Quando dizemos que "chamamos" uma função, estamos querendo dizer que digitamos seu nome no código. Lembre-se: uma função sempre carrega parênteses imediatamente após o seu nome. Então, quando escrevemos 'exemplo()', estamos na verdade chamando aquela função.
# Ao ler 'exemplo()' no código fonte, o intepretador imediatamente começa a ler o código da função. Em outras palavras: Quando chamamos uma função, estamos indicando ao interpretador que desejamos executar o bloco que define a função, naquele instante.

# Eis mais um exemplo:
def soma(a, b): # definindo uma função que soma dois números
    print(a + b)

soma(1, 2) # chamando a função passando alguns dados para que ela execute de forma bem sucedida

print("Isso é executado apenas depois da execução da função")

# No exemplo acima, primeiro definimos uma função chamada soma() que recebe dois dados importantes para a sua execução. Em seguida, chamamos a função passando os dados para que ela funciona adequadamente. Quando o intepretador ler "soma()" ele irá executar seu código imediatamente, retornando ao resto do código apenas após o fim da execução da função.



# Então, temos uma lógica: O intepretador lê o código da esquerda para a direita, de cima para baixo, assim como lemos um livro. Porém, quando ele se depara com uma chamada de uma função, ele imediatamente para a execução do código em si, e passa a executar o código da função. Uma vez finalizada a função, ele retorna a execução do restante do código normalmente.
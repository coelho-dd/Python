# !!!! INTRODUÇÃO AOS CONSTRUTORES !!!!

# -> Um construtor nada mais é do que um método que sempre é executado quando ocorre um instanciamento de um objeto.

# Quando criamos uma classe, é importante definir um método construtor. Esse método será chamado, pela própria linguagem, toda vez que um objeto for instanciado. Nele, podemos definir dados importantes para o objeto, e comportamentos de interesse da classe.

# Eis um exemplo de um método construtor:
class Exemplo:
    def __init__(self):
        print("Essa mensagem está sendo executada dentro do método construtor, que é chamado a cada instanciamento")


exemplo1 = Exemplo()

# Note que no código acima, definimos um método de nome '__init__()'. Em python, todo método que possui 4 sublinhados é um método especial e que possui um trabalho específico. Nesse caso, ele executa um bloco de código todo instanciamento. Esse método foi executado através da criação do objeto 'exemplo1', aparecendo a mensagem no console, o que prova que ele é chamado a cada instanciamento de objeto.

# Antes de continuarmos falando sobre os construtores, devemos falar sobre a palavrinha mágica da programação orientada a objetos: self. 
# A palavra-chave 'self' é uma referência direta ao objeto que está sendo usado no momento. Por exemplo, quando o construtor é chamado, ele é chamado em relação a um objeto. No caso do instanciamento acima, ele foi chamado através do instanciamento de exemplo1. Nesse caso, o construtor foi chamado em relação ao objeto exemplo1. Então, é a partir de 'exemplo1' que essa mensagem é executada. Para ficar mais claro, veja o seguinte exemplo:
class Exemplo2:
    def metodo_exemplo(self):
        print("essa mensagem vem do acesso do próprio objeto ao método")

exemplo2 = Exemplo2()
exemplo2.metodo_exemplo()

# Quando executamos a expressão de chamada exemplo2.metodo_exemplo(), a mensagem do método irá aparecer no console. Note que o método tem como parâmetro a palavra-chave 'self'. O que está acontecendo por trás dos panos é o seguinte: A notação de ponto para chamar um método, 'exemplo2.metodo_exemplo()', indica de forma mais clara que o método está sendo chamado a partir do objeto. Quando isso ocorre, o método recebe implicitamente o próprio objeto que o chama, que nesse caso é exemplo2. Como 'self' é "uma referência direta ao objeto que está sendo usado no momento", sendo esse objeto 'exemplo2', então metodo_exemplo() recebe 'exemplo2' como argumento, dessa forma podendo acessar o conteúdo do método através do objeto.

# Em outras palavras: Para cada método definido em uma classe, deve existir o parâmetro self. O motivo para isso é que, para que o objeto consiga acessar o método x ele precisa de se passar como argumento.


# Agora que desvendamos a palavra-chave 'self', eis mais um exemplo de construtor, aonde passamos informações relevantes ao objeto:
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def altera_endereco(self, novo_endereco):
        self.endereco = novo_endereco


# A classe acima é uma representação mais completa e exata da classe representada no arquivo de introdução desse capítulo.
# No código logo acima, temos alguns pontos interessantes.

# Primeiro, o construtor contém parâmetros. O motivo para isso é que nos permite definir dados de forma mais dinâmica, no momento de instanciar o objeto.
# Observe:
pessoa1 = Pessoa("Davi", 23, "Brasil")

# Na criação do objeto acima, passamos valores representando os dados de uma pessoa ao construtor. Sim, a notação NomeDaClasse() é uma chamada ao método construtor da classe.

# No método construtor definido da classe Pessoa, definimos que self.nome receberá o argumento nome, self.idade receberá o argumento idade e self.endereco o argumento endereco. Como vimos, 'self' é uma referência direta ao objeto que está sendo usado no momento. Ou seja, a expressão self.nome = nome, quer dizer que o atributo nome do objeto será igual ao argumento nome passado ao construtor. E isso ocorre para cada parâmetro passado ao construtor, quando esse valor é passado a algum atributo de self.

# Após o método construtor, definimos um outro método para alterar o atributo endereco do objeto. Isso só acontecerá caso o método seja chamado. Note que o método recebe 'self' e um parâmetro qualquer, que carregará o novo endereço. Como vimos, a expressão 'self.endereco = novo_endereco' é um indicador de que o atributo endereco do objeto em questão será alterado para o argumento passado ao método na hora da chamada.



# Por fim, entendemos que um método construtor é um método que é chamado na hora do instanciamento de um objeto, aonde ele pode ou não carregar informações e ações interessantes aos objetos em questão.

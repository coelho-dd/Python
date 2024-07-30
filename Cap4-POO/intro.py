# !!!! INTRODUÇÃO À POO !!!!

# -> Programação orientada a objetos é um paradigma de programação, que gira em torno de objetos representados no código, aonde tais elementos interagem entre si para compor o programa.

# Apenas pela frase acima, podemos destrinchar alguns conceitos chave. 

# -> Um paradigma de programação nada mais é do que uma lógica que envolve a forma de escrever um código fonte. Existem diversos paradigmas, cada um com sua própria lógica. Temos o paradigma funcional, procedural, orientado a objetos, etc. O mais comum é o procedural, aonde definimos linha a linha o que o computador deve fazer. O paradigma funcional gira em torno de funções, e o orientado a objetos em torno de objetos. Recomendo uma leitura mais afundo na internet sobre os paradigmas, se for do interesse.

# Para entender o paradigma orientado a objetos, devemos primeiro entender dois conceitos fundamentais que compõem tal paradigma: O de classes, e o de objetos.

# -> Uma classe é um conjunto de códigos variados, podendo ser dados, manipulações de dados ou ambos, agrupados em um mesmo ambiente. Ela serve como uma abstração de conceitos. Por exemplo, podemos definir uma classe que simula uma pessoa, contendo nome, idade, endereço, etc. Além de termos dados, podemos ter meios de manipulação desses dados, como alterar o endereço da pessoa por exemplo. Tudo isso contido dentro de uma classe, encapsulando todo o código.

# Eis um exemplo de uma classe:
class Pessoa:
    nome = "Davi"
    idade = 23
    endereco = "Brasil"

    def muda_endereco(self):
        self.endereco = "EUA"

# No exemplo de classe acima, definimos uma tal que temos uma representação de uma pessoa, com dados definindo suas características, e uma função intitulada 'muda_endereco()' que muda o valor do endereço da pessoa.

# -> É importante saber que, sob o contexto de programação orientada a objetos, uma função recebe um novo nome: métodos. Claro, ainda funcionam e se parecem exatamente como uma função, mas são chamadas de métodos quando existem sob uma classe. Portanto, na classe acima, temos um método chamado 'muda_endereco()' e não uma função com esse nome.

# -> Uma outra nomenclatura que muda sob o contexto de uma classe são as variáveis. Elas ainda se comportam como tal, mas quando existem dentro de uma classe são chamados de atributos e não variáveis(apesar de que podem existir fontes que a chamem de variáveis de classes).


# Agora que sabemos um pouco do que é uma classe(um encapsulamento de códigos relacionados), devemos entender o conceito de objetos. 
# Quando criamos uma classe, temos um monte de código que não tem ação no programa. Uma classe é um código passivo. Isso significa que, ao apenas criarmos uma, não poderemos fazer nada com ela, a não ser que seja criado um objeto a partir dela. Do contrário, uma classe é apenas uma especificação de uma série de códigos passivos(quando não existe algum objeto).

# Podemos encarar uma classe como um código passivo, e um objeto como um código ativo. Isso fará mais sentido adiante.

# Como vimos, uma classe não faz nada. Ela apenas define uma série de código, no qual um objeto irá agir em cima. Então, como criamos um objeto? Precisamos iniciar um objeto, a partir de uma classe, com o seguinte código: nome_objeto = NomeClasse().

# Exemplo:
pessoa1 = Pessoa()

# No código acima, criamos uma variável, que recebe a inicialização da classe Pessoa. Isso faz com que, a variável 'pessoa1' se torne um objeto da classe 'Pessoa', criando um objeto. O nome para esse processo é: instanciamento. Quando criamos um objeto, temos uma instância de uma classe.

# Agora que temos um objeto, temos uma forma de interagir com o código da classe.
# Como podemos ver a segur, um objeto carrega o código da classe dentro de si:

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.endereco)

# Note que nas 3 linhas de código acima, estamos printando os dados que representam uma pessoa, que estão contidos na classe Pessoa. Isso é uma indicação de que um objeto carrega o próprio código da classe dentro de si. Isso, em programação orientada a objetos, é chamado de encapsulamento: onde um objeto encapsula todo o código definido pela classe.

# Além de um objeto carregar todos os atributos(variáveis de classe) existentes na classe, ele também carrega os métodos. Ou seja, podemos chamar o método muda_endereco() a partir do objeto:
pessoa1.muda_endereco()
print(pessoa1.endereco) # Agora, temos que o endereço de pessoa1 é 'EUA' e não 'Brasil'

# Perceba então que, a proposição de que uma classe é um código passivo e um objeto é um código ativo, é verdadeira. É a partir do objeto, e das suas interações no código, que conseguimos realizar as ações para um programa rodar apropriadamente. Uma classe apenas serve de base para um comportamento do objeto.


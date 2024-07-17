# !!! INTRODUÇÃO ÀS CONDIÇÕES !!!


# Um conceito fundamental do mundo da programação é o de condição. Nessa estrutura de código que veremos a seguir, temos que um código é executado ou não, de acordo com uma condição específica. Por exemplo: 
 
# Se estiver chovendo, pegue o guarda-chuva. Senão não pegue.

# Nessa condição, levamos em conta o tempo e tomamos uma decisão de acordo com ele. Podemos representar essa lógica em código da seguinte forma:

chovendo = True

if chovendo: # se if for verdadeiro
    print("Pegue o guarda-chuva.")
else: # se if for falso
    print("O guarda-chuva não é necessário.")

# No código acima, estabelecemos uma condição que será utilizada para realizar uma ação ou não, que no caso é uma variável do tipo lógico chamada 'chovendo'. Se chovendo for True(verdadeiro) será printado na tela a mensagem "Pegue o guarda-chuva.". Se chovendo for False(falso), será printado na tela a mensagem "O guarda-chuva não é necessário." terminando o programa.

# Essa é a lógica básica de uma condição em programação: Temos um elemento(ou vários) no qual queremos nos basear e tomar uma ação no código de acordo com seu estado. 




# * As cláusulas da estrutura condicional

# Quando se trata de condicionais em Python, temos 3 cláusulas(palavras-chave) que realizam tarefas diferente. Já vimos duas delas: o 'if' e o 'else'. 

# if -> A cláusula if é utilizada para iniciar uma estrutura condicional. Quando a digitamos no código, estamos indicando ao interpretador que está sendo criado uma condição.
# else -> A cláusula else é utilizada para definir uma ação que só será executada caso if não seja. Em outras palavra, se a condição estipulada em if for falsa, então else é executado.

# Para fins didáticos, vamos utilizar mais um exemplo, dessa vez com uma entrada de usuário:

usuario = input("Digite qual sua marca de carro preferida: ")

if usuario == "porsche": # se a entrada do usuário for igual a "porsche"(o operador == compara valores para igualdade)
    print("Você tem muito bom gosto!")
else:
    print("Legal! Você gosta da " + usuario)

# No código acima, o usuário irá nos fornecer uma marca de carro do seu agrado. Caso o usuário digite a palavra "porsche", uma mensagem específica é utilizada para interagir com o usuário. Caso ele digite qualquer outra marca, uma outra mensagem específica entra em vigor. Note que temos um padrão: Definimos uma condição na cláusula if(que nesse caso é se a entrada do usuário for igual a "porsche"), e logo em seguida definimos uma condição para ser executada caso a condição de if for falso(o usuário não digite "porsche"), que no caso é a cláusula else.

# Para completar a estrutura condicional, temos a última cláusula: 'elif'.

# elif -> Essa cláusula pode ser repetida quantas vezes forem necessárias, para garantir que o programador consiga estabelecer um código para reagir a todas as condições necessárias. Essa cláusula é necessária porque um par if/else não pode ser repetido(a não ser que seja aninhado).

# Eis um exemplo da cláusula elif:

time = "Barcelona"

if time == "Real Madrid":
    print("Torcedor do Real Madrid.")
elif time == "Atlético de Madrid":
    print("Torcedor do Atlético de Madrid.")
elif time == "Valencia":
    print("Torcedor do Valencia.")
elif time == "Mallorca":
    print("Torcedor do Mallorca.")
elif time == "Celta de Vigo":
    print("Torcedor do Celta de Vigo.")
else:
    print("Torcedor de outro time não presente na lista...") # esse código é executado

# Note que no código acima temos 4 cláusulas elif, e poderíamos ter quantas forem necessárias para o programa. Não que seja melhor opção de código, mas é possível estabelecer uma enxurrada de códigos elif. Essa é apenas uma demonstração para demonstrar que esse é o caso. 

# O motivo para a cláusula elif existir, não é só para garantir que o programador consiga atingir a todas as condições necessárias para a sua aplicação, como também para remover os if/else aninhados.

# Eis um exemplo do mesmo código escrito acima, sem a cláusula elif:

if time == "Real Madrid":
    print("Torcedor do Real Madrid.")
else:
    if time == "Atlético de Madrid":
        print("Torcedor do Atlético de Madrid.")
    else:
        if time == "Valencia":
            print("Torcedor do Valencia.")
        else:
            if time == "Mallorca":
                print("Torcedor do Mallorca")
            else:
                if time == "Celta de Vigo":
                    print("Torcedor do Celta de Vigo.")
                else:
                    print("Torcedor de outro time não presente na lista...")

# Pode parecer que a existência da cláusula elif não é necessária, mas em códigos mais complexos e maiores, a necessidade da sua presença fica muito mais clara.

# Como vemos acima, a falta de 'elif' nos força em uma estrutura que pode rapidamente se tornar desorganizada e complexa de manter.

# Portanto, em um conjunto if/elif/else, temos que a relação entre essas cláusulas é a seguinte: if define a primeira condição e inicia a estrutura. Caso if seja falso, o interpretador pula para a condição elif. Se elif for falso, ele pula para outra condição elif(se existir) e continua o processo até não ter mais nenhum elif. Se todas as condições, tanto if quanto elif, forem falsas, a cláusula else é executada(como vimos no penúltimo exemplo).
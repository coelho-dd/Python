# !!! INTRODUÇÃO AOS LOOPS E SEUS ELEMENTOS !!!

# * Em programação existe uma estrutura muito útil: os loops. Eles te permitem executar o mesmo código para uma série de elementos.

# Por exemplo, imagine que seja necessário calcular a média de duas notas para uma turma de 100 alunos. Seria inviável escrever o seguinte código:
aluno1 = (100 + 90) / 2
aluno2 = (50 + 50) / 2
aluno3 = (25 + 100) / 2
aluno4 = (100 + 100) / 2
# 100 vezes...

# Obviamente ficaria muito repetitivo e cansativo escrever essse código. Isso é facilmente resolvido pela estrutura de loop.

# Por exemplo(estudaremos os loops em mais detalhes adiante):
x = 1
while x <= 100:
    nota1 = int(input("Primeira nota do aluno " + str(x) + ": "))
    nota2 = int(input("Segunda nota do aluno " + str(x) + ": "))
    media = (nota1 + nota2) / 2

    print("Média do aluno " + str(x) + " é igual a: " + str(media) + "\n")

    x += 1

# No código acima, definimos um loop que executará o código desejado(calcular a média de duas notas dos 100 alunos) de forma muito mais simples e automática, em relação a calcular manualmente como vimos no primeiro exemplo. Esse é o poder da estrutura de loop.

# Claro, quando estamos falando de poucos números, um loop não parece tão necessário. Porém, é mais do que comum trabalhar com uma quantidade enorme de dados, aonde codificar um por um de forma manual é simplesmente inviável e até mesmo impossível. 

# Imagine, por exemplo, que um programador da Amazon precisa realizar uma ação para cada conta cadastrada no banco de dados de usuários ativos. Vale mais a pena realizar isso através de um loop, ou codificar manualmente um bloco de código específico?




# * Loop while:

# Existem duas estruturas de loops principais em python, while e for. Veremos agora o loop while.

# -> O loop while define uma condição(verdadeiro ou falso) que será verificada no início de cada iteração do loop, incluindo a primeira, aonde seu bloco será executado *enquanto* a condição for verdadeira.

# Exemplo:
exemplo = 1 # contador
while exemplo <= 10:
    print(exemplo)
    exemplo += 1 # incrementando em 1 o valor do contador a cada iteração

# O código acima pode ser lido como: "defina o valor de exemplo para 1. Enquanto exemplo for menor ou igual a 10, mostre o valor de exemplo na tela e some 1 ao valor atual de exemplo."

# Como vimos, o loop while executa uma verificação a cada iteração da condição que o define. Nesse exemplo, a condição é 'exemplo <= 10'. Enquanto essa condição for verdadeira, o bloco de código dentro do loop será executado.

# Note como precisamos de definir um contador para o loop while, do contrário, não haveria uma forma de sair dele, criando um loop infinito. Observe:

exemplo2 = 1 # contador
while exemplo2 <= 10:
    print(exemplo2)
    # nesse loop não existe a modificação do valor do contador, o que significa que a condição 'exemplo <= 10' será sempre verdadeira, criando um loop que não acaba(infinito)


# Loops infinitos, normalmente, são um problema na aplicação, porém às vezes necessários. É importante que, se tratando do loop while, seja definida uma condição de parada e que o contador vá em direção à tal condição.

# Portanto, temos que a forma geral de um loop while é:

# while <condição>:
    # bloco de código

# aonde o bloco de código é executado enquanto a condição for verdadeira(e é verificada a cada iteração).




# * Loop for:

# O loop for está intimamente ligado às estrutura de dados. Ele é uma puramente uma estrutura de repetição feita para iterar sobre alguma estrutura de dados. No caso, com while também é possível, porém seria mais complexo.

# Observe um exemplo de loop for:

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for elemento in lista1:
    print(elemento) # printa cada elemento da lista1

# No código acima, definimos uma lista, contendo uma lista numérica de 1 a 9. Logo em seguida, definimos um loop for. Esse loop define uma variável de nome qualquer, que nesse caso possui nome 'elemento'. A variável 'elemento' representa todos os elementos da estrutura de dados, que nesse caso é a lista 'lista1'. 'elemento' será igual a cada elemento dentro da lista, mudando para o próximo a cada iteração. Por exemplo, na primeira iteração 'elemento' tem como valor 1. Na segunda, 'elemento' tem como valor 2. Na terceira, 3. E por aí vai. Por fim, indicamos que vamos iterar sobre a lista 'lista1' com o comando 'in lista1'.

# O loop for dado como exemplo pode ser lido da seguinte forma: "para cada elemento da lista1, printe tal elemento".

# NOTA: Para utilizar o loop for, é preciso uma estrutura de dados qualquer, para iterar sobre ela. Mas para utilizar while, não é necessário ter uma estrutura de dados específica, o loop funciona por conta própria.




# * Comandos break e continue:

# Quando falamos de loops, temos dois comandos muito úteis: break e continue.

# -> break: esse comando define um ponto de parada para um loop, seja o loop for ou o loop while. Quando o interpretador ler o comando 'break', ele imediatamente para o loop(a qualquer custo) e vai para a próxima instrução após o loop(ou acaba o programa se não tiver nenhuma).

# -> continue: esse comando indica ao intepretador que pule a iteração atual e pule para a próxima.

# Eis um exemplo de cada comando:

# break:

b = 1
while b <= 10:
    if b == 5:
        break # para o loop quando b for 5
    print(b)
    b += 1

# no exemplo acima, o loop não completa as 10 iterações, porque definimos que quando b for 5, o loop quebrará.


# continue:

for i in range(1, 11):
    if i == 5:
        continue # pula para a próxima iteração não deixando o comando print(5) acontecer
    print(i)

# no exemplo acima, o número 5 não é printado no console, porque definimos que quando i for 5 o loop irá pular para a próxima iteração.
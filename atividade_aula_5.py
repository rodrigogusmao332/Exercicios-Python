"""
#QUESTÃO 1
print('Adicione dois números para ver qual o maior')
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

if numero1 > numero2:
    print('número 1 é o maior')
elif numero1 == numero2:
    print('São iguais')
else:
    print('Número dois é maior')
________________________________________________________________________________________________________________________

#QUESTÃO 2
print('Leia um número real para ser extraído a raiz quadrada')
numero = float(input('O número é: '))

if numero <= -1:
    print('numero inválido')
else:
    print(numero ** 0.5)

________________________________________________________________________________________________________________________

#QUESTÃO 3

print('Leia um número real')
numero = int()

if numero >= 1:
    print(numero**0.5)
else:
    print(numero**2)

________________________________________________________________________________________________________________________
#Questão 4

print('Faça um programa que leia um numero')
numero = int(25)

if numero >= 1:
    print((numero**2)**0.5)
________________________________________________________________________________________________________________________
#QUESTÃO 5

print('Numero par ou impar')
numero = int(6)

if numero % 2 == 0:
    print('par')
else:
    print('impar')

________________________________________________________________________________________________________________________
#QUESTÃO 6

#Questão 6

print('Adicione dois números para ver qual o maior')
numero1 = int(input('Número 1: '))
numero2 = int(input('Número 2: '))

if numero1 > numero2:
    print('número 1 é o maior')
elif numero1 == numero2:
    print('São iguais')
else:
    print('Número dois é maior')

if numero1 > numero2:
    print(f'A diferença é {numero1-numero2}')
if numero2 > numero1:
    print(f'A diferença é {numero2-numero1}')



________________________________________________________________________________________________________________________
#QUESTÃO 8

print('Notas do Aluno')
nota = float(input())
nota2 = float(input())

if nota > 10.0:
    print(f'{nota}nota inválida')
elif nota2 > 10.0:
    print(f'{nota2}nota inválida')
elif nota < 0.0:
    print(f'{nota}Nota inválida')
elif nota2 < 0.0:
    print(f'{nota2}Nota inválida')
else:
    print(f'Nota 1: {nota} e nota 2: {nota2}')
____
________________________________________________________________________________________________________________________

#Questão 9
print('Leia a prestação de um salário de um trabalhador')
salario = float(input('Salário em reais é igual a:'))
emprestimo = float(input('Empréstimo é: '))

if emprestimo > (0.2*salario):
    print('Empréstimo não concedido')
else:
    print('Emprestimo concedido')

________________________________________________________________________________________________________________________
#Questãodd peso ideal')
altura = float(input('Altura em m é igual a: '))
sexo = str(input('Sexo: '))
mulher = (62.1 * altura) - 58
homem = (72.7 * altura) - 44.7

if sexo == 'mulher':
    print(f'peso ideal é {mulher}')
if sexo == 'homem':
    print(f'Peso ideal é {homem}')
________________________________________________________________________________________________________________________

#Questão 11

print('Adicione o número para ser somado')
numero = int(input('Número de 10 a 9999: '))
a = str(numero)

if numero <= 9:
    print('Numero inválido')
elif len (a) == 2:
    uni = int(a[0])
    dez = int(a[1])
    soma = dez + uni
    print(f'O numero é {soma}  ')
elif len (a) == 3:
    uni = int(a[0])
    dez = int(a[1])
    cen = int(a[2])
    soma = uni + dez + cen
    print(f'O numero é {soma}')



________________________________________________________________________________________________________________________
#Questão 12
print('Calculando logaritmos')
numero = int(input())

if numero <= 0:
    print('Número inválido')
else:
    from math import log
    log = log(2, numero)
    print(f'O lagaritmo é {log}')


________________________________________________________________________________________________________________________

#Questão 13
print('Média das provas')
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

notaf1 = nota1 * 1
notaf2 = nota2 * 2
notaf3 = nota3 * 2

media = (notaf1 + notaf2 + notaf3)/5
print(f'A média é : {media}')

if media >= 60:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')

________________________________________________________________________________________________________________________

#Questão 15

print('Dias da semana, escolha um numero entre 1 e 7')
numero = int(input())

if numero == 1:
    print('domingo')
elif numero == 2:
    print('segunda')
elif numero == 3:
    print('terça')
elif numero == 4:
    print('quarta')
elif numero == 5:
    print('quinta')
elif numero == 6:
    print('sexta')
elif numero == 7:
    print('sábado')
else:
    print('número inválido')

________________________________________________________________________________________________________________________
#Questão 17

print('Calculando a área de um trapézio')
basemenor = float(input('Adicione o valor da base menor: '))
basemaior = float(input('Adicione o valor da base maior: '))
altura = float(input('Adicione valor da altura: '))

if basemaior == 0:
    print('Erro')
elif basemenor == 0:
    print('Erro')
else:
    area = (((basemenor + basemaior) * altura)/2 )
    print(f' A área do trapézio é igual a {area} cm2')

________________________________________________________________________________________________________________________

#Questão 18

print('Adicione a operação a ser feita')
operacao = int(input('Adicione [1] para soma, [2] para subtracao, [3] para divisao e [4] para multiplicacao: '))

while operacao <1 or operacao >4:
    print('Valor desconhecido, adicione números de 1 a 4 para fazer as operações')
    operacao = int(input('Adicione [1] para soma, [2] para subtracao, [3] para divisao e [4] para multiplicacao: '))


numero1 = int(input('Adicione numero inteiro: '))
numero2 = int(input('Adicione numero inteiro: '))

if operacao == 1:
    print(f'Soma escolhida, a soma dos números é {numero1 + numero2}')
if operacao == 2:
    print(f'Subtração escolhida, a subtração dos números é {numero1 - numero2}')
if operacao == 3:
    print(f'Divisão escolhida, a divisão é {numero1 / numero2} ')
if operacao == 4:
    print(f'Multiplicação escolhida, a multiplicação é {numero1 * numero2}')

________________________________________________________________________________________________________________________
#Questão 19

print('O número é divisível por 3 e 5 simultaneamente?')
numero = int(input())

if numero % 5 == 0 and numero % 3 == 0:
    print('Inválido')
else:
    print('Válido')
________________________________________________________________________________________________________________________
#Questão 20

print('Determine a classificação do triangulo')
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print('O triângulo é Equilátero')
if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('O triângulo é escaleno')
if lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 != lado3 == lado2 or lado3 == lado1 != lado2:
    print('O triângulo é Isósceles')
________________________________________________________________________________________________________________________
#Questão 21

print('Escolha as operações')
operacao = int(input('Escolha para somar [1], para subtrair [2], para dividir [3] e para multiplicar [4]: '))

while operacao  <1 or operacao >4:
    print('Escolha a operação, [1] para somar, [2] para subtrair, [3] para dividir, [4] para multiplicar')
    operacao = int(input('Escolha para somar [1], para subtrair [2], para dividir [3] e para multiplicar [4]: '))

num1 = int(input())
num2 = int(input())

if operacao == 1:
    print(f'A operação escolhida foi somar, logo o resultado é {num1 + num2}')
if operacao == 2:
    print(f'A operação escolhida foi subtração, logo o resultado é {num1 - num2}')
if operacao == 3:
    print(f'A operação escolhida foi divisão, logo o resultado é {num1 / num2}')
    if num2 == 0:
        print('Valor inválido')
if operacao == 4:

    print(f'A operação escolhida foi multiplicação, logo o resultado é {num1 * num2}')
________________________________________________________________________________________________________________________
#Questão 22
print('Pode se aposentar ou não?')
idade = int(input('Idade: '))
tempo = int(input('Tempo de trabalho: '))

if idade >= 65 or tempo >= 30:
    print('Aposentadoria aceita ')
if idade <= 60 and tempo <25:
    print('Aposentadoria negada')
if idade >= 60 and tempo >= 25:
    print('Aposentadoria aceita')
if idade < 50 and tempo < 30:
    print('Aposentadoria negada')
________________________________________________________________________________________________________________________

#Questão 23

print('Determinando se o ano é bissexto')
ano = int(input())

if ano % 4 == 0 and ano % 100 != 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

________________________________________________________________________________________________________________________
#Questão 24

print('Imposto do produto X nos estados')
estado = int(input('Adicione número correspondente ao estado, sendo RJ[1], SP[2], MG[3], MS[4]: '))

produto = float(input('Adicione o preço do produto: '))

if estado == 1:
    imposto1 = produto * 0.07
    print(f'O estado é minas gerias o imposto é {imposto1}, sendo o valor total do produto {imposto1 + produto}')
if estado == 2:
    imposto2 = produto * 0.12
    print(f'O Estado é São Paulo, o imposto é {imposto2}, sendo o valor total do produto {imposto2 + produto}')
if estado ==3:
    imposto3 = produto * 0.15
    print(f'O Estado é Rio de Janeiro, o imposto é {imposto3}, sendo o valor total do produto {imposto3 + produto}')
if estado ==4:
    imposto4 = produto * 0.08
    print(f'O Estado é Mato Grosso, o imposto é {imposto4}, sendo o valor total do produto {imposto4 + produto}')
else:
    print('erro')

________________________________________________________________________________________________________________________
#QUESTÃO 25

print('Calcule as raízes de 2º')
a = int(input('Adicione valor de a: '))
b = int(input('Adicione valor de b: '))
c = int(input('Adicione valor de c: '))

delta = b**2 - 4 * a * c
print(delta)

valorx = (-b + delta**0.5) / 2
valory = (-b - delta**0.5) / 2


if delta < 0:
    print('Não existe raíz')
if delta == 0:
    print(f'Raíz única, a raíz é {valory}')
if delta > 0:
    print(f'Duas raízes, são {valory} e {valorx}')

________________________________________________________________________________________________________________________
#QUESTÃO 41

print('IMC - Índice de Massa Corporal')
peso = float(input('Adicione o peso em kgs: '))
altura = float(input('Adicione altura em m: '))

imc = peso / altura**2
print(imc)

if imc < 18.5:
    print(f'Abaixo do peso')
elif imc >= 18.6 and imc <= 24.9:
    print(f'Saudável')
elif imc >= 25.0 and imc <= 29.9:
    print(f'Peso em excesso')
elif imc >= 30.0 and imc <= 34.9:
    print(f'Obesidade Grau I')
elif imc >= 35.0 and imc <= 39.9:
    print(f'Obesidade Grau II')
elif imc > 40.0:
    print(f'Obesidade Grau III (mórbida)')

________________________________________________________________________________________________________________________

"""
print('Imposto do produto X nos estados')
estado = int(input('Adicione número correspondente ao estado, sendo RJ[1], SP[2], MG[3], MS[4]: '))

produto = float(input('Adicione o preço do produto: '))

if estado == 1:
    imposto1 = produto * 0.07
    print(f'O estado é minas gerias o imposto é {imposto1}, sendo o valor total do produto {imposto1 + produto}')
if estado == 2:
    imposto2 = produto * 0.12
    print(f'O Estado é São Paulo, o imposto é {imposto2}, sendo o valor total do produto {imposto2 + produto}')
if estado ==3:
    imposto3 = produto * 0.15
    print(f'O Estado é Rio de Janeiro, o imposto é {imposto3}, sendo o valor total do produto {imposto3 + produto}')
if estado ==4:
    imposto4 = produto * 0.08
    print(f'O Estado é Mato Grosso, o imposto é {imposto4}, sendo o valor total do produto {imposto4 + produto}')
else:
    print('erro')

#Questão 1: Faça um programa que leia um número inteiro e imprima:

print('Imprima um número inteiro')
numero = int(input('o numero inteiro é: '))
print(f'o numero inteiro é {numero} ')

#Questão 2

real = 200
print(real)

#Questão 3: Peça o usuário que imprima três valores e em seguida a soma deles:

print('Digite tres valores inteiros')

valor1 = int(input(''))
valor2 = int(input(''))
valor3 = int(input(''))
soma = valor1 + valor2 + valor3

print(f'o resultado da soma é {soma}')


#Questão 4

real1 = 100
print(real1)

real1 = real1 ^ 2
print(real1)

#Questão 5

real2 = 20
print(real2)

real2 = real2 / 5
print(real2)



#Questão 6: Leia a temperatua em graus Fahrenheit e apresente convertida em C:

print('Ponha o valor e ele sera convertido automaticamente em ºF')
tempc = float(input('temperatura em celsius: '))
tempf = float(tempc * (9/5) + 32)
print(f'A temperatura em graus  é {tempf} ºF')



#Questão 7: Leia a temperatua em graus Fahrenheit e apresente convertida em C:

print('Coloque o valor em graus Fahrenheit e ele será automaticamente convertido em Celsius')
tempf = float(input('Temperatura em F:'))
tempc = float(5 * (tempf - 32) / 9)
print(f'A temperatura em C é {tempc}')



#Questão 9: Leia uma temperatura em graus Kevin e a converta em graus celsius:

print('Adicione um valor em graus Kelvin e ele será convertido em graus Celsius')
tempk = float(input('A temperatura em graus Kelvin é: '))
tempc = float(tempk - 273.15)
print(f'A temperatura em graus celsius é {tempc}')



#Questão 10: Leia a velocidade em Km/h e apresente em m/s.

print('Adicione um número e ele será convertido de km/h para m/s')
velkm = float(input('A velocidade em Km/h é: '))
velms = float(velkm/3.6)
print(f'A velocididade em m/s é {velms}')


#Questão 16: Leia um valor com comprimento em polegadas e o apresente em centímetros:

print('Apresente o valor com comprimento em polegadas para a conversão em centímetros')
polegadas = float(input('Comprimento em polegadas é: '))
centimetros = float(polegadas * 2.54)

print(f'O comprimento em polegadas são {centimetros} cms')



#QUESTÃO 28: Faça a leitura de três numeros e faça a soma dos quadrados

print('Adicione 3 valores para obtermos a soma dos quadrados dos três valores lidos')
valor1 = int(input('o valor é: '))
valor2 = int(input('o valor é: '))
valor3 = int(input('o valor é: '))
soma = valor1 + valor2 + valor3
total = soma**2

print(f'A soma dos quadrados é: {total}')



#QUESTÃO 29: Leia 4 notas, calcule a média aritmetica e imprima o resultado:

print('Adicione 4 notas para obter resultado da média aritmética')
nota1 = float(input('A nota do primeiro bismestre é: '))
nota2 = float(input('A nota do segundo bismestre é: '))
nota3 = float(input('A nota do terceiro bismestre é: '))
nota4 = float(input('A nota do quarto bismestre é: '))
soma = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média do aluno é {soma} ')

if soma >= 7:
    print('Aprovado')
else:
    print('reprovado')



#QUESTÃO 30: Transforme um valor de Real para dolar.

print('Adicione o valor em Real e obtenha o valor correspondente em Dólar')
real = float(input('O valor em real é: '))
dolar = float(real * 0.19)

print(f'O valor em dólar é a {dolar}')



#QUESTÃO 31: Leia um número inteiro e escreva seu sucessor e antecessor:

print('Adicione um número inteiro para ver seu antecessor e sucessor')
numero = int(input('O numero inteiro é:'))
sucessor = int(numero + 1)
antecessor = int(numero - 1)

print(f'O antecessor é igual a {antecessor} e o sucessor é {sucessor}')



#QUESTÃO 32: Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro:

print('Adicione um número inteiro')
numero = int(input('Esse é o número inteiro: '))
sucessor = int(numero + 1)
antecessor = int(numero - 1)
soma = (sucessor * 3 + antecessor *2)

print(f'Esse é a {soma}: ')


#Questão 33: Leia o tamanho do lado de um quadrado e consiga sua área:

print('Adicione o tamanho do lado do quadrado:')
lado = int(input('Esse é o lado do quadrado em cm: '))
area = int(lado * lado)

print(f'A área de um quadrado é igual a {area} m2')

#QUESTÃO 34
print('Calcule a área de um círculo')
raio = float(input('O raio do círculo é igual a:'))
area = float(3.14 * raio**2)

print(f'A área do círculo é equivalente a {area} cm2')


#QUESTÃO 38: Leia o salário de um funcionário. Calcule e imprima o valor de um novo salário, sabendo que ele recebeu
#aumento de 25%

print('Adicione o valor do salário de um funcionário')
salario = float(input('O valor de um salário de um funcionário é: '))
ajuste = float(salario / 100 * 25)
novo = salario + ajuste

print(f'O novo salário do funcionário ajustado é de {novo} reais')


#QUESTÃO 39

total = 780000

p1 = 0.42
p2 = 0.38
p3 = 1 - (p1 + p2)

print(f'Jogador 1 receberá {p1 * total}')
print(f'Jogador 2 receberá {p2 * total}')
print(f'Jogador 3 receberá {p3 * total}')

total2 = p1 + p2 + p3
print(total2)


#QUESTÃO 40

print('Quantidade de dias que o encanador trabalhará')
dias = int(input('O encanador trabalhará '))
valor = int(dias * 30)
desconto = int(valor * 0.08)
liquido = int(valor - desconto)

print(f'O trabalhador receberá um valor líquido de {liquido} reais')


#QUESTÃO 41

print('Cálculo do valor-hora de trabalho')
hora = float(input(('O trabalhador teve carga horária no mês de: ')))
valor = float(input('O valor em reais da hora de trabalho é de: '))
total = hora * valor
total2 = total * 0.10
salario = total + total2

print(f'O trabalhador receberá igual a {salario} reais')



#Questão 42

print('Receba o salário-base de um funcionário')
salario = float(input('O salário total em reais é de: '))
gratificacao = float(salario * 0.05)
desconto = float(salario * 0.07)
salario2 = salario - desconto + gratificacao

print(f'O salario-base do trabalhador é {salario2} reais')


#QUESTA0 44

print('A partir de um total lido')
total = float(input('O valor total em reais é de: '))
desconto = total * 0.10
parcelas = total / 3
comissao1 = (total - desconto) * 0.05
comissao2 = total * 0.05

print(f'O desconto À vista é de {desconto}, as parcelas são de {parcelas}')
print(f'A comissão a vista é de {comissao1} e parcelada é de {comissao2}')



#QUESTÃO 46

numero = input('informe numero entre 100 e 999')

while len(numero) !=3 :
    numero = input('informe numero entre 100 e 999')

print(numero[::-1])




#QUESTÃO 47

numero = input('Leia um numero de 1000 a 9999: ')

print(str(numero[0]))
print(str(numero[1]))
print(str(numero[2]))
print(str(numero[3]))




#QUESTÃO 48

print('Escreva segundos para imprimir em horas, minutos e segundos')
segundos = float(input('Adicione os segundos: '))
minutos = segundos/60
horas = segundos/3600

print(f'São {horas}, {minutos}, {segundos} ')


# Exercicio 49

segundos = int(input('Favor informar a hora inicial em segundos '))

horas = int(segundos / 3600)

segundos_rest = segundos % 3600

minutos = int(segundos_rest / 60)

segundos_final = segundos_rest % 60

print(f'O tempo inicial é {horas} horas, {minutos} minutos e {segundos_final} segundos')

segundos_duracao = int(input('Favor informar o tempo de duração em segundos '))

horas_duracao = int(segundos_duracao / 3600)

segundos_rest_duracao = segundos_duracao % 3600

minutos_duracao = int(segundos_rest_duracao / 60)

segundos_final_duracao = segundos_rest_duracao % 60

horas_final = horas_duracao + horas

minutos_final = minutos + minutos_duracao

segundos_finalmente = segundos_final + segundos_final_duracao

print(f'O tempo final é {horas_final} horas, {minutos_final} minutos e {segundos_finalmente} segundos')


#Questão 50

print('Ano de nascimento a partir da data atual')
idade = int(input('Adicione idade: '))
ano_atual = int(2021)
ano_de_nascimento = ano_atual - idade

print(f'O ano de nascimento é igual a: {ano_de_nascimento}')


#Questão 51

print('Calcular a distância entre dois pontos (0,0)')
x1 = float(input('Adicione o valor de x1: '))
x2 = float(input('Adicione o valor de x2: '))
y1 = float(input('Adicione o valor de y1: '))
y2 = float(input('Adicione o valor de y2: '))
R = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'O valor das coordenada é igual a: {R} ')



#QUESTÃO 52

print('Faça o cálculo da loteria')
premio = float(input('O premio total da loteria foi de:'))

investimento1 = float(input('Adicione o investimento do jogador 1: '))
investimento2 = float(input('Adicione o investimento do jogador 2: '))
investimento3 = float(input('Adicione o investimento do jogador 3: '))
investimento4 = float(input('Adicione o investimento do jogador 4: '))
aposta_total = investimento1 + investimento2 + investimento3 + investimento4

porcentagem1 = investimento1 / aposta_total
porcentagem2 = investimento2 / aposta_total
porcentagem3 = investimento3 / aposta_total
porcentagem4 = investimento4 / aposta_total

premio1 = porcentagem1 * premio
premio2 = porcentagem2 * premio
premio3 = porcentagem3 * premio
premio4 = porcentagem4 * premio

print(f'O prêmio do jogador 1 é {premio1}')
print(f'O prêmio do jogador 2 é {premio2}')
print(f'O prêmio do jogador 3 é {premio3}')
print(f'O prêmio do jogador 4 é {premio4}')


#QUESTÃO 53

print('Medindo as dimensões de um terreno')
comprimento = float(input('O comprimento do terreno é igual a: '))
largura = float(input('A largura do terreno é igual a: '))
dimensao = largura * comprimento

tela_preco = 20
custo = dimensao**0.5 * 20

print(f'O custo da tela por m é de {custo}')





"""
#Aula dia 27/03

print('Ola Mundo')

divida = 0
compra = 100

divida = divida + compra
print(divida)
compra = 200
divida = divida + compra
print(divida)
compra = 300
divida = divida + compra
compra = 0

print(divida)



x = input("Digite um número: ")
print(x)

nome = input ("Digite seu nome: ")
print("Voce digitou %s" %nome)
print("Olá, %s!" %nome)




anos = int(input("Anos de serviço: "))
valor_por_ano=float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print("Bonus de R$%5.2f" %bonus)




numero1 = int(input ("Digite um numero: "))
numero2 = int(input ("Digite um numero: "))
soma = (numero1 + numero2)
print(soma)




if numero1 > numero2:
    print("Uau, o primeiro numero é maior")

if numero1 < numero2:
    print("Uau, o segundo numero é maior")




velocidade= int(input("Qual a velocidade que o carro passou pelo local? "))
if velocidade > 80:
    print("Voce tera que pagar uma multa no valor situado em: ")
    print(5*(velocidade -80 ))



idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")
    
    
    
minutos = int(input("Quantos minutos voce utilizou esse mes: "))
if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print("Você vai pagar este mês:R$%6.2f"  % (minutos * preço))



x= 1
while x <= 5:
    print(x)
    x = x + 1


x = 10
while x >= 1:
    print(x)
    x = x - 1

print("F O O G O ! ! !" )




fim = int(input("Digite o ultimo numero a imprimir: "))

x = 1 #se quizer numeros impares
x = 0 #se quiser numeros pares
while x <= fim:
    print(x)
    x = x + 2 #quantidade de numeros que pulam

"""
"""
pontos = 0
questão = 1
questão = questão + 1 
while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão)
if questão == 1 and resposta == "b":
    pontos = pontos + 1
if questão == 2 and resposta == "a":
    pontos = pontos + 1
if questão == 3 and resposta == "d":
    pontos = pontos + 1
questão +=1
print("O aluno fez %d ponto(s)" % pontos)

"""


n = 1
soma = 0

while n<=10:
    x = int(input("Digite o %d numero: " %n))
    soma = soma + x
    n = n + 1

print("Soma: %d " %soma)



x = 1
soma = 0 
while x <= 4:
    n = int(input("%d Digite o número:" % x))
    soma = soma + n 
    x = x + 1
print("Média: %5.2f" % (soma/5)) 



s= 0
while True:
    v= int(input("Digite um numero a somar ou 0 para sair: "))
    if v == 0:
        break
    s= s+v
print(s)

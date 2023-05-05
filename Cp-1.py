#RM98603 - David Guilherme B. Denunci

print("Seja Bem-vindo!")

print('''
''')

nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))

idade1 = 18
if idade < 18:
    print("Você não pode continuar a sua compra, você deve ser maior de 18 anos.")
    print("Compra finalizada! ")
    exit()
else:
    end_do_cliente = input("Digite seu endereço: ")
    end_de_entrega = input("Digite aqui o endereço de entrega: ")


print('''
    ''')


vinho1 = "Vinho uva roxa (R$20,00). "
vinho2 = "Vinho uva verde (R$35,00). "
vinho3 = "Vinho seco (R$50,00). "
vinho4 = "Vinho branco (R$ 80,00). "
vinho5 = "Vinho molhado (R$45,00). "

print("Nós temos uma diversidade de ótimos vinhos! Dê uma olhada: ")
print(vinho1 )
print(vinho2 )
print(vinho3 )
print(vinho4 )
print(vinho5 )


vinhos1 = 20
vinhos2 = 35
vinhos3 = 50
vinhos4 = 80
vinhos5 = 45

print('''
''')
quantidade = int(input("Quantos vinhos você irá comprar? "))
tipos1 = (int(input("Você deseja adicionar quantos Vinhos de uva roxa ao seu carrinho? ")))
print(vinho1)
soma1 = (vinhos1 * tipos1)
print(str(soma1) + " reais")

tipos2 = (int(input("Você deseja adicionar quantos Vinhos de uva verde ao seu carrinho? ")))
print(vinho2)
soma2 = (vinhos2 * tipos2)
print(str(soma2) + " reais")

tipos3 = (int(input("Você deseja adicionar quantos Vinhos seco ao seu carrinho? ")))
print(vinho3)
soma3 = (vinhos3 * tipos3)
print(str(soma3)+ " reais")

tipos4 = (int(input("Você deseja adicionar quantos Vinhos branco ao seu carrinho? ")))
print(vinho4)
soma4 = (vinhos4 * tipos4)
print(str(soma4) + " reais")

tipos5 = (int(input("Você deseja adicionar quantos Vinhos molhado ao seu carrinho? ")))
print(vinho5)
soma5 = (vinhos5 * tipos5)
print(str(soma5) + " reais")


soma_total = (soma1 + soma2 + soma3 + soma4 + soma5)
print(float(soma_total))

if soma_total < 100:
    print("Valor mínimo de compra é R$100,00. Por favor selecione mais produtos.")
    print(input("Para continuar comprando pressione a tecla 'enter'. "))

tipos6 = (int(input("Você deseja adicionar quantos Vinhos de uva roxa ao seu carrinho? ")))
print(vinho1)
soma6 = (vinhos1 * tipos6)
print(str(soma6) + " reais")

tipos7 = (int(input("Você deseja adicionar quantos Vinhos de uva verde ao seu carrinho? ")))
print(vinho2)
soma7 = (vinhos2 * tipos7)
print(str(soma7) + " reais")

tipos8 = (int(input("Você deseja adicionar quantos Vinhos seco ao seu carrinho? ")))
print(vinho3)
soma8 = (vinhos3 * tipos8)
print(str(soma8) + " reais")

tipos9 = (int(input("Você deseja adicionar quantos Vinhos branco ao seu carrinho? ")))
print(vinho4)
soma9 = (vinhos4 * tipos9)
print(str(soma9) + " reais")

tipos10 = (int(input("Você deseja adicionar quantos Vinhos molhado ao seu carrinho? ")))
print(vinho5)
soma10 = (vinhos5 * tipos10)
print(str(soma10) + " reais")

print('''
''')

soma_total1 = (soma6 + soma7 + soma8 + soma9 + soma10)
soma_total_total = soma_total1 + soma_total
print("O valor do seu carrinho é de " + str(soma_total_total ) + " reais.")


if soma_total_total > 200:
    print("Parabéns, você ganhou frete grátis!")
    print('''
        ''')
else:
    print("O frete será de R$ 15,00")


print('''
    ''')
    
print("O valor total da sua compra é de: " + str(soma_total_total) + " reais.")

print('''
    ''')
quantidade_p = (tipos1 + tipos2 + tipos3 + tipos4 + tipos5 + tipos6 + tipos7 + tipos8 + tipos9 + tipos10)
print((str(quantidade_p) + " produtos comprados."))

print('''
    ''')
    
print("Será entregue no endereço: " + str(end_de_entrega))
print("Obrigado pela preferência!")




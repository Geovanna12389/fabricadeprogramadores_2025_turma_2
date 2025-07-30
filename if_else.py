'''
saldo= int( input("digite o saldo bancário"))
saque= int( input("digite o valor de saque"))
if saldo >= saque:
    saldo -= saque
    print("voce realizou um saque com sucesso.",saldo)
else:
    print("voce nao possui saldo suficiente para realizar essa operaçao.",saldo)  

nome = (input("digite o nome do aluno: "))
nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
media =(nota1+nota2)/2
if media >= 6 and media <= 7:
    print("o aluno", nome, "foi aprovado com a nota ", media)
elif media >= 8:
    print("o aluno",nome, "foi aprovado com louvor com a nota", media)
else: 
'''
valor_parte = float(input("insira o valor parte: "))
porcentagem = float(input("insira o valor da porcentagem: "))
valor_total = valor_parte * (porcentagem/100)
if porcentagem <=0.0:
    print("insira um numero maior que 0")
else:
    print(valor_total)
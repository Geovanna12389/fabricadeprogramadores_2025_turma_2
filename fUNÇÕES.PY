'''
texto_escrito="este livro é legal!"
outro_texto='vou aprender a programar'
texto="""
primeira linha 
segunda linha
terceira linha
"""
print(texto)
print("\toi!\neu me chamo \"(geovanna)\"!!!")
outro_texto=texto_escrito 
print(outro_texto)
fatias_bolo=30
quantidade_subtraidas=10
fatias_bolo-=quantidade_subtraidas
print(fatias_bolo) 
carteira_digital=0
print(carteira_digital)
carteira_digital+=100
print(carteira_digital)
carteira_digital-=75.99
print(carteira_digital)
carteira_digital+=200
print(carteira_digital)
print("oiii")
print('calara')
print("geovanna")
print("hello")
"""
 um comentario, dentro
  de um outro
  comentario
 """
def dizer_ola( nome_usuario="calara"):
    print("ola", nome_usuario)
dizer_ola("geovanna")
dizer_ola()
def dizer( nome_usuario):
    print("ola",nome_usuario)
dizer_ola("geovanna")
dizer_ola("zebra")
dizer_ola(1000)
nome = input("insira seu nome: ")
saudacao = "olá "+nome
print(saudacao)
nome = int(input("insira um numero:"))
saudacao = nome - 2
print(saudacao)
numero = 3
def apresentar_numero():
    numero = 2
    print(numero)
apresentar_numero()
print(numero)
numero = 9
def apresentar_numero():
    global numero
    print(numero)
    numero = 23
    print(numero)
apresentar_numero()
print(numero)
'''
def quadrado(area):
    resultado = area **2
    return resultado
print(quadrado(4))

def salario(valor):
    resultado = valor + valor * 0.15
    return resultado
print(salario(100000)) 

def triangulo(base, altura):
    resultado = base * altura / 2
    print(triangulo(6,2)) 

def temperatura(celsius):
    fahrenheit = (9*celsius+160)/5
    return fahrenheit
print(temperatura(100))

def valores(x,y):
    z=x
    x=y
    y=z 
    return ("o valor de x é:",x,
             "e o valor de y é:",y)
print(valores(100,40))

def paralelepipedo(base, largura, altura):
    resultado = base * altura * largura
    return resultado 
print(paralelepipedo(6,10,20)) 
    
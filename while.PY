'''
x = 1 
while x <= 100:
    print(x)
    x = x + 1

x = 50
while x <= 100:
    print(x)
    x = x + 1

def exercicio_3():
    x = 10
    while x >= 0:
        print(x)
        x = x + -1
    print('fogo!')
exercicio_3()

def números_pares():
    fim=int(input("digite o último número a imprimir:"))
    x = 0 
    while x <= fim:
        if x % 2 == 0:
            print(x)
        x = x + 1
números_pares()

def números_impares():
    fim = 9
    x = 0 
    while x <= fim:
        if x % 2 == 0:
            print()
        else:
            print(x)    
        x = x + 1
números_impares()
'''
def arvore_de_natal():
    linha = 1
    while linha <= 10:
        coluna = 1
        while coluna <= linha:
            print('💚', end="")
            print('🤍', end="")
            print('❤️', end="")
            coluna = coluna + 1
        print()
        linha = linha + 1
arvore_de_natal()
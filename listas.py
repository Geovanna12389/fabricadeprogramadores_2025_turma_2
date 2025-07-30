import math

def equaçao():
    a = float(input("insira o valor de a:"))
    b = float(input("insira o valor de b:"))
    c = float(input("insira o valor de c:"))
    delta = b**2 - 4 * a * c 
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / 2 * a
        raiz2 = (-b - math.sqrt(delta)) / 2 * a     
        print("as raizes reais sao: ",raiz1, raiz2)  
    else:
        print('''essa equaçao nao possui raízes reais''')
#equaçao()

import random
numero_aleatorio = random.randint(0,10)
#print(numero_aleatorio)

import random 
cesta = ['roxo', 'rosa', 'amarelo', 'azul', 'laranja', 'verde', 'vermelho', 'preto', 'branco', 'magenta']
print(random.choice(cesta)) 
import time 
#print(time.asctime())
import turtle 

turtle.circle(-50)
#turtle.getscreen()._root.mainloop()
import this 
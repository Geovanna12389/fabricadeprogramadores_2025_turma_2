def raça_atendimento():
    valor_total = 0
raças = ['pug', 'pastor-alemão', 'labrador']
raça = input('insira uma raça:')
if (raça in raças):

    if (raça == 'pug'):
        valor_total =+ 70.99
    print("atendimento disponivel, pelo valor de:" ,valor_total )
elif (raça == 'pasto-alemão'):
    valor_total =+ 120.99
    print("atendimento disponivel, pelo valor de:" ,valor_total )
elif (raça == 'labrador'):
    valor_total =+ 110.99 
    print("atendimento disponivel, pelo valor de:" ,valor_total )
else:
    print("o atendimento não está disponivel")

'''
print(raças[0])
print(raças[1])
print('labrador' in raças)
'''
'''
l = [8,9,15]
for e in l:
    print(e)

l = ["rosa", "girassóis", "lírios", "orquídeas", "tulipas","margaridas" , "astromélias", "gérberas", "violetas", "dália"]
for s in l:
    for letra in s:
        print(letra)

def exibe_maior():
    l = [1,7,2,4]
    máximo = l[0]
    for e in l:
        if e > máximo:
            máximo = e
            print(máximo)

def exibe_menor():
    l = [1,7,2,4]
    minímo= l[0]
    for e in l:
        if e < minímo:
            minímo = e
            print(minímo)

def range_exemplo():
    for v in range(10):
        print(v)
range_exemplo()

def range_inicio_fim():
    for v in range(5,8):
        print(v)
range_inicio_fim()

def range_salto():
    for t in range(3,33,3):
        print(t,end=" ")
range_salto()
'''

nome = "geovanna"
idade = 15
grana = 51.34
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
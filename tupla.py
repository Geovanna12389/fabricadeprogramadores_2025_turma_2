#tupla = ("data de nascimento", "cpf","")
L = [0,2,4,8,10,12,14,16,18,20 ]
for x, e in enumerate(L):
    print("2 x %d = %d" % (x,e))
    for x, e in enumerate(L):
        #print("[%d] %d" (x,e))
        print("[%d] x %d = %d" % (x, e, x*e))
    for x, e in enumerate(L):
        print("[%d] + %d = %d" % (x, e, x+e))
    for x, e in enumerate(L):
        print("[%d] - %d = %d" % (x, e, x-e))
    for x, e in enumerate(L):
        print("[%d] / %d = %d" % (x, e, x/e))
   
        
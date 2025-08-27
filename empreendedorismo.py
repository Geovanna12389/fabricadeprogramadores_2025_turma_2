estoque={   "ração cachorro": [ 1000, 25.30],
            "ração gato": [ 1000, 35.45],
			"ração aves": [ 1000, 19.20],
			"ração roedores": [ 1000, 25.50], 
            "ração peixes": [1000, 12.00],
            "coleiras":[400, 20.00],
            "camas e casinhas":[7000, 400.00],
            "roupinhas":[2000, 29.90],
            "bebedouros e comedouros":[90, 10.99],
            "brinquedos":[456, 15.25],
            "shampoos":[4000, 60.00],
            "condicionador":[4000, 65.00],
            "perfumes":[50, 12.00],
            "tapetes hingienicoos":[6000, 54.00],
            "areia sanitária para gatos":[7000, 70.00],
            "cortador de unha p/cães e gatos":[90, 9.80],
            "remédios contra pulgas e carrapatos":[9000, 90.00],
            "sachês naturais":[90, 15.99],
            "sachês para gatos":[90, 12.99],
            "sachês para cães":[90, 12.99], }
produto = input("digite o produto selecionado: "),
quantidade = int(input("digite a quantidade: "))
venda = [ [produto, quantidade]]
total = 0
if produto in estoque:
  print("Vendas:\n")
  for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
    print("não temos este produto no estoque!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
estoque = {
    "Tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}
venda = [["tomate", 5], ["batata", 10], ["alface", 5]]
total = 0
print("Vendas: \n")
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade, preco, custo))
    estoque[produto][0]  -= quantidade
    total = total + custo
print(" Custo total: %21.2f\n " % total)
print("Estoque: \n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantiade: ", dados[0])
    print("Preco: %6.2f\n" % dados[1])
compras = [ ]
while True:
    produto = input("Produto: ")
    if produto == "FIM":
        break
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preco: "))
    compras.append([produto, quantidade, preco])
soma = 0.0
for e in compras:
    print("%20s x%5d %5.2f %6.2f" % (e[0], e[1], e[2], e[1] * e[2]))
    soma = soma + e[1] * e[2]
print("total: %7.2f" % soma)

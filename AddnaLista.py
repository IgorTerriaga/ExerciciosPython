l = []
while True:
    n = int(input("Digite um numero (0 sair): "))
    if n == 0:
        break
    l.append(n)
x = 0
while x < len(l):
    print("Posicao %d: %d " % (x, l[x]))
    x = x + 1

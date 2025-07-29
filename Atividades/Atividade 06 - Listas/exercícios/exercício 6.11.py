L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)

print("\nElementos da lista:")
for e in L:
    print(e)
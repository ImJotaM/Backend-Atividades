T = [-10, -8, 0, 1, 2, 5, -2, -4]

menor = T[0]
maior = T[0]
soma = 0

for temperatura in T:
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
    soma += temperatura

media = soma / len(T)

print(f"A menor temperatura é: {menor}°C")
print(f"A maior temperatura é: {maior}°C")
print(f"A temperatura média é: {media:.2f}°C")
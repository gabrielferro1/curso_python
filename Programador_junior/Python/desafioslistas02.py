# Crie uma lista chamada numeros com 5 números inteiros diferentes.

numeros = [5, 10, 2, 3, 6, 7]

print("Lista de numeros:", numeros)

# Mostre na tela:
# O maior número da lista.
# O menor número da lista.
# A soma de todos os números da lista.
# A média dos números da lista.

maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
quantidade = len(numeros)
media = soma / quantidade

print("Maior numero:", maior)
print("Menor numero:", menor)
print("Soma dos numeros:", soma)
print("Media dos numeros:", media)

# Crie uma lista chamada nomes com 5 nomes (pode escolher os que quiser).
# Mostre todos os nomes, um por linha, usando um laço for.
# Depois, peça para o usuário digitar um nome.
# Se o nome estiver na lista, mostre:
"O nome aparece X vezes na lista."
# (use .count() para contar).
# Caso contrário, mostre:
"Esse nome não está na lista."

names = ['ana', 'gabriel', 'maria', 'joyce', 'gabriel']

print("Name's list")
for name in names:
    print(name)

entered_name = input("Type a name:").lower()
names = [name.lower() for name in names] 

if entered_name in names:
    quantity = names.count(entered_name)
    print(f"The name appears {quantity} times on the list!")
else:
    print("This name is not in the list!")
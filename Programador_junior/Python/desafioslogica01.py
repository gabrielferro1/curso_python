# Exercício: Inverter um número

valores = []

# ler 4 numeros e guardar na lista

for x in range(4):
    valor = int(input(f"Digite o {x+1}º valor: "))
    valores.append(valor)

# Mostrar entrada

print("Entrada:", valores)

# mostrar saida invertida

print("Saida:", valores[::-1])  # fatia invertida

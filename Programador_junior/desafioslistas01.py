# Desafios com listas

# Crie uma lista chamada frutas com pelo menos 5 frutas diferentes.

frutas = ['banana', 'morango', 'uva', 'kiwi', 'pessego']

#Mostre na tela:
#A primeira fruta da lista.
#A última fruta da lista.
#O total de frutas

primeira_fruta = frutas [0]
ultima_fruta = frutas [4]

print("A primeira fruta e:", primeira_fruta,)
print("A ultima fruta e:", ultima_fruta)
print("O total de frutas e:", len(frutas))

#Peça para o usuário digitar o nome de uma fruta e:
#Se a fruta estiver na lista, mostre "Sim, essa fruta está na lista!".
#Caso contrário, mostre "Essa fruta não está na lista.".

fruta = str(input("Digite o nome de uma fruta:"))
if fruta in frutas:
    print("Sim, essa fruta esta na lista!")
else:  
    print("Essa fruta nao esta na lista!")





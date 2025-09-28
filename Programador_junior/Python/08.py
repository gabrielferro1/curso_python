#Exemplo com uma criacao de um chat

import os

mensagens = []

nome = input("Nome: ")

while True:

    #Limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("__________________")

    #Obtendo texto

    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adicionando mensagem na lista

    mensagens.append({
        "nome": nome,
        "texto": texto
    })
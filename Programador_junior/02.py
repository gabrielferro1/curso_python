# EXERCICIO DE CALCULO DE PRESTACOES

casa = int(input("Valor da casa:"))
salario = int(input("Salario do comprador:"))
ano = int(input("Quantos anos de financiamento?:"))

prestacao = casa / (ano * 12)


print("Para pagar uma casa de", casa, "em", ano,
      "anos a prestacao sera de", prestacao)
if salario <= 600:
    print("NEGADO!!")
else:
    print("APROVADO!!")

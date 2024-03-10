# preco do bordado

pont = input("Quantos pontos tem o bordado? ")
precoPont = float(input("Quanto custa 1000 pontos? "))
quant = input ("Quantas peça você quer? ")
rs = (pont * precoPont) / 1000
custo = quant * rs
print"O bordado custa R$%.2f"%custo

op = raw_input("Tem desconto? s ou n ")
if op == "s":
    desc = input("Quantos por centos? ")
    desconto = (custo *desc) / 100
    prec = custo - desconto
    print"Com o desconto fica de R$%.2f"%prec

elif op == "n":
    print"Obrigado pela preferencia."


else:
    print"Você nao digito sua opção: s ou n"

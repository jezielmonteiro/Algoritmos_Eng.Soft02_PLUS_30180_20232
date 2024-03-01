#Um comerciante comprou um produto e quer vendê-lo com lucro de 5% se o valor da compra for menor que 20,00; caso contrário, o lucro 
#será de 30%. Entrar com o valor do produto e imprimir o valor da venda.

produto = float(input("Informe o valor do produto: "))
if (produto < 20):
    venda =  produto + (produto * 0.05)
    print(venda)
else:
    venda = produto + (produto * 0.3)
    print(venda)
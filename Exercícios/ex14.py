#Solicitar salário, prestação. Se prestação for maior que 20% do salário, imprimir: Empréstimo não pode ser concedido. Senão imprimir empréstimo pode ser concedido.


salario = float(input("Informe seu salário: "))

prestacao = float(input("Informe uma prestação: "))

if(prestacao > (salario * 0.2)):
   print("O empréstimo não pode ser concedido.")

else:
   print("O empréstimo pode ser concedido.")


    

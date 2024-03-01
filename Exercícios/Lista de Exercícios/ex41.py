#Solicitar um número entre 1 e 4. Se a pessoas digitar um número diferente, mostrar a mensagem "entrada inválida" e solicitar o número novamente. Se digitar correto mostrar o número digitado.


numero = int(input("Digite um número: "))

if(1 < numero < 4):
    print(numero)

else:
   numero = int(input("Entrada inválida. Digite um número válido: "))
   if(1 < numero < 4):
       print(numero)
       

    


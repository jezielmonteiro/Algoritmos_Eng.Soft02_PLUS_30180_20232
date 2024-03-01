#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("\nDigite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario != senha:
        print("\nUsername: ", usuario)
        print("Password: ", senha)
        break
    if usuario == senha:
        print("\nErro. Sua senha não pode ser igual ao seu nome de usuário. Tente novamente.")
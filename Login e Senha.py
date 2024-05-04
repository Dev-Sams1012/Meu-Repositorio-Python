"""Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações."""

def login():
    usuario = input("\nEscreva seu usuário: ")
    senha = input("\nEscreva sua senha: ")
    
    while usuario == senha:
        print("A senha é igual ao usuário, troque.")
        return login()

    print("Login feito.")

        
login()
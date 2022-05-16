from functions import *


print("Bem vindo(a)!")

tipoUser = int(input("Digite (1) se você for um candidato ou (2) para acesso como empresa: "))
loginOuCadastro = int(input("Digite (1) login ou (2) para cadastro: "))

if tipoUser != 1 and tipoUser != 2 or loginOuCadastro != 1 and loginOuCadastro != 2:
    tipoUser = int(input("Entrada inválida. Digite 1 para login de candidato ou 2 para login de empresa:  "))

while True:
    if tipoUser == 1:
        if loginOuCadastro == 1:
            login()
            menuCand()
            break
        elif loginOuCadastro == 2:
            cadastrarCand()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Sessão encerrada.")
                break
            else:
                continue
    if tipoUser == 2:
        if loginOuCadastro == 1:
            login()
            menuEmp()
            break
        elif loginOuCadastro == 2:
            cadastrarEmpr()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Sessão encerrada.")
                break
            else:
                continue










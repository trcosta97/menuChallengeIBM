
def login():
    emailSalvo = "email"
    senhaSalva = "12345"

    while True:
        print("Entre seu email e senha:")
        email = input("Email: ")
        senha = input("Senha: ")
        if email == emailSalvo and senha == senhaSalva:
            print("Login realizado com sucesso!")
            break
        else:
            print("Usuário ou senha incorretos, tente novamente.")

#CANDIDATO
def cadastrarCand():
    user = [input("Nome: "),
            input("Sobrenome: "),
            input("CPF: "),
            input("Data de Nascimento: "),
            input("Endereço: "),
            int(input("Telefone: ")),
            input("Email: "),
            input("Senha: ")]

    print("Obrigado por se cadastrar, um email foi enviado para a confirmação dos dados.")
    print("\n")

def menuCand():
    while True:
        opcaoCand = int(input("Bem vindo(a) ao menu do candidato(a)! Escolha a opção desejada: \n"
                              "(1) Cadastrar skills \n"
                              "(2) Buscar vaga \n"
                              "(3) Acompanhamento de candidaturas \n"))
        if opcaoCand == 1:
            cadastrarSkills()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Encerrando sessão.")
                break
            elif fim == "S":
                menuCand()
            else:
                print("Opção inválida. Retornando ao menu.")
                menuCand()
        elif opcaoCand == 2:
            buscarVaga()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Encerrando sessão.")
                break
            elif fim == "S":
                menuCand()
            else:
                print("Opção inválida. Retornando ao menu.")
                menuCand()
        elif opcaoCand == 3:
            candidaturas()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Encerrando sessão.")
                break
            elif fim == "S":
                menuCand()
            else:
                print("Opção inválida. Retornando ao menu.")
                menuCand()

        else:
            print("Opção inválida. Encerrando sessão.")
            break


def cadastrarSkills():
    print("Entre suas soft e hardskills: ")
    softSkiils = input("Softskills: ")
    hardSkills = input("Hardskills: ")



def buscarVaga():
    nivelVaga = int(input("Digite o número do nivel hierárquico da vaga desejada:\n"
                      "(1) Estágio\n"
                      "(2) Junior\n"
                      "(3) Pleno\n"
                      "(4) Sênior\n"))

    modalidadeVaga = int(input("Digite o número da modalidade da vaga desejada:\n"
                           "(1) Presencial\n"
                           "(2) Home Office\n"
                           "(3) Híbrido\n"))

    periodoVaga = int(input("Digite o período da vaga desejada:\n"
                           "(1) Manhã)\n"
                           "(2) Tarde\n"
                           "(3) Integral\n"))
def candidaturas():
    print("USUÁRIO ENCAMINHADO PARA PÁGINA DE CANDIDATURAS")


#EMPRESA
def cadastrarEmpr():
    empresa = [input("Nome: "),
               input("CNPJ: "),
               input("Endereço: "),
               input("Telefone: ")]
    print("Obrigado por se cadastrar, um email foi enviado para a confirmação dos dados.")



def menuEmp():
    while True:
        opcaoEmp = int(input("Bem vindo(a) ao menu da Empresa! Escolha a opção desejada: \n"
                             "(1) Buscar Candidato \n"
                             "(2) Anunciar Vaga \n"))
        if opcaoEmp == 1:
            buscarCand()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Sessão encerrada.")
                break
            elif fim == "S":
                menuEmp()
            else:
                print("Opção inválida. Retornando ao menu.")
                menuEmp()
        elif opcaoEmp == 2:
            anunciarVaga()
            fim = input("Deseja continuar? (S) ou (N)").capitalize()
            if fim == "N":
                print("Sessão encerrada.")
                break
            elif fim == "S":
                menuEmp()
            else:
                print("Opção inválida. Retornando ao menu.")
                menuEmp()
        else:
            print("Opção inválida. Encerrando sessão.")
            break


def buscarCand():
    nivelCand = int(input("Digite o número do nivel hierárquico do candidato desejado:\n"
                      "(1) Estágio\n"
                      "(2) Junior\n"
                      "(3) Pleno\n"
                      "(4) Sênior\n"))

    modalidadeCand = int(input("Digite o número da modalidade disponível desejada:\n"
                           "(1) Presencial\n"
                           "(2) Home Office\n"
                           "(3) Híbrido\n"))
    periodoCand = int(input("Digite o período de disponibilidade desejada:\n"
                           "(1) Manhã\n"
                           "(2) Tarde\n"
                           "(3) Integral\n"))


def anunciarVaga():
    nivelVaga = int(input("Digite o número do nivel hierárquico da vaga desejada:\n"
                          "(1) Estágio\n"
                          "(2) Junior\n"
                          "(3) Pleno\n"
                          "(4) Sênior\n"))

    modalidadeVaga = int(input("Digite o número da modalidade da vaga desejada:\n"
                               "(1) Presencial\n"
                               "(2) Home Office\n"
                               "(3) Híbrido\n"))

    periodoVaga = int(input("Digite o período da vaga desejada:\n"
                            "(1) Manhã\n"
                            "(2) Tarde\n"
                            "(3) Integral\n"))








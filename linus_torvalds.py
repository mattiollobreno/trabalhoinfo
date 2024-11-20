def resumo():
    mensagem = "Linus Torvalds é o criador do Linux e do Git, fundamentais no software livre e no desenvolvimento de sistemas."
    return mensagem


def doutorado():
    mensagem = "Doutorado honorário da Universidade de Estocolmo, em 1999, e outro da Universidade de Helsinque, em 2000"
    return mensagem


def contribuicoes():
    mensagem = "Linux (1991): Criador do kernel do sistema operacional, base de diversas distribuições como Ubuntu, Fedora e Android. Também foi criador do sistema de controle de versão usado por milhões de desenvolvedores para gerenciar código de forma eficiente e colaborativa, o Git."
    return mensagem


def artigos():
    mensagem = "blablalalalalalzaslakfni"
    return mensagem


def citacoes():
    mensagem = "dfbfjbajfbajfjkabjdfbajfbkjanfasfsaf"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)

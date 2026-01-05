
def adicionar_contato(nome, telefone):
    agenda = open("agenda/agenda1.txt", "a")
    agenda.write("Nome: " + nome + " | Telefone: " + telefone + "\n")
    agenda.close()

    return "Contato salvo!"


def listar_contatos():
    agenda = open("agenda/agenda1.txt", "r")
    conteudo = agenda.read()
    agenda.close()

    if conteudo == "":
        return "Agenda vazia!"
    else:
        return conteudo


def buscar_contato(nome):
    agenda = open("agenda/agenda1.txt", "r")
    lista = agenda.readlines()
    agenda.close()

    encontrado = False
    resultado = ""

    for linha in lista:
        if nome.lower() in linha.lower():
            resultado += linha
            encontrado = True

    if encontrado:
        return resultado
    else:
        return "Contato não encontrado!"


def remover_contato(nome):
    agenda = open("agenda/agenda1.txt", "r")
    linhas = agenda.readlines()
    agenda.close()

    agenda = open("agenda/agenda1.txt", "w")
    encontrado = False

    for linha in linhas:
        if nome.lower() not in linha.lower():
            agenda.write(linha)
        else:
            encontrado = True

    agenda.close()

    if encontrado:
        return "Contato removido!"
    else:
        return "Contato não encontrado!"


while True:
    print("1 - Adicionar contato.")
    print("2 - Exibir lista de contatos.")
    print("3 - Buscar contato.")
    print("4 - Remover contato.")
    print("5 - Sair.")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        print(adicionar_contato(nome, telefone))

    elif escolha == 2:
        print(listar_contatos())

    elif escolha == 3:
        nome = input("Digite o nome do contato que deseja buscar: ")
        print(buscar_contato(nome))

    elif escolha == 4:
        nome = input("Digite o nome do contato que deseja remover: ")
        print(remover_contato(nome))

    elif escolha == 5:
        break

    else: 
        print('Escolha inválida!')
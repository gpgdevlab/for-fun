def inverter(lista):
    i = -1
    invertida = []

    for elemento in lista:
        invertida.append(lista[i])
        i -= 1

    print(invertida)


def adicionar(dicionario):
    elemento = input("Nome do elemento: ")
    valor = int(input("Valor: "))

    dicionario[elemento] = valor

    print(f"{elemento} foi adicionado com o valor R${valor}")


def atualizar(dicionario):
    print("Qual elemento você quer atualizar o valor?")

    for key in dicionario:
        print(f"{key} - {dicionario[key]}")

    print("Caso deseje retornar digite 'Sair'")

    elemento = input("Elemento: ")

    while elemento != "Sair":
        if elemento not in dicionario:
            print("Não achamos o elemento no estoque")
        else:
            valor = int(input("Qual o novo valor do elemento? "))
            dicionario[elemento] = valor
            print(f"{elemento} tem um novo preço agora")

        elemento = input("Digite outro elemento ou 'Sair': ")


def excluir(dicionario):
    for key in dicionario:
        print(key)

    print("Caso deseje retornar digite 'Sair'")

    elemento = input("Qual elemento você deseja remover do Banco de Dados? ")

    while elemento != "Sair":
        if elemento not in dicionario:
            print("Não achamos o elemento no estoque")
        else:
            dicionario.pop(elemento)
            print(f"{elemento} foi removido")

        elemento = input("Digite outro elemento ou 'Sair': ")

    print(dicionario)


def menu(dados):
    while True:
        print("\n======= MENU =======")
        print("""1 - Adicionar Elemento
2 - Excluir Elemento
3 - Atualizar Elemento
4 - Ver Elementos
5 - Sair""")

        try:
            acao = int(input("Escolha sua ação de 1 - 5: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        match acao:
            case 1:
                adicionar(dados)
            case 2:
                excluir(dados)
            case 3:
                atualizar(dados)
            case 4:
                print(dados)
            case 5:
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")


def personalizada():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    print(f"Olá, {nome}, você possui {idade} anos")


klinck = {
    "k": 34,
    "j": 34,
    "l": 34,
    "v": 34
}

lista = [1, "dois", 4]

menu(klinck)

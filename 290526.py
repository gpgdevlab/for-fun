def inverter(lista):
    i = -1 
    j = 0
    invertida = []
    for element in lista:
        invertida.append(lista[i])
        i -= 1
    return print(invertida)

def adicionar(dicionario):
    item = str(input(""))
    valor = int(input(""))

    dicionario.update({item: valor})

    return print(f"{item} foi adicionado com o valor R${valor} no dicionário")

def atualizar(dicionario): 
    print(f"Qual item você quer atualizar o valor?")

    for key in dicionario:
        print(key)

    print("Caso deseje retornar digite *Sair*")

    item = str(input())   

    while item != "Sair":
        if item not in dicionario:
            print("Não achamos o item no estoque")
        else:
            valor = int(input("Qual o novo valor do item?"))
            dicionario[item] = valor
            print(f"{item} tem um novo preço agora")
        
    return 0

def menu(dados):
    print("======= MENU =======")
    print("""1 - Adicionar Elemento
2 - Excluir Elemento
3 - Atualizar Elemento
4 - Ver Elementos
5 - Sair""")
    acao = int(input("Escolha sua ação de 1 - 5: "))

    match acao:
        case 1:
            adicionar(dados)
        case 2:
            atualizar(dados)
        case 3:
            atualizar(dados)
        case 4:
            print(dados)  
        case 5:
            return 0      
    return menu(dados)

klinck ={
    "k" : 34,
    "j" : 34,
    "l" : 34,
    "v" : 34
}


lista = [1, "dois", 4]


def personalizada():
    nome = str(input(""))
    idade = int(input(""))
    return print(f"Olá, {nome} você possui {idade} anos")

menu(klinck)

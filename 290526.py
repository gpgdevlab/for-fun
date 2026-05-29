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

klinck ={

}


lista = [1, "dois", 4]

inverter(lista)

adicionar(klinck)
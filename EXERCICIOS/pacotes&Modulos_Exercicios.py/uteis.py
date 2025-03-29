def aumentar(preco, taxa):
    res = f'R${preco + (preco * taxa / 100): .2f}'.replace('.', ',')
    return res

def diminuir(preco, taxa):
    res = f'R${preco - (preco * taxa / 100): 2f}'.replace('.', ',')
    return res


def dobro(preco, taxa):
    res = f'R${preco* 2: .2f} '.replace('.', ',')
    return res

def metade(preco, taxa):
    res = f'R${preco * 2: .2f} '.replace('.', ',')
    return res

def monetario(preco):
    res = f' R$ {preco: .2f}'.replace('.', ',')
    return res


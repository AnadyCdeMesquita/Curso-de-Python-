import uteis

preco = float(input('Digite o preço:  '))
taxa = int(input('Digite a taxa:  '))

aumento = uteis.aumentar(preco, taxa)
diminui = uteis.diminuir(preco, taxa)
dobrar = uteis.dobro(preco, taxa)
met = uteis.metade(preco, taxa)
valor = uteis.monetario(preco)

print(f'O valor é de {preco}/ o aumento foi de {aumento}/ diminui: {diminui}/ dobra: {dobrar} / metade: {met}.')
print(valor)
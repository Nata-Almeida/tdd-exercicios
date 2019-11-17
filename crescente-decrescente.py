lista = [9,5,2,3,6,8,4,1]
print(lista)
pergunta = input('Ordem crescente ou decrescente? ')
if pergunta == 'crescente':
    print(sorted(lista))
elif pergunta == 'decrescente':
    print(sorted(lista, reverse = True))

from random import randint
computador = randint(0,100)
pergunta = int(input('Em qual numero de 0 a 100 eu estou pensando? '))

if pergunta > computador:
        print('Maior')
elif pergunta < computador:
        print('menor')
elif pergunta == computador:
        print('Parabens você acertou !')



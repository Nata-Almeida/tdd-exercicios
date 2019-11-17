n1 = float(input('Primeiro Bimestre: '))
n2 = float(input('Segundo Bimestre: '))
n3 = float(input('Terceiro Bimestre: '))
n4 = float(input('Quarto Bimestre: '))
media = float((n1+n2)+(n3+n4)) /4
if media < 7:
     print('Você foi reprovado com {} de média'.format(media))
else:
    print('Você foi aprovado com {} de média'.format(media))
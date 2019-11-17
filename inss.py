salario = float(input('Digite um salario: '))
transporte = (salario * 3 / 100)
inss = salario * 9 / 100
saude = 347 * 15 / 100

sl = salario - inss - transporte - saude
print('Seu salario integral é', salario)
print('INSS - {:.2f}.'.format(inss))
print('- 15% do valor total de 347,00 do Plano de saude ({:.2f}).'.format(saude))
print('Vale transporte  - 3% ({:.2f}).'.format(transporte))
print('Salario líquido:', sl)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
if imc <= 24.9:
    print('Parabéns você está em seu peso normal')
if imc <= 30:
    print('Você está acima do peso')
if imc > 30:
    print('Você está obeso')
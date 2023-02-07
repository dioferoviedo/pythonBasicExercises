print('Seja bem-vindo ao Exército do Diofer!\nInsira suas informações: ')
print()

nome = input('Nome: ')
idade = input('Idade: ')
altura = input('Altura: ')
peso = input('Peso: ')

print()
if idade < str(18):
    print('Dispensado. Idade insuficiente.')
elif altura < str(1.70):
    print('Dispensado. Altura insuficiente.')
elif peso < str(60):
    print('Dispensado. Peso insuficiente.')
else:
    print('Parabéns,', nome,'\nVocê está apto para ingressar no Exército do Diofer!')



'''
Faça um programa que pergunte a idade, o peso e altura
de uma pessoa e veja se ela está apta para o Exército.
Requisitos: 18 anos, 60kg e 1.70m.
'''
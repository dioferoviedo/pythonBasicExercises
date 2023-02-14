print('Controle de convidados para a festa')
print('##################################')

quantia = input('Quantidade de convidados: ')
lista_de_convidados = []


i = 1
while i <= int (quantia): # for i in range(int(quantia))
    nome_convidado = input('Insira o nome do convidado #' + str(i) + ':')
    lista_de_convidados.append(nome_convidado)
    i += 1

print('Serão', quantia, 'convidados.')

print('\nLista de Convidados')
for convidado in lista_de_convidados:
    print(convidado)


'''
Faça um programa que leia a quantidade de pessoas que
serão convidadas para uma festa. Após isso, o programa 
irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
Imprimir todos os nomes da lista.
'''
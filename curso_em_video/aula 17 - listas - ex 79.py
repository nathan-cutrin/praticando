# Ex 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    var = int(input('Digite um valor: '))
    if var not in lista:
        lista.append(var)
        print('Número adicionado')
    else:
        print('Número duplicado não será adicionado')
    cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if 'N' in cont:
        break

lista.sort()
print(lista)


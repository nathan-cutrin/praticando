# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
continuar = 'S'

while continuar == 'S':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]

for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f'Lista toda: {lista}'
      f'\nLista de pares: {lista_par}'
      f'\nLista impares: {lista_impar}')

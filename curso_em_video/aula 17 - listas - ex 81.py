# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


tamanho = int(input('Digite qual será o tamanho da lista: '))

lista = [int(input('Digite um número: ')) for num in range(0, tamanho)]

lista.sort(reverse=True)

print(f'O tamanho da lista é de {len(lista)} valores'
      f'\nLista ordenada de forma decrescente: {lista}')

if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')

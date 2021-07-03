# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = tuple(int(input('Digite um numero: ')) for c in range(1, 5))
print(num)


num = tuple()

for c in range(1, 5):
   num = input('Digite um número: ')





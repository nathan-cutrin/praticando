# Ex 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

v = ("a","e","i", "o", "u")

count = 0
for x in range (0,len(palavras)):
    for y in range(0,len(palavras[x])):
         if palavras[x][y] in v[:]:
            count +=1
    print (palavras[x], f"Tem {count} vogais.")
    count = 0
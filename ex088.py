from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('       JOGA NA MEGASENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os números sorteados foram {jogos}')
print('-=' *3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
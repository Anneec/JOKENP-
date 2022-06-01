from random import randint
from  time import  sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}.'.format(itens[computador]))
print('''SUAS OPCOES: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÓ!!!')
sleep(1)
print('\033[1;34m''-=''\033[m' * 12)
print('\033[33m''Computador jogou {}{}{}.''\033[m'.format('\033[4;32m', itens[ computador ], '\033[m'))
print('\033[33m''Jogador jogou {}{}{}.''\033[m'.format('\033[4;32m', itens[jogador], '\033[m'))
print('\033[1;34m''-=''\033[m' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA')
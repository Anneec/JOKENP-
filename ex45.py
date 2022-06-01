from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura ''')

jogador = int(input("Qual a sua jogada? "))

print(f"Computador jogou {itens[computador]} ")
print(f'Jogador jogou {itens[jogador]} ')



from random import choice

print('\033[1;37;40m JOKENPÔ \033[m')

# 1. Entrada do jogador (usamos .lower() para evitar erro com letras maiúsculas)
pptJ = input('Faça uma jogada (pedra, papel, tesoura): ').lower().strip()

# 2. O computador faz a escolha dele e guarda na variável 'pc'
jogadas = ['pedra', 'papel', 'tesoura']
pc = choice(jogadas)

print(f'O computador escolheu: {pc}')

# 3. Lógica do Jogo
if pptJ == pc:
    print('\033[1;33mEMPATE!\033[m')

elif pptJ == 'pedra':
    if pc == 'tesoura':
        print('Você GANHOU! Pedra quebra tesoura.')
    else:
        print('Você PERDEU! Papel embrulha pedra.')

elif pptJ == 'tesoura':
    if pc == 'papel':
        print('Você GANHOU! Tesoura corta papel.')
    else:
        print('Você PERDEU! Pedra quebra tesoura.')

elif pptJ == 'papel':
    if pc == 'pedra':
        print('Você GANHOU! Papel embrulha pedra.')
    else:
        print('Você PERDEU! Tesoura corta papel.')

else:
    print('Jogada inválida! Escreva pedra, papel ou tesoura.')
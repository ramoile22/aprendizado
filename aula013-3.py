from time import sleep
# Aqui você digita um número e o programa vai contá-lo
n = int(input('''digite um número.
e nós o contaremos, começando em 1'''))
# Ele vai fingir que tá processando, quando na verdade, NÃO.
print('PROCESSANDO...')
sleep(5)
# Então ele começará a contar os números
for c in range(0, n):
    print(c)

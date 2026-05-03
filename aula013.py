from time import sleep

# Passo 1: Recebemos a entrada do utilizador
aL = input('Digite algo: ')

# Passo 2: Avisamos o utilizador e fazemos a pausa
print('Imprimindo...')
sleep(5)

# Passo 3: Criamos um laço que vai rodar 99 vezes (do 1 ao 99)
for b in range(1, 100):
    # Passo 4: Exibimos a variável 6 vezes na mesma linha
    # No Python, multiplicar um texto (str) faz com que ele se repita!
    print(f'{aL} ' * 6)
print('END')
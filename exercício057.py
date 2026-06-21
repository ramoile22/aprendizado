from emoji import emojize
n1 = ''
r = 'S'
homem = mulher = 0
while r == 'S':
    # noinspection PyRedeclaration
    n1 = emojize(input('\033[1;32mDigite seu sexo: [M/F]\033[m 👩🧔')).strip().upper()
    if n1 == 'M' :
        homem += 1
        r = input('\033[0;30;43mDeseja continuar?\033[m \033[0;32m[S\033[m\033[0;31m/N]\033[m').strip().upper()
    elif n1 == 'F':
        mulher += 1
        r = input('\033[0;30;43mDeseja continuar?\033[m \033[0;32m[S\033[m\033[0;31m/N]\033[m').strip().upper()
    else:
        print('Tente novamente com a palavra correta!')

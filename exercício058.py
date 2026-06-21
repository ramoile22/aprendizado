from random import randint
from emoji import emojize
from time import sleep
print(emojize('Sorteando...🙂(De 1 a 10)'))
sleep(5)
r1 = randint(0,10)
r2 = int(input('Qual número eu sortiei?'))
r3 = 0
sleep(3)
while r2 != r1 :
    r2 = int(input('Digite novamente!'))
    r3 += 1
print('Você precisou de \033[0;37m{}\033[m chances para acertar!'.format(r3))


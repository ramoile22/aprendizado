#frase = 'Curso em vídeo Python'
#print(frase)
#aqui a exibimos normalmente
frase = str(input('Digite uma frase'))
print(frase)

print(len(frase))
r1=frase.count('O') and frase
r2=frase.count('o') and frase
if r1 < 2 and r2 < 2 :
  rf1 =  r1.replace('o' ,'e')
  rf2 =  r2.replace('O','E')
  print(f'As frases modificadas são {rf1} e {rf2}')
else:
  print('a frase é {}, portanto não precisa de modificações'.format(frase))

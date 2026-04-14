nl = int(input('Digite um número'))
M = nl // 1  % 10
c = nl // 10 % 100
d = nl // 100 % 1000
u = nl // 1000 % 10000
print(f'''unidade{u} 
dezena {d},
centena {c}
e unidade de milhar {M}''')


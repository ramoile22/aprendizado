r = input('Digite algo')
print('o valor disso', r.__class__.__name__
)
print('tem espaços? ',r.isspace())
print('tem letras?',r.isalpha())
print(len(r))
print('tem numeros?',r.isnumeric())
print('tem letras e números?',r.isalnum())

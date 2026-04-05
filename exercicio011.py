# Leitura dos dados
largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))

# Cálculo da área
area = largura * altura

# Cálculo da tinta (1 litro para cada 2m²)
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')

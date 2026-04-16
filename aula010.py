# Passo 1: Recebemos o valor em reais
rS = float(input('Quantos reais você tem? '))

# Passo 2: Verificamos se o valor é maior que 5
if rS > 5:
    print('Uau, você não é pobre.')

    # Passo 3: Recebemos a confirmação do utilizador
    vf = input('''Tem certeza que você está falando a verdade?
(digite "true!" para verdade e "false" para falso): ''')

    # Passo 4: Comparamos texto com texto usando as aspas
    if vf == 'false':
        print('Você é um mentiroso, hein?')
    elif vf == 'true50':
        print('Ainda bem que falou a verdade!')
    else:
        # Se o utilizador digitar algo diferente de true! ou false
        print('Resposta inválida, mas vou fingir que acredito!')

else:
    print('Kkk, você é pobre!!')


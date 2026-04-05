prc = float(input('Quantos dias você ficou com o carro?')) * 60.00
prkm = float(input('QUantos km você rodou com o carro?')) * 0.15
qc = int(input('Quantos carros vc alugou?'))
print('O valor que v3ocê tem que pagar é de {}'.format((prc  + prkm) * qc ))
import random
chances=[3,2,1]
for i in chances:
	numero_ale=random.randint(1,2)
	print('Você tem apenas...',i,'chances')
	chute=int(input('Digite seu chute: '))
	if numero_ale==chute:
		print('Acertou em cheio! ')
		break
	else:
			print('Errou feio! ')
else:
			print('Chances esgotadas!!! Perdeu feio')
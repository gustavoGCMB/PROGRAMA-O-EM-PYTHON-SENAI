#calculadora
def soma(n1, n2):
          print('=',n1+n2)
def subtracao(n1,n2):
          print('=',n1,n2)
def mult(n1,n2):
          print('=',n1-n2)
def div(n1,n2):
          print('=',n1 / n2)
def calculadora():
	n1=float(input('='))
	op=input('Escolha a operação + - * ')
	if op =='+':
		n2=float(input('='))
		soma(n1,n2)
	elif op=='-':
			n2=float(input('='))
			subtracao(n1,n2)
	elif op=='*':
			n2=float(input('='))
			mult(n1,n2)
	elif op=='/':
			n2=float(input('='))
			div(n1,n2)
	else:
		print('Digite algo válido')
while True:
	calculadora()
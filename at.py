def chamar_nome():
    print('Nome: ','João')
chamar_nome()
def mostrar_idade():
	idade=int(input('Digite a idade'))
	print('Sua idade é', idade)
mostrar_idade()
#ação banco:
#saque-deposito-extrato-emprestimo
def banco():
    saldo = 10000.0
    escolha = input('''
      1 -  saque
      2 - deposito
      3 - extrato
      4 - emprestimo
     ''')
    if escolha  == '1':
        valor_saque = float(input(' saque >>'))
        saque  =  saldo - valor_saque
        print('Saque - R$', valor_saque)
        print('Saldo - R$  ', saque)
    elif escolha  == '2':
        valor_deposito = float(input(' deposito >>'))
        total  =  saldo + valor_deposito
        print('Deposito - R$', valor_deposito)
        print('Saldo - R$  ', total)
    elif escolha  == '3':
        print('Saldo R$', saldo )
    elif escolha == '4':
        print('Voce escolheu emprestimo digite o valor')
        saldo = saldo + float(input('Valor: '))
        print('R$ - ',saldo)
        
    else:
        print('essa opção não existe')
        
def loop():        
    while True:
        banco()
    
        
loop()        



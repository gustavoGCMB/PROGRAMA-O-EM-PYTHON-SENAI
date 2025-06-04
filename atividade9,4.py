# e-commerce

carrinho  = []
m_valores = []

comprar =  input('Deseja fazer pedido?: s/n ')

produtos = ['','a','b','c']
valor = ['',100.0,200.0,300.0]
while comprar == 's' or comprar == 'S' or comprar == 'sim':
    meu_prod = int(input('Digite o ID 1  -  2  - 3'))
    carrinho.append(produtos[meu_prod])
    m_valores.append(valor[meu_prod])
    print('seus produtos', carrinho)
    soma = sum(m_valores)
    print('R$', soma)
    comprar =  input('Deseja continuar?: s/n ')
else:
    
    print('---'*10)
    print('R$', soma )
    print('Obrigada volte sempre')
    
    
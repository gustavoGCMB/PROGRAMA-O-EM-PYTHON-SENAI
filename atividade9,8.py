#1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
i=0
while i <=1000:
	print(i)
	i=i+1
#2 -  Faça um sistema, utilizando ***while e listas***,
#que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.# sistema de notas

senha  =  'Gustavocardozo10_'
acesso =  'gustavomoital10'
p  =   0
lista_notas  = []

while p  <= 3:
    senha_user = input('Digite sua senha: ')
    login =  input('Digite seu login')
    p = p + 1
    if senha == senha_user and login == acesso:
        print('Sistema de notas')
        quantas_notas =  int(input('Quantiade notas: '))
        for n in range(quantas_notas):
            nota =  float(input('Digita a nota: '))
            lista_notas.append(nota)
            soma = sum(lista_notas)
            media  =  soma / quantas_notas
        print('Media - ', media)
        break
             
        
        
    else:
        print('Digitação incorreta! ')
else:
    print('Conta bloqueada!!')
    
    

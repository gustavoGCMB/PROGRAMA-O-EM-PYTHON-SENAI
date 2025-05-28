#indentação em python-organizar o codigo py
#tipo de organização do código
#variável precisa estar dentro da borda
#quando não estiver dentro de nenhum escopo
x=10
#quando estiver dentro de um escopo
#precisar ter pelo menos um espaço
#o padrão são quatro espaços
if x==10:
    print(x)
    

variável='teste'
x=10
for n in range(1,3):
if variável=='teste':
   print('ok')
else:
   print('teste2')
if 1>10:
    x:10
#concatenação=juntar informações
nome=maria
print('ola,seja bem vinda',nome)
print('ola,seja bem vinda'+' '+ nome)
print('ola,seja bem vinda {}'format(nome))
print('ola,seja bem vinda %s'%(nome))
print(f'ola,seja bem vinda {nome}')
print(f'ola,seja bem vinda\n',nome)
#-------------------------------------
#refatorar = melhorar o código
#encontrar erros
nome='julio'
sobrenome='cesar'
print('hello',nome,sobrenome)
#exemplo incorreto
x='julio'
y='cesar'
print('hello',x,y)

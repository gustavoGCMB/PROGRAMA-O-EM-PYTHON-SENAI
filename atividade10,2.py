#exercicio 1
def comparar_par_impar(num1, num2):
    # Verificando se o primeiro número é par ou ímpar
    if num1 % 2 == 0:
        resultado1 = 'par'
    else:
        resultado1 = 'ímpar'
    
    # Verificando se o segundo número é par ou ímpar
    if num2 % 2 == 0:
        resultado2 = 'par'
    else:
        resultado2 = 'ímpar'
    
    # Comparando os resultados
    if resultado1 == resultado2:
        return f"Os dois números são {resultado1}s."
    else:
        return "Os números são diferentes (um é par e o outro é ímpar)."
    

#exercicio 2
def multiplicar_tres_numeros(a, b, c):
    return a * b * c

# Solicitar os três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chamar a função e exibir o resultado
resultado = multiplicar_tres_numeros(num1, num2, num3)
print(f"O resultado da multiplicação é: {resultado}")
 
 
#exercicio 3
def elevar_numero(base, expoente):
    return base ** expoente

# Solicitar a base e o expoente ao usuário
base = float(input("Digite o número base: "))
expoente = int(input("Digite o expoente: "))

# Chamar a função e exibir o resultado
resultado = elevar_numero(base, expoente)
print(f"O resultado de {base} elevado a {expoente} é: {resultado}")

#exercicio 4
def mensagem_personalizada(idade):
    if idade == 18:
        print("Você tem 18 anos! Parabéns por alcançar a maioridade!")
    else:
        print("Sua idade é", idade, "anos.")
    
#exercicio 5
from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

# Solicitar o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

# Calcular e exibir a idade
idade = calcular_idade(ano_nascimento)
print(f"Sua idade é: {idade} anos.")

#exercicio 6
def verificar_copa_1999():
    
    copa_1999 = "Não"
    if copa_1999 == "Não":
        return "O Brasil não ganhou a Copa do Mundo de 1999."
    else:
        return "O Brasil ganhou a Copa do Mundo de 1999!"

# Chamar a função e mostrar o resultado
resultado = verificar_copa_1999()
print(resultado)

#exercicio 7
def mostrar_menu():
    print("Bem-vindo ao Restaurante!")
    print("Escolha uma opção do menu:")
    print("1. Salada - R$ 15.00")
    print("2. Macarronada - R$ 20.00")
    print("3. Sanduíche - R$ 10.00")
    print("4. Sorvete - R$ 8.00")

def pedir_prato():
    mostrar_menu()
    
    # Solicitar ao cliente a escolha do prato
    opcao = int(input("Digite o número do prato escolhido: "))
    
    if opcao == 1:
        return "Salada", 15.00
    elif opcao == 2:
        return "Macarronada", 20.00
    elif opcao == 3:
        return "Sanduíche", 10.00
    elif opcao == 4:
        return "Sorvete", 8.00
    else:
        print("Opção inválida. Tente novamente.")
        return pedir_prato()

def calcular_total(pedidos):
    total = 0
    for pedido in pedidos:
        total += pedido[1]
    return total

def sistema_restaurante():
    pedidos = []
    continuar = 's'
    
    while continuar.lower() == 's':
        prato, preco = pedir_prato()
        pedidos.append((prato, preco))
        
        continuar = input("Deseja escolher outro prato? (s/n): ")
    
    total = calcular_total(pedidos)
    print("\n--- Pedido Final ---")
    for prato, preco in pedidos:
        print(f"{prato}: R$ {preco:.2f}")
    
    print(f"\nTotal a pagar: R$ {total:.2f}")
    print("Obrigado por escolher o nosso restaurante!")

# Iniciar o sistema de restaurante
sistema_restaurante()

     
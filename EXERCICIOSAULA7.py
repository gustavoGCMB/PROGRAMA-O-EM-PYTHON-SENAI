#Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
numeros=list(range(2,22,2))
print(numeros)
#Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
numeros=list(range(1,11,1))
print(numeros)
#Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
numeros=[1,2,3,4,5,6]
print(numeros[2])
#Exercício 3:** Adicione o número 9 à lista numeros e imprima a lista atualizada.
lista=[1,2,3,4,5,6,7]
lista.append(9)
print(lista)
#Exercício 4:** Remova o número 5 da lista numeros e imprima a lista resultante.
lista=[1,2,3,4,5,6,7,8,9,]
lista.remove(5)
print(lista)
#Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
carros  =  ['tesla', 'ferrari','Jeep']
print(carros,numeros)
carros +=(numeros)
print(carros)



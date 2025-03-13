'''
1.
dados = (25, 3.14, "João", True)
print("Segundo elemento:", dados[1])
print("Quarto elemento:", dados[3])
try:
    dados[0] = 30  
except TypeError as e:
    print("Erro:", e)
2.
tupla = (1, 2, 2, 3, 2)
contagem = tupla.count(2)
print("O número 2 aparece", contagem, "vezes na tupla.")
3.
numint=[1,2,3,4,5,6]
numint.append(100)
numint.pop(2)
numint[0]=500
print(numint)






4.
notas=[6,6,6,6,6]
soma = sum(notas)
media = soma / len(notas)
print("Soma das notas:", soma)
print("Média das notas:", media)


5.
numint=[1,2,3,4,5,6]
print(numint.sort())
print(numint.sort(reverse=True))]
numeros_maiores_que_10 = [num for num in numeros if num > 10]
print("Números maiores que 10:", numeros_maiores_que_10)


6. notas = [[7, 8, 9, 6], [6, 5, 8, 7], [10, 9, 8, 9]]
print(notas[1][2])
medias = [sum(aluno) / len(aluno) for aluno in notas]
maior_media = max(medias)
indice_maior_media = medias.index(maior_media)
print(f'Aluno {indice_maior_media + 1} com a maior média: {maior_media}')
7. valores = []
for i in range(4):
    valores.append(int(input(f'Digite o {i+1}º valor: ')))

print(f'O valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O primeiro valor 3 foi digitado na posição {valores.index(3)}.')
else:
    print('O valor 3 não foi digitado.')

pares = [num for num in valores if num % 2 == 0]
print(f'Os números pares são: {pares}')
8. import random

lancamentos = [random.randint(1, 6) for _ in range(50)]
ocorrencias_face_6 = lancamentos.count(6)
percentual_face_6 = (ocorrencias_face_6 / 50) * 100

print(f'A face 6 apareceu {ocorrencias_face_6} vezes, o que representa {percentual_face_6}% dos lançamentos.')


'''

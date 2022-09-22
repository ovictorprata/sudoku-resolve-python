


def confere_lista(lista):
	dicionario = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	erro = 0
	for i in range(0,9):
		for elemento in lista[i]:
			dicionario[elemento] += 1

		for valor in dicionario.values():
			if valor != 1:
				erro += 1

		dicionario = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	return erro

def ler_matriz():
	matriz = []
	for i in range(9):
		linha = raw_input("")
		numeros_texto = linha.split()
		numeros = []
		for texto in numeros_texto:
			numeros.append(int(texto))
		matriz.append(numeros)
	return matriz

n = int(input(""))

for i in range (n):
	linhas = ler_matriz()


# FAZ O COLUNAS
colunas = []
coluna = []
for j in range(0, 9):
	for i in range (0, 9):
		coluna.append(linhas[i][j])
		if i == 8:
			colunas.append(coluna)
			coluna = []

# FAZ O QUADRADOS---------------------
quadrados = []
quadrado1 = []
quadrado2 = []
quadrado3 = []

for k in range(0, 3): #pega os 3 primeiros quadrados
	for i in range(0 + k*3, 3 + k*3): #agrupa os quadrados
		for j in range(0, 9):
			if j < 3:
				quadrado1.append(linhas[i][j])
			elif j < 6:
				quadrado2.append(linhas[i][j])
			elif j < 9:
				quadrado3.append(linhas[i][j])

			if len(quadrado1) == 9:
				quadrados.append(quadrado1)
				quadrado1 = []

			if len(quadrado2) == 9:
				quadrados.append(quadrado2)
				quadrado2 = []

			if len(quadrado3) == 9:
				quadrados.append(quadrado3)
				quadrado3 = []

erro = 0

if confere_lista(linhas) != 0 or confere_lista(colunas) != 0 or confere_lista(quadrados) != 0:
	print('\nJogo incorreto\n')
else: 
	print('\nJogo CORRETO\n')

	

print('linhas', confere_lista(linhas))
print('colun', confere_lista(colunas))
print('qua', confere_lista(quadrados))


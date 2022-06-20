#	Python 3.10.5
#   Author: Lorran Rocha https://lorranrocha.com/

import string, random, os


caracteres = list(string.ascii_letters + string.digits + "!@#$%&*")

def gerarSenha():
	try:
		os.system('clear')
	finally:
		os.system('cls')


	tamanho = int(input("Digite o tamanho da senha (Ex.:15): "))

	random.shuffle(caracteres)
	
	
	senha = []
	for i in range(tamanho):
		senha.append(random.choice(caracteres))


	random.shuffle(senha)

	try:
		os.system('clear')
	finally:
		os.system('cls')


	print("Sua senha gerada é:", "".join(senha))
	print("\n\n\n")
	opcao = int(input("Deseja gerar outra senha?\n1- Sim\n2- Não\nR: "))

	if opcao == 1:
		gerarSenha()

	else:
		print("Obrigado por usar nosso sistema!")
		exit()

gerarSenha()
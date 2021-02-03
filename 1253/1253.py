
#função que recebe as hash
def recebe_valor(quant_senhas):
	#guarda as senhas e posições
	senhas=[]
	#verifica se são apenas letras
	verificador = []
	testador = False
	
	for i in range(quant_senhas):
		segredo=input('Digite a palavra criptografada\n').upper()
		#converte a string em lista pra poder verificar os caracteres
		verificador = list(segredo)
		#percorre cada letra da string
		for index in verificador:
			#verifica se não é uma letra maiuscula
			if ord(index) < 65 or ord(index) > 90:
				#se não for a variavel teste é alterada para rodar o proximo loop
				testador = True
		#testes até o dado de entrada ser o pedido na questão
		while testador:
			#limpa a lista para nao haver copias
			verificador.clear()
			print('\nDigite apenas Letras maiúsculas entra A~Z\n')
			segredo=input('Digite a palavra criptografada\n').upper()
			verificador = list(segredo)
			for index in verificador:
				if ord(index) < 65 or ord(index) > 90:
					testador = True
				#quando o usuario digitar certo a variavel de teste é alterada
				else:
					testador = False
		#recebe a quantidade de casas a mover	
		casas= int(input('Digite a quantidade de posições movidas à direita\n(0~25)\n'))
		#enquanto valor de posição estiver fora do especificado
		while casas < 0 or casas > 25:
			print('\nNUMERO INVÁLIDO\n')
			casas= int(input('Digite a quantidade de posições movidas à direita\n(0~25)\n'))
		#adiciona a senha e as posições na lista
		reagrupa = ''.join(verificador)
		senhas.append([reagrupa, casas])
	return senhas


#função que traduz os segredos
def decodificador(chaves):
	#recebe o resultado da string trabalhada
	aux_recebedora=[]
	#recebe o resultado final
	senha=[]
	#percorre as listas dentro da lista
	for hash in chaves:
		 #criada toda vez pra juntar a cifra final
		 juncao=""
		 #recebe a cifra
		 str_aux = hash[0]
		 #recebe a quantidade de posições movidas
		 posicao = hash[1]
		 #percorre os caracteres da cifra
		 for i in range(len(str_aux)):
		 	#trata as letras que irão chegar no -'Z'
		 	if ord(str_aux[i]) - posicao < 65:
		 		#recebe o valor restante a descontar a partir do -'Z'
		 		soma = ord(str_aux[i]) - 65
		 		#desconta as casas andadas ate a letra 'A'
		 		posicao-=soma
		 		#recebe a quantidade final de casas a andar a partir do -'Z'
		 		soma = 91 - posicao
		 		#recebe a nova letra
		 		aux_recebedora.append(chr(soma))
		 	#caso não chegue no -'Z'
		 	else:
		 		#recebe o numero da tabela ascii referente ao caractere
		 		soma = ord(str_aux[i])
		 		#desconta as posições andadas
		 		soma -= posicao
		 		#recebe a nova letra
		 		aux_recebedora.append(chr(soma))
		 #junta todos os caracteres em uma string
		 juncao = ''.join(aux_recebedora)
		 #adiciona a nova senha em uma lista
		 senha.append(juncao)
		 #limpa lista auxiliar para evitar replicas
		 aux_recebedora.clear()
	return senha
		 

#recebe a quantidade de senhas a armazenar		 
testes=int(input('Digite a quantidade de testes a serem feitos: '))
criptografias=[]
resultado=[]

#chama funcão para pedir as senhas do usuario
criptografias=recebe_valor(testes)
#chama função pra descriptografar as cifras
resultado = decodificador(criptografias)


for i in range(len(resultado)):
	print('{}° senha -> {}'.format(i+1, resultado[i]))
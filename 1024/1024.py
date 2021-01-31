#função que recebe os segredos do usuario
def recebe_segredo(valor):
	segredos=[]
	for i in range(valor):
		palavras = input('Digite seu {}° segredo\n'.format(i+1))
		segredos.append(palavras)
	return segredos

#primeira parte - modifica letras maiusculas e minusculas
def mod_letras(list_test):
	aux_modifica = []
	lista_tudo = []
	#loop para percorrer cada segredo
	for i in list_test:
		primeira_mod = ""
		modifica = i
		#loop para percorrer cada caractere do segredo
		for j in range(len(modifica)):
			#int_ascii recebe o valor inteiro equivalente ao caracter da posição 'j'
			int_ascii = ord(modifica[j])
			#verifica se o caracter é uma letra maiuscula ou minuscula
			if int_ascii > 64 and int_ascii < 91 or int_ascii > 96 and int_ascii < 123:
				#coloca o novo caracter segundo a tabela ascii
				aux_modifica.append(chr(int_ascii + 3))
			else:
				#coloca o caracter na posição novamente
				aux_modifica.append(modifica[j])
				
		#coloca a nova palavra na variavel	
		primeira_mod= ''.join(aux_modifica)
		#adiciona a nova palavra na lista
		lista_tudo.append(primeira_mod)
		#limpa a variavel para evitar replicas
		aux_modifica.clear()
	return lista_tudo	

#segunda parte - inverte a posição dos caracteres do segredo
def inverso(list_test):
	inverso=[]
	#percorre cada segredo da lista
	for i in range(len(list_test)):
		#separa um unico elemento em uma variavel
		hash = list_test[i]
		#slice para obter o valor invertido
		invertido = hash[::-1]
		#adiciona o novo segredo em uma lista
		inverso.append(invertido)
		#invertido.clear()
	return inverso

#terceira parte - modifica a partir da metade da hash
def mod_metade(list_test):
	#variável que vai receber as transformações
	truncado = []
	lista_final=[]
	#percorrendo cada elemento da lista
	for i in list_test:
		str_aux=""
		recebe_elemento = i
		#verificando se a quantidade de caracteres da um numero par
		if len(recebe_elemento)%2==0:
			#percorrendo cada caractere do segredo
			for j in range(len(recebe_elemento)):
				#recebendo o valor inteiro da tabela ascii equivalente ao catactere da posição 'j'
				int_ascii = ord(recebe_elemento[j])
				#verificando se ja chegou na metade da string
				if j >= len(recebe_elemento)/2:
					#modifica o caractere uma casa a eaquerda pela tabela ascii
					truncado.append(chr(int_ascii-1))		
				else:
					#se não chegou na metade, o caractere volta para seu lugar
					truncado.append(recebe_elemento[j])
		#se o tamanho do elemento for impar			
		else:
			#percorre todos os caracteres do segredo
			for j in range(len(recebe_elemento)):
				#recebe o valor inteiro equivalente ao caracter na tabela ascii
				int_ascii = ord(recebe_elemento[j])
				#virifica se ja percorreu a metade do segredo
				if j >= len(recebe_elemento)/2 -1:
					#modifica o caractere uma casa a eaquerda pela tabela ascii
					truncado.append(chr(int_ascii-1))		
				else:
					#se não chegou na metade, o caractere volta para seu lugar
					truncado.append(recebe_elemento[j])
		#junta toda a lista em uma unica string
		str_aux = ''.join(truncado)
		#adiciona o novo segredo em uma lista
		lista_final.append(str_aux)
		#limpa a lista trabalhada para evitar copias
		truncado.clear()
	return lista_final


#pergunta quantas palavras serão lidas
quant_ent = int(input('Digite quantos testes deseja fazer: '))
entrada_inicial = []
primeira_mod=[]
segunda_mod=[]

#chama função para receber o segredo o usuario
entrada_inicial = recebe_segredo(quant_ent)
#chama a primeira função para modificar as letras
primeira_mod=mod_letras(entrada_inicial)
#chama a segunda função para inverter o segredo
segunda_mod = inverso(primeira_mod)
#chama a terceira função para modificar a partir da metade da string
terceira_mod = mod_metade(segunda_mod)

print('\nsegredo(s) inseridos\n')
for i in entrada_inicial:
	print('{}'.format(i))
	
print('-'*20)

print('\nNova(s) hash gerada')
for i in terceira_mod:
	print('{}'.format(i))
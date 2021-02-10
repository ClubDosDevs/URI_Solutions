#recebe as palavras
def pede_valor(valor):
	segredos=[]
	for i in range(valor):
		palavras = input('Digite a {}° palavra\n'.format(i+1))
		segredos.append(palavras)
	return segredos

def monta_triangulo(palavra):
	#lista pra trabalhar com cada string
	palavra_aux=[]
	for i in palavra:
		#o '^' é responsável pelo centralizado e o '20' pelo tamanho de espaços
		print('{:^20}'.format(i))
		palavra_aux=list(i)
		while True:
			#remove o ultimo elemento da lista
			palavra_aux.pop(len(palavra_aux)-1)
			aux=""
			#enquato a lista tiver algo dentro
			if bool(palavra_aux)==True:
				#junta a lista em uma unica string
				aux = ''.join(palavra_aux)
				print('{:^20}'.format(aux))
				#lista recebe a nova palavra sem o ultimo caractere
				palavra_aux=list(aux)
				
			#quando a lista estiver vazia esse teste acaba
			else:
				break
		#pra ficar bonitinho ^-^
		print('-=-'*20)
		

def main():
	palavras=[]
	quant_test=int(input('Digite a quantidade de testes: '))
	palavras=pede_valor(quant_test)
	monta_triangulo(palavras)
	
main()

def fatorial(n):
	if n==0:
		n=1
		return n
	elif n==1:
		return n
	return fatorial(n-1) * n

m=int(input('Primeiro Número: '))
n=int(input('Segundo Número: '))
fat1=fatorial(m)
fat2=fatorial(n)
print('='*20)
print('Soma do fatorial = {}'.format(fat1+fat2))

try: numero=int(input('Digite um número. '))
except: print('Caractere(s) não permitidos.');exit()
if numero <=0:
	print('Apenas números positivos.')
else:
	fatorial=1;i=2
	for _ in range(i-1, numero):
		fatorial=fatorial*i
		i=i+1
	print(fatorial)

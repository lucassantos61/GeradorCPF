
def geraNumeros():
	import random
	numeros = []
	x = 0
	while x < 9:
		numeros.append(random.randint(1,9))
		x +=1 
	return numeros

def geraVerificador(cpf,aux):
	x = 0
	total = 0
	while x < len(cpf):
		total += (cpf[x] * (aux))
		aux -= 1
		x+=1
	if(total%11 < 2 ):
		cpf.append(0)
	else:
		cpf.append(11 - (total%11))
	return cpf
def geraMascara(cpf):
	x = 0
	cpfaux = ''
	while x < len(cpf):
		cpfaux = cpfaux+cpf[x]
		if x == 2 or x == 5:
			cpfaux +='.'
		elif x == 8:
			cpfaux += '-'

		x +=1
	return cpfaux

def geraCPF():
	num = geraNumeros()
	temp = geraVerificador(num,10)
	temp = geraVerificador(temp,11)
	cpf =  "".join(str(i) for i in temp)
	
	return geraMascara(cpf)


print(geraCPF())	

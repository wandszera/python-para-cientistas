
# Em python temos diferentes tipos de variaveis, com diferentes formas de tratamento
# veremos aqui as principais para o minicurso

num_int = int(2) #int é a função que define um numero inteiro, ou seja, desconsidera decimais
num_int_2 = int(2.6)
print('Números inteiros:int()')
print(num_int,'Aqui ja tinhamos um número inteiro')
print(num_int_2, 'Aqui, como podemos ver só printou o numero inteiro\n')

#temos também claro, funções que consideram os decimais
print('Números decimais:float()')
num_dec = float(2.0)
num_dec_2 = float(2.912)

print(num_dec)
print(num_dec_2)

# As strings são uma sequencia de letras (mesmo se tiver números)
n1 = input('Digite um número:')
n2 = input('Digite outro numero:')


print(n1 + n2,'\n')
# Os números não foram somados pois são lidos como strings, realizando apenas a concatenação dos inputs
# para resolver isso basta usar uma das variáveis acima que é o int() ou o float()
n3 = float(input('Digite um número:'))
n4 = float(input('Digite outro número'))

print(n3 + n4)
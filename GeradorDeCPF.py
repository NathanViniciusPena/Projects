from random import randint
cpf_nove_digitos = ''
for i in range(9):
    cpf_nove_digitos += str(randint(0, 9))
print(cpf_nove_digitos)
cont = 10
resultado = 0
for n in cpf_nove_digitos: 
    resultado += (cont * int(n)) #Tansformamos o n em um numero inteiro, pois ele dentro da lista é uma str
    cont -= 1
    if cont == 1:
        break
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 #Esta é uma forma de fazer o if else direto, sem precisar do for
print(f'O primeiro digito do CPF é {digito_1}')
print('-='*15)
cont_2 = 11
resultado_2 = 0
cpf_dez_digitos = cpf_nove_digitos + str(digito_1)
for n_2 in cpf_dez_digitos: 
    resultado_2 += (cont_2 * int(n_2))
    cont_2 -= 1
    if cont_2 == 1:
        break
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'O segundo digito do CPF é {digito_2}')
print('=-'*15)
cpf_gerado = str(cpf_nove_digitos) + str(digito_1) + str(digito_2)
print(f'O CPF gerado foi: {cpf_gerado}')
print('-='*15)

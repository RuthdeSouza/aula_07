# Funções em Python inicia com a palavra
# reservada "def"
# Funções são rotinas em seu conceito
# Funções
# São blocos de códigos que só serão executados, se forem chamados.


# def saudacao():
#     print('Olá Mundo!')


# saudacao()
# saudacao()
# saudacao()

# def mostrar_linha()
#     print(30'=')


# mostrar_linha()
# print('MODULO 01')
# mostrar_linha()
# print('ALGORITMOS')
# mostrar_linha()
# print('ANÁLISE DE DADOS')
# mostrar_linha()

# def saudacao(nome):
#     print(f'Olá {nome}')


# saudacao('João')

# nome = input('Informe o nome: ')
# saudacao(nome)

# def somar(a, b):
#     s = a + b
#     print()
#     return s 


# soma = somar(4, 5)
# print(f'O valor da variavel soma é {soma}')

def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input('Informe o número: '))
    n2 = int(input('Informe o número: '))

    soma = somar_numeros(n1, n2)
    print(soma)

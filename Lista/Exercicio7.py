"""7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. """

ano = int(input('Informe o ano que você nasceu :'))
mes = int(input('Informe o mês que você nasceu :'))
dia = int(input('Informe o dia que você nasceu :'))

idade: int = 2023-ano
Idade_em_dias: int = idade*365

print('Dias vividos: {} dias'.format(Idade_em_dias))

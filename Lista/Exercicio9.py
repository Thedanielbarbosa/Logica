"""9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
Calcular e escrever o valor do novo salário."""

sal = float(input('Informe o valor do salário do funcionário: R$'))
pro = float(input('Informe o valor do reajuste: '))

sal_reajuste = sal + (sal*pro/100)

print('o salario de R${:.2f}, após o reajuste de {:.0f}%, foi para R${:.2f}'.format(sal, pro, sal_reajuste))

"""10) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor
seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro,
calcular e escrever o custo final ao consumidor. """

fab = float(input('informe o valor de fabricação do carro: '))

imposto: float = 45
distribuidor: float = 28

val_imp: float = (fab*45/100)
val_dis: float = (fab*28/100)
val_con: float = fab+val_dis+val_imp

print('O custo final deo carro é de R${:.2f} '.format(val_con))

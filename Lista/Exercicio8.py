""" 8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
de eleitores."""

num_total = float(input('Informe o numero total de votos: '))
voto_branco = float(input('Informer o numero total de votos em branco: '))
voto_nulo = float(input('Informer o numero total de votos nulo: '))
validos = float(input('Informer o numero total de votos válidos: '))

por_voto_branco = (voto_branco * 100) / num_total
por_nulo = (voto_nulo * 100) / num_total
por_validos = (validos * 100) / num_total

print('A porcentagem de votos nulos é {:.1f}%\nA porcentagem de votos em branco é {:.1f}%'
      '\nA porcentagem de votos validos é {:.1f}%'.format(por_nulo, por_voto_branco, por_validos))

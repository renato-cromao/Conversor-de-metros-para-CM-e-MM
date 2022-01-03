titulo = ('CONVERSOR MÉTRICO')
print('*'*80)
print('{:^80}'.format(titulo))
print('*'*80)
print('')

print('''
Conversor de metros para:
Centímetros ----------(1)
Milímetros ------------(2)
''')
print('')
n1 = int(input('Informe para qual métrica deseja converter: '))
print('')

if n1 == 1:
    print('A métrica escolhida foi CENTÍMETROS:')
    v1 = float(input('Informe o valor em metros: '))
    conv = v1 * 100
    print('{} metros é o mesmo que {} centímetros'.format(v1, conv))

elif n1 == 2:
    print('A métrica escolhida foi MILÍMETROS:')
    v1 = float(input('Informe o valor em metros: '))
    conv = v1 * 1000
    print('{} metros é o mesmo que {} milímetros'.format(v1, conv))

else:
    print('Opção inválida.')

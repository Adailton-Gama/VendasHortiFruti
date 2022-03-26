print('MENU')
print()
print('1 - MAÇÃ')
print('2 - LARANJA')
print('3 - BANANA')
print()
print('Escolha a fruta que deseja comprar:')

preco_1 = float(2.30)
preco_2 = float(3.60)
preco_3 = float(1.85)

esc_fruta = int(input('Qual Fruta deseja comprar? '))
print()

fruta = 0
if esc_fruta == 1:
    qtd = int(input('Quantas unidades deseja comprar? '))
    fruta = 'Maçãs'
    precototal = qtd * 2.3
    print('Você comprou %i %s, o valor a ser pago é: R$ %.2f' % (qtd, fruta, precototal))
elif esc_fruta == 2:
    qtd = int(input('Quantas unidades deseja comprar? '))
    fruta = 'Laranjas'
    precototal = qtd * 3.60
    print('Você comprou %i %s o valor a ser pago é: R$ %.2f' % (qtd, fruta, precototal))
elif esc_fruta == 3:
    qtd = int(input('Quantas unidades deseja comprar? '))
    fruta = 'Bananas'
    precototal = qtd * 1.85
    print('Você comprou %i %s, o total a ser pago é: R$ %.2f' % (qtd, fruta, precototal))
else:
    print('Fruta Inexistente!')

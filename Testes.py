n = 1
cp = 0
ci = 0
while n != 0:
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        cp += 1
    else:
        ci += 1
print('O total de pares é: {} e impares: {}!'.format(cp, ci))
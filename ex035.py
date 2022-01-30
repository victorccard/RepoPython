# print('-+-'* 10)
# print('ANALISADOR DE TRIÂNGULOS')
# print('-+-' * 10)
# s1 = int(input('Primeiro segmento:'))
# s2 = int(input('Segundo segmento:'))
# s3 = int(input('Terceiro segmento:'))
# if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
#     print('Os segmentos acima PODEM FORMAR triângulo!')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR triângulo!')


nome = 'victor'
cores = {
    'limpa':'\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco':'\033[7;30m'
}

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
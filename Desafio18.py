'''import math
angulo = float(input('Informe um ângulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O Ângulo de {} tem o seno de:{:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tg))'''

from math import sin, cos, tan, radians
angulo = float(input('Informe o ângulo desejado: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cos))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tg))

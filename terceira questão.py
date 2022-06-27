#Faça um programa que, dados dois inteiros positivos e distintos, x e y, calcular o M.D.C.(Máximo Divisor Comum) de x e y.
from math import gcd #comecei impotanto,novamento, a biblioteca.
x = int(input('Dígite um número: ')) #pedi para que escolhece dois números.
y = int(input('Dígite outro número: '))
print('MDC({}, {}) = ' .format(x , y), end= '') #aqui fiz com que aparece na tela a forma representada do mdc como pedido em prova.
print (gcd(x , y)) #cálulo gerado pela biblioteca.

#Faça um programa em Python para calcular o fatorial de um número inteiro e positivo N e exibir
# o resultado no seguinte formato (por exemplo, para N = 5): 5 * 4 * 3 * 2 * 1 = 120

from math import factorial    #comecei importando a biblioteca.
n = int(input("Digite um número qualquer: ")) 
fac = factorial(n)   #trouxe a função da biblioteca que seria necessaria no momento.
print ('O fatorial do número {} é {}' .format(n, fac))  #fiz o print com o resultado usando .format para substituir.

#também fiz da forma ensinada em sala de aula.
n = int(input("Digite um número qualquer: ")) #começo fazendo a introdução novamente. 
c = n #atribuição de c para n 
fac = 1 #coloquei para que o fator nulo da multipliação funiona-se
print ('{}! = ' .format(n)) #print para que o resultado saia com o número escolhido em fatorial.
while c > 0: #usando while para que haja uma repetição dos números.
    print(c, end = '') #números que sairam em tela pelo uso do while
    print(' * ' if c>1 else ' = ', end = '') #ao ver algumas videos aulas, aprendi que pode utilizar if no print, fazendo com que o cog fique menor 
    fac *=c #conta para que o resultado das multiplicações.
    c-=1 #atribuição para que os múmeros imprimidos em tela diminuam menos um. 
print (fac) #resultado final.

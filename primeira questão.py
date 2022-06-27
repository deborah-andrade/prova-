#Faça um programa em Python que irá ler uma data através de três valores inteiros.

mesim =[1, 3, 5, 7, 8, 10, 12] #mes impares e pares
mespa = [4, 6, 9,11]
bi = 2020
d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))
  
if  a > 2022 and a < 1900: #conferi ano
  print('Data Inválida!')
elif 0 < m >= 12: #conferi se mes ta no intevalo
  print('Data Inválida!')
elif 0 < d >= 31: #conferi se dia ta no intevalo
  print('Data inválida!')
elif m in mesim:
  if 0 < d <=31:
    print('{}/{}/{} Data Válida.'.format(d, m, a))
  else:
    print('Data Invalida!')
elif m in mespa:
  if 0 < d <= 30:
    print('{}/{}/{} Data Válida!')
  else:
    print('Data Inválida!')
elif m == 2:
  if d == 29:
    if a == bi:
      print('{}/{}/{} Data Válida.'.format(d, m, a))
    else:
      while True:
        bi = bi - 4
        print(bi)
        if bi <= a:
          break
      if bi == a:
        print('{}/{}/{} Data Válida.'.format(d, m, a))
  if d <= 28:
    print('{}/{}/{} Data Válida.'.format(d, m, a))

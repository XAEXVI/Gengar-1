import json

eb = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de braço.text')
contenteb = eb.read()
eb.close()

ep = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de perna.text')
contentep = ep.read()
ep.close()

print('Inicializando sua lista por favor escolha o grupo muscular que deseja')
gm = input('Braço ou Perna? ')

if gm == 'Braço':
    print(contenteb)
elif gm == 'Perna':
    print(contentep)

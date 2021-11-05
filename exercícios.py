import re
import json
from os import name


eb = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de braço.text')
contenteb = eb.read()
eb.close()

ep = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de perna.text')
contentep = ep.read()
ep.close()

eo = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de ombro.text')
contenteo = eo.read()
eo.close()

et = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de peito.text')
contentet = et.read()
et.close()

ec = open(r'C:\Users\fakea\Documents\Curso python\software de exercícios\exercícios de costa.text')
contentec = ec.read()
ec.close()

print('Inicializando THE COACH por favor insira seu detalhes.')
name = input('Qual é o seu nome? ')
peso = input('Quanto você está pesando? ')
altura = input('Qual é sua Altura? ')
nivel = input('Na musculação, você se considera(Amador, Intermediário, Experiente? ')
objetivo = input('Qual é seu objetivo(Emagrecer ou Ganhar Massa)? ')

if nivel + objetivo == 'Amador''Emagrecer':
    rep = '3x12'
    print('Já que você está começando agora e seu objetivo é emagracer, eu não vou pegar muito pesado, começaremos com 3x12(3 Séries de 12 repetições)')
else:
    if nivel + objetivo == 'Amador''Ganhar Massa':
        rep = '3x8'
        print('Se você quer ganhar massa, então teremos um treino de força, mas para não te lesionar, vamo começar com 3x8(3 Séries de 8 repetições) com o peso um pouco acima do normal')
    else:
        if nivel + objetivo == 'Intermediário''Emagrecer':
            rep = '3x15'
            print('Vamos pegar um pouco mais pesado, eu quero 3x15(3 séries de 15 repetições) com mais carga ')
        else:
            if nivel + objetivo == 'Intermediário''Ganhar Massa':
                rep = '4x10'
                print('Ta na hora de subir um degrau, 4x10(4 séries de 10 repetições) com a carga bem alta')
            else:
                if nivel + objetivo == 'Experiente''Emagrecer':
                    rep = '4x15'
                    print('O Segredo para emagrecer sendo avançado é, cargas altas e 4x15(4 Séries de 15).')
                else :
                    if nivel + objetivo == 'Experiente''Ganhar Massa':
                        rep = 'Máximo de carga possível, até a falha'
                        print('Se você é experiente e quer ganhar massa, vamo pra cima, eu quero o seu limite de carga, ATÉ A FALHA.')

print('')

escolha = input('Agora que já sabemos o seu nível, posso te mostrar uma lista de exercícios?: ')
if escolha == 'Sim':
    gm = input('Tudo bem, agora escolha um grupo muscular: Braço, Peito, Ombro, Costas ou Perna? ')
    if gm == 'Braço':
        print('Preparando sua ficha')
        print('____________________')
        print('Nome:', name,'\nPeso:', peso,'kg', '\nAltura:', altura,'metros', '\nNível:', nivel, '\nObjetivo:', objetivo ,'\nExercícios:','\n', rep , contenteb, '\n',rep,'de cada')
    elif gm == 'Perna':
        print('Preparando sua ficha')
        print('____________________')
        print('Nome:', name,'\nPeso:', peso,'kg', '\nAltura:', altura,'metros', '\nNível:', nivel, '\nObjetivo:', objetivo ,'\nExercícios:','\n', rep , contentep, '\n',rep,'de cada')
    elif gm == 'Peito':
        print('Preparando sua ficha')
        print('____________________')
        print('Nome:', name,'\nPeso:', peso,'kg', '\nAltura:', altura,'metros', '\nNível:', nivel, '\nObjetivo:', objetivo ,'\nExercícios:','\n',  rep ,contentet, '\n',rep,'de cada')
    elif gm == 'Ombro':
        print('Preparando sua ficha')
        print('____________________')
        print('Nome:', name,'\nPeso:', peso,'kg', '\nAltura:', altura,'metros', '\nNível:', nivel, '\nObjetivo:', objetivo ,'\nExercícios:', '\n',rep , contenteo, '\n',rep,'de cada')
    elif gm == ('Costas'):
        print('Preparando sua ficha')
        print('____________________')
        print('Nome:', name,'\nPeso:', peso,'kg', '\nAltura:', altura,'metros', '\nNível:', nivel, '\nObjetivo:', objetivo ,'\nExercícios:',contentec, '\n',rep,'de cada')
print('')
print('Obrigado por usar o THE COACH.')

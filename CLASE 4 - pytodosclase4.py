# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 02:44:58 2022

@author: Franco Fabián
"""

str1 = 'Buen'
str2 = 'día'
saludo = str1 + str2
print(saludo)

str3 = '123'
str4 = '123'+1

x = int(str3)+1
print(x)

casa = 'ISODEC'
letra = casa[1]
print(letra)

x = 3
y = casa[x-1]
print(y)

print(casa[2:4])

casa = 'ISODEC'
letra = casa[6]
print(letra)

casa = 'ISODEC'
print(len(casa))


casa = 'ISODEC'
inicio=0
while inicio < len(casa):
    letra = casa[inicio]
    print(letra)
    inicio=inicio+1 # poner 0 en lugar de inicio y hacer pregunta

casa = 'ISODEC'
for letra in casa:
    print(letra)

casa = 'ISODEC'
'I' in casa

'i' in casa

'M' in casa

if 'D' in casa:
    print('Encontrado')

casa = 'ISODEC'
pos = casa.find('DE')
print(pos)

nopos = casa.find('N')
print(nopos)

saludo = 'Hola clase'
reemp = saludo.replace('clase', 'mañana')
print(reemp)

reemp = saludo.replace('a','x')
print(reemp)

saludo = '      Hola clase'
saludo.lstrip()

saludo.rstrip()

saludo.strip()

frase = 'Sigue el camino'
frase.startswith('Sigue')

frase.startswith('s')

data = 'De ffabian@isodec.com.pe Sab Ago 20:15:13 2022'

pos = data.find('@')
print(pos)

pos2 = data.find(' ',pos)
print(pos2)

host = data[pos+1:pos2]
print(host)

saludo = 'Hola\nclase'
saludo

print(saludo)

algo = 'x\ny'
print(algo)

len(algo)

file = open('mbox.txt')
for line in file:
    print(line)

texto = open('mbox.txt')
count = 0
for line in texto:
    count = count + 1
print('Número de líneas:',count)

texto = open('mbox.txt')
data = texto.read()
print(len(data))
8405
print(data[:20])

texto = open('mbox.txt')
for line in texto:
    if line.startswith('From:'):
        print(line)

texto = open('mbox.txt')
for line in texto:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)

texto = open('mbox.txt')
for line in texto:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

texto = open('mbox.txt')
for line in texto:
    line=line.strip()
    if not '@isodec.edu.pe' in line:
        continue
    print(line)

nombre = input('Ingresa el nombre del texto: ')
text = open(nombre)
count = 0
for line in texto:
    if line.startswith('Destinatario:'):
        count = count + 1
print('Hay',count,'destinatarios en',nombre)













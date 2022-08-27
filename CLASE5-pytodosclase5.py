# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 06:29:52 2022

@author: Franco Fabián
"""

amigos = ['Nora','Teo','Sonia']

oficina = ['silla','escritorio','computadora']

num = [1,2,3,4]

algo = [1,2,3,[4,5],6]


amigos = ['Nora','Teo','Sonia']
for amigo in amigos:
    print('Feliz día:',amigo)
print('Fin')

a = ['Nora','Teo','Sonia']
for b in a:
    print('Feliz día:',b)
print('Fin')

amigos = ['Nora','Teo','Sonia']
print(amigos[1])

amigos[1]='Bruno'
print(amigos)

saludo = 'Hola clase'
print(len(saludo))

z = [1,2,'Nora',7]
print(len(z))

print(range(3))

amigos = ['Nora','Teo','Sonia']
print(len(amigos))

print(range(len(amigos)))

amigos = ['Nora','Teo','Sonia']

for amigo in amigos:
    print('Feliz día',amigo)

for i in range(len(amigos)):
    amigo = amigos[i]
    print('Feliz día',amigo)

a = [1,2,3]
b = [4,5]
c = a + b
print(c)

num = [23,1,4,5,23,18]
num[1:3]
num[:4]
num[2:]
num[:]

var = list()
var.append('escritorio')
var.append(20)
print(var)

var.append('cuaderno')
print(var)

var = [1,2,3,4,5]
4 in var

7 in var

14 not in var

var = [2,4,1,20,3,15,37]

print(len(var))

print(max(var))

print(min(var))

print(sum(var))

print(sum(var)/len(var))


total=0
count=0
while True:
    inp=input('Ingrese un número:')
    if inp == 'fin': break
    val=float(inp)
    total=total+val
    count=count+1
prom=total/count
print('El promedio es:',prom)


numlist=list()
while True:
    inp=input('Ingrese un número:')
    if inp == 'fin': break
    val=float(inp)
    numlist.append(val)
prom=sum(numlist)/len(numlist)
print('El promedio es:',prom)

line='Tengo      mucho espacio'
var=line.split()
print(var)

line='primero;segundo;tercero'
var=line.split()
print(var)

print(len(var))

var=line.split(';')
print(var)
print(len(var))


line='From franco.fabian@isodec.com.pe Sab Ago 10:15:12 2022'
palabra=line.split()
print(palabra)

texto = open('mbox.txt')
for line in texto:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue

    palabra=line.split()
    print(palabra[2])


col=dict()
col['dinero']=12
col['caramelo']=3
col['papel']=20
print(col)

print(col['dinero'])

col['caramelo']=col['caramelo']+2
print(col)

col={'dinero':12,'caramelo':3,'papel':20}
print(col)

vac={}
print(vac)

col=dict()
nombres=['Nora','Teo','Sonia','Nora','Teo']
for nombre in nombres:
    if nombre not in col:
        col[nombre]=1
    else:
        col[nombre]=col[nombre]+1
print(col)

if nombre in col:
    x=col[nombre]
else:
    x=0

x=col.get(nombre,0)

col=dict()
nombres=['Nora','Teo','Sonia','Nora','Teo']
for nombre in nombres:
    col[nombre]=col.get(nombre,0)+1
print(col)


texto='Oh! Cuánto tiempo silenciosa el alma'
texto.split()
print(texto)

col=dict()
line=input('Ingrese texto:')
palabras=line.split()
for palabra in palabras:
    col[palabra]=col.get(palabra,0)+1
print('La cantidad de palabras es:',col)

col={'dinero':12,'caramelo':3,'papel':20}
print(list(col))

print(col.keys())

print(col.values())

print(col.items())

col={'dinero':12,'caramelo':3,'papel':20}

for aaa,bbb in col.items():
    print(aaa,bbb)

nombre=input('Ingrese texto:')
texto=open(nombre)

col=dict()
for line in texto:
    palabras=line.split()
    for palabra in palabras:
        col[palabra]=col.get(palabra,0)+1

mayorconteo=None
mayorpalabra=None
for palabra,conteo in col:
    if mayorconteo is None or conteo > mayorconteo:
        mayorpalabra=palabra
        mayorconteo=conteo

print(mayorpalabra,mayorconteo)





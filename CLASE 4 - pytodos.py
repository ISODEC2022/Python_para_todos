# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:31:48 2022

@author: Franco Fabián
"""

'''
Primera clase
'''

x=1
print(x)
x=x+1
print(x)

x=0.5
x=2.5*x*(2-x)


23%5

x = 2 + 2**4 / 2 *5
print(x)

# Integers
x = 1
y = 2
z = 3. # no entero

print(type(x), type(y), type(z))

z = int(3.2)
print(z, type(z))

# Floats
x = 1.2
y = 22*3.33
z = 1.4

print(type(x), type(y), type(z))

entero = int(5)
print(x+entero)
print(y-entero)
print(z*entero)
print(z/entero)
print(entero/z)

# String
x = 'Python "básico"'
y = 'primera'
z = 'clase'

print(x + y + z)
print(x, y, z)

# Boolean
print(type(True))
print(False)

# Arrays
nombres = ['Carlos', 'Nora', 'Pedro']
print(nombres[0])
print(len(nombres))
print(type(nombres))

# List
milista = [1, 3.2, 'Text', True]

print(milista[0])
print(len(milista))
print(type(milista))

nombre=input('¿Quién eres?')
print('Hola',nombre)

x='hola'
type(x)

a=10
b=float(a)
print(b)
type(b)

float(a)
type(a)


entrada = input('Número de orden ')
ordpy = int(entrada)-1
print('El orden en Python es:',ordpy)


x = 2
x=x+10
print(x)

n =3+6**2/3*2
print(n)
type(n)

entrada = input('Número de orden ')
ordpy = int(entrada)-1
print('El orden en Python es:',ordpy)


horas = input('Ingrese horas trabajadas:')
salario = input('Ingrese pago por hora:')
h=int(horas)
s=int(salario)
pago = h * s
print(pago)

'''
Segunda clase
'''

def mifuncion(lugar):
    if lugar == 1:
        print('Primer')
    elif lugar == 2:
        print('Segundo')
    else:
        print('Tercer')

mifuncion(3)







def mifuncion(lugar):
    if lugar == 1:
        print('Primer')
    elif lugar == 2:
        print('Segundo')
    elif lugar == 3:
        print('Tercer')
    else:
        print('No es podio')

mifuncion(3)

def mifuncion(lugar):
    if lugar == 1:
        return 'Primer'
    elif lugar == 2:
        return 'Segundo'
    else:
        return 'Tercer'

mifuncion(2)

print(mifuncion(1),'puesto')


n=5

n=0

while n>0:
    print('Nunca')
    print('Acaba')
print('Fin')


mayor=-1
print('Inicio',mayor)
for numero in [4,10,23,18,30,77,7,5]:
	if numero > mayor:
		mayor=numero
	print(mayor,numero)
print('Fin',mayor)

contar=0
print('Inicio',contar)
for numero in [4,10,23,18,30,77,7,5]:
	contar = contar + 1
	print(contar,numero)
print('Fin',contar)

sumar=0
print('Inicio',sumar)
for numero in [4,10,23,18,30,77,7,5]:
	sumar = sumar + numero
	print(sumar,numero)
print('Fin',sumar)

contar=0
sumar=0
print('Inicio',contar,sumar)
for numero in [4,10,23,18,30,77,7,5]:
	contar=contar+1
	sumar = sumar + numero
	print(sumar,contar,numero)
print('Fin',contar,sumar,sumar/contar)


print('Inicio')
for numero in [4,10,23,18,30,77,7,5]:
	if numero > 20:
		print('Número grande',numero)
print('Fin')


busqueda = False
print('Inicio',busqueda)
for numero in [4,10,23,18,30,77,7,5]:
	if numero == 30:
		busqueda=True
	print(busqueda,numero)
print('Fin',busqueda)


menor=-1
#10,100,100000000
print('Inicio',menor)
for numero in [4,10,23,18,30,77,7,5]:
	if numero < menor:
		menor=numero
	print(menor,numero)
print('Fin',menor)




menor = None
print('Inicio')
for numero in [4,10,23,18,30,77,7,5]:
	if menor is None:
		menor=numero
	elif numero < menor:
		menor=numero
	print(menor,numero)
print('Fin',menor)


x=5
if  x == 5 :
    print('Es 5')
    print('Sigue 5')
print('Aún 5')


x  =   7
if x < 2:
	print('Pequeño')
elif x < 8:
	print('Mediano')
elif x < 10:
	print('Grande')

def algo():
    print('Hola')
print('Sábado')

def algo1():
    print('Hola')
    return
    print('Mundo')
algo()

n = 5
while n > 0 :
    print(n)
print('Hecho')

amigos = ['Luis', 'Nora', 'Mou']
for amigo in amigos :
     print('Feliz día:',  amigo)
print('Fin')


horas = [10,8,9,7,10]

tiempo = 0
dias = 0

for hora in horas:
    dias = dias + 1
    tiempo = tiempo + hora

print('El promedio de horas trabajadas es de:',tiempo/dias,'horas')

'''
Tercera clase
'''

# Pregunta 1

# Importar librería Pandas

import pandas as ppp

# Importar librería Math

import math

ruta='D:\clase3'

b=pandas.read_excel(ruta+'\base.xlsx')

b=pd.read_excel(ruta+'\base.xlsx')

b=ppp.read_excel(ruta+'\base.xlsx')








# Pregunta 2

round(2.6)+math.ceil(2.2)







# Pregunta 3

# Ver script

# Pregunta 4

# Ver script

# Pregunta 5

# Ver script

# Pregunta 6

# Ver script

# Pregunta 7


b1['var_2'] = b1['var_1']*'3000'



'''
Cuarta clase
'''

# Pregunta 1

x = '10'
y= int(x) + 2
print(y)

# Pregunta 2

casa = 'ISODEC'
inicio=0
while inicio < len(casa):
    letra = casa[inicio]
    print(letra)
    inicio=0+1

# Pregunta 3

data = 'Para ffabian.isodec@com.pe Sab Ago'
pos = data.find('.')
print(data[pos:pos+4])




























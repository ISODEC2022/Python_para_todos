# -*- coding: utf-8 -*-


nombre = input('Ingrese el nombre del documento:')
texto = open(nombre)

counts = dict()
for line in texto:
        palabras = line.split()
        for palabra in palabras:
            counts[palabra] = counts.get(palabra,0) + 1

mayorcount = None
mayorpalabra = None
for palabra,count in counts.items():
    if mayorcount is None or count > mayorcount:
        mayorpalabra = palabra
        mayorcount = count

print(mayorpalabra,mayorcount)




















# Pregunta 1

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))
























# Pregunta 2

fname = input('Ingrese el nombre del documento:')
fh = open(fname)
lst = list()
for line in fh:

    line=line.rstrip()
    words=line.split()

    for line2 in words:

        if line2 in lst:
            continue

        else:
            lst.append(line2)

lst.sort()
print(lst)











# Pregunta 3

fname = input('Ingrese el nombre del documento:')
fh = open(fname)
count = 0

for line in fh:
    line=line.rstrip()
    if not line.startswith('From:'):
        continue
    words=line.split()

    print(words[1])
    count=count+1


print('Hay', count, 'líneas que empiezan con From')


























# Pregunta 4




# Pregunta 5

nombre = input('Ingrese el nombre del documento:')
texto = open(nombre)

counts = dict()
for line in texto:
    if line.startswith('From:'):
        palabra1 = line.split()
        palabra2 = palabra1[1]
        if palabra2 not in counts:
            counts[palabra2] = 1
        else:
            counts[palabra2] = counts[palabra2] + 1

mayorcount = None
mayorpalabra = None
for palabra,count in counts.items():
    if mayorcount is None or count > mayorcount:
        mayorpalabra = palabra
        mayorcount = count

print(mayorpalabra,mayorcount)


counts[palabra] = counts.get(palabra,0) + 1

nombre = input('Ingrese el nombre del documento:')
texto = open(nombre)

counts = dict()
for line in texto:
    if line.startswith('From:'):
        palabra1 = line.split()
        palabra2 = palabra1[1]
        if palabra2 not in counts:
            counts[palabra2] = counts.get(palabra2,0) + 1

mayorcount = None
mayorpalabra = None
for palabra,count in counts.items():
    if mayorcount is None or count > mayorcount:
        mayorpalabra = palabra
        mayorcount = count

print(mayorpalabra,mayorcount)

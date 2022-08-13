# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 04:08:52 2022

@author: Franco Fabián
"""

'''
Importar librerías
'''
# Importar librería Pandas

import pandas as pd

# Importar librería Math

import math

# Importar librería dbfread

from dbfread import DBF

'''
Definir ruta
'''

# Ruta del directorio: D:\curso isodec\clase3

ruta='D:\curso isodec\clase3'

# Ruta de archivos de entrada: D:\curso isodec\clase3\Input

ruta_input=ruta+'\Input'

# Ruta de archivos de salida: D:\curso isodec\clase3\Output

ruta_output=ruta+'\Output'

'''
Importar bases
'''

# Importar base

b1=pd.read_excel(ruta_input+'\Primera_base.xlsx',sheet_name='Hoja1',nrows=9,header=3,usecols='A:L')

'''
Exportar bases
'''

b1.to_excel(ruta_output+'\Base_exportada.xlsx', sheet_name='taller' , index= False)

'''
Verificar y cambiar tipo de variables
'''

print(b1.dtypes)

b1['Código Pliego']=b1['Código Pliego'].astype(str)
b1.Docente=b1.Docente.astype(str)

b1['Código Pliego']=b1['Código Pliego'].astype(int)
b1.Docente=b1.Docente.astype(int)

'''
Generar variables
'''

monto_doce=3000

meses_activo10=['mar','abr','may','jun','jul','ago','set','oct','nov','dic']

b1['p1']=22

b1['p2']='22'

print(b1.dtypes)

b1['IE']=b1['Nombre IE']

'''
Renombrar variables
'''

# Eliminar espacios de nombres de variables

b1.columns = b1.columns.str.rstrip()
b1.columns = b1.columns.str.lstrip()

# Renombrar variables

b1.rename(columns={'Código Pliego':'cod_pliego'},inplace=True)
b1.rename(columns={'Código de Ejecutora':'cod_ue'},inplace=True)
b1.rename(columns={'Código Local':'cod_local'},inplace=True)
b1.rename(columns={'Total de estudiantes':'n_estu'},inplace=True)
b1.rename(columns={'Docente':'n_doce'},inplace=True)
b1.rename(columns={'Coordinador':'coor'},inplace=True)
b1.rename(columns={'Personal de Seguridad':'segu'},inplace=True)
b1.rename(columns={'Código Modular':'cod_mod'},inplace=True)
b1.rename(columns={'Pliego':'pliego'},inplace=True)
b1.rename(columns={'Ugel':'ugel'},inplace=True)

'''
Multiplicar variables
'''

b1['remu_doce'] = b1['n_doce']*monto_doce

b1['remu_doce_2'] = b1['n_doce']*3000

b1['resultado'] = b1['n_doce']*b1['coor']

'''
Generar variables usando for
'''

for mes in meses_activo10:
    b1['remu_doce_'+mes] = b1['n_doce']*monto_doce

'''
Eliminar variables
'''

del b1['ugel']

'''
Usar mínimo
'''

# Valor proyectado de UIT para el 2022

UIT_2022=4600

# Porcentaje para monto techo en EsSalud CAS

UIT_porc=0.45

# Tope de EsSalud

tope_essalud_menos=round(0.09*UIT_porc*UIT_2022)

tope_essalud_mas=math.ceil(0.09*UIT_porc*UIT_2022)

#b1['essalud_doce']=math.ceil(0.09*monto_doce)

b1['essalud_doce']=min(math.ceil(0.09*monto_doce),tope_essalud_mas)

'''
Usar condicional
'''

b1.loc[(b1['cod_pliego']==453)&(b1['cod_ue']==305),'var_1'] = 100
b1.loc[(b1['cod_pliego']==453) | (b1['cod_ue']==305),'var_2'] = 100

'''
Quitar valores NA
'''

#b1 = b1.dropna()

#b1 = b1.dropna(subset=['var_2'])

# Reemplzar NA por 0

b1 = b1.fillna(0)

#b1 = b1.fillna('')

'''
Agrupar (collapse)
'''
print(b1.dtypes)

b1.n_doce=b1.n_doce.astype(int)
b1.coor=b1.coor.astype(int)
b1.segu=b1.segu.astype(int)

# Agrupar usando el método groupby

b1_g=b1.groupby(['cod_mod'])[['n_doce','coor','segu']].sum()

# Quitar el índice de la base

b1_g_ri = b1_g.reset_index()

'''
Combinar (merge)
'''

# Importar segunda base

b2=pd.read_excel(ruta_input+'\Segunda_base.xlsx')

# Combinar usando inner

b1_g_ri_b2_1=pd.merge(b1_g_ri, b2, on ='cod_mod', how ='left', indicator=True)
b1_g_ri_b2_2=pd.merge(b1_g_ri, b2, on ='cod_mod', how ='right', indicator=True)
b1_g_ri_b2_3=pd.merge(b1_g_ri, b2, on ='cod_mod', how ='inner', indicator=True)
b1_g_ri_b2_4=pd.merge(b1_g_ri, b2, on ='cod_mod', how ='outer', indicator=True)

b2_b1_g_ri_1=pd.merge(b2, b1_g_ri, on ='cod_mod', how ='left', indicator=True)
b2_b1_g_ri_2=pd.merge(b2, b1_g_ri, on ='cod_mod', how ='right', indicator=True)
b2_b1_g_ri_3=pd.merge(b2, b1_g_ri, on ='cod_mod', how ='inner', indicator=True)
b2_b1_g_ri_4=pd.merge(b2, b1_g_ri, on ='cod_mod', how ='outer', indicator=True)

'''
Usar melt para pasar a long (reshape long)
'''
# Importar base

b3=pd.read_excel(ruta_input+'\Tercera_base.xlsx')

# Pasar a long

b3_long=pd.melt(b3, id_vars=['cod_pliego', 'cod_ue', 'cod_ugel','nom_pliego','nom_ue','ugel'], value_vars=b3.columns[[x.startswith('name') for x in b3.columns]].tolist(), var_name='s', value_name='name')

'''
Extraer números de una cadena
'''

b3_long['valor']=b3_long.s.str.extract('(\d+)')

b3_long['mes']=b3_long['s'].str.extract('(?:.*_)([0-9]+)')

#b3_long['valor2'] = b3_long['s'].str[6:]

'''
Usar pivot para pasar a wide (reshape wide)
'''

del b3_long['s']

b3_wide=b3_long.pivot(index=['cod_pliego', 'cod_ue', 'cod_ugel','valor','nom_pliego','nom_ue','ugel'], columns='mes', values='name').reset_index()

'''
Agregar ceros a la izquierda
'''

print(b3_wide.dtypes)

b3_wide.cod_ugel=b3_wide.cod_ugel.astype(str)

b3_wide['cod_ugel']= b3_wide['cod_ugel'].str.zfill(10)

'''
Ordenar por variables
'''

# Ordenar usando el método sort

b_ord=b3_wide.sort_values(by=['cod_ugel'])

# Odenar base por variables de interés

b_f=b_ord[['cod_pliego','nom_pliego','cod_ue','nom_ue','cod_ue','nom_ue','cod_ugel','ugel','1','2','3','4','5','6','7','8','9','10','11','12','13']]

'''
Usar startswith
'''
# Importar base

b4=pd.read_excel(ruta_input+'\Tercera_base.xlsx')

# Usar startswith

b4_st=b4.groupby(['cod_pliego','nom_pliego'])[b4.columns[[x.startswith('name1') for x in b4.columns]].tolist()].sum().reset_index()

'''
Usar endswith
'''
# Importar base

b5=pd.read_excel(ruta_input+'\Tercera_base.xlsx')

# Usar endswith

b5_st=b5.groupby(['cod_pliego','nom_pliego'])[b5.columns[[x.endswith('_13') for x in b5.columns]].tolist()].sum().reset_index()

# Sumar y almacenar en una variable

b5['var'] = b5[b5.columns[[x.endswith('_13') for x in b5.columns]].tolist()].sum(axis=1)

'''
Usar ESCALE
'''

# b) Importar Padrón web

# Generar DBF

b_dbf=DBF(ruta_input+'/Padron_web_20220809.dbf')

# Generar dataframe

padweb = pd.DataFrame(iter(b_dbf))

# Filtrar para estado igual a activa IE

padweb = padweb[padweb.D_ESTADO == 'Activa']

# Establecer df con variables de interés

padweb_i=padweb[['COD_MOD','CODOOII']]

# Verificar tipo de variables

print(padweb_i.dtypes)

# Pasar a integer

padweb_i.COD_MOD=padweb_i.COD_MOD.astype(int)
padweb_i.CODOOII=padweb_i.CODOOII.astype(int)

# Renombrar variables

padweb_i.rename(columns={'COD_MOD':'cod_mod'},inplace=True)
padweb_i.rename(columns={'CODOOII':'cod_ugel'},inplace=True)

# Importar base

b6=pd.read_excel(ruta_input+'\Segunda_base.xlsx')

# Combinar bases usando inner

b6_padweb=pd.merge(b6, padweb_i, on ='cod_mod', how ='inner')



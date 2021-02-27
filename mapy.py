# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:14:07 2020

@author: krizh
"""
import geopandas as gpd


f_admi = r"C:\Users\krizh\Documents\ArcCR500\AdministrativniCleneni_v13.gdb"

okresy_body = gpd.read_file(f_admi, layer=15)
okresy_hranice = gpd.read_file(f_admi, layer=16)
hranice = gpd.read_file(f_admi)
obce = gpd.read_file(f_admi, layer=9)
kraje_hranice = gpd.read_file(f_admi, layer=18)
mapa = gpd.read_file(r"C:\Users\krizh\Documents\ArcCR500\ArcCR500_v33.gdb")
obce = gpd.read_file(r"C:\Users\krizh\Documents\ArcCR500\ArcCR500_v33.gdb",driver='FileGDB', layer=0)
 

#%%
import fiona
x1 = fiona.listlayers(r"C:\Users\krizh\Documents\ArcCR500\AdministrativniCleneni_v13.gdb")
for i in x1:
    print(i)
print("\n")    
x2 = fiona.listlayers(r"C:\Users\krizh\Documents\ArcCR500\ArcCR500_v33.gdb")
for i in x2:
    print(i)
    
#%%

df1 = obce
bod = df1[df1['NAZ_OBEC'] == 'Psáry'] 
df = okresy_hranice
okres = df[df['NAZ_LAU1'] == 'Praha-západ'] 


ax = okres.plot()
bod.plot(color='red',ax=ax)

#%% notes
kraj = kraj.iloc[:2]
kraj = okres['geometry']
import gc
gc.collect()
    
    

    
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns
import webbrowser

datos = pd.read_csv('datos2.csv')
df = pd.DataFrame(datos)

#g=sns.lmplot(x='IMC', y='Edad', data=(df))
#df.groupby('IMC')['Edad'].plot(kind='bar', legend='Reverse')
g=sns.lmplot(x='Edad', y='IMC', data=df,hue='Categoria', col='Tipo', aspect=.4,x_jitter=.1)






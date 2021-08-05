
#!/usr/bin/env python3
import pandas as pd


data = pd.read_csv('https://raw.githubusercontent.com/csfeeser/Python/master/pokedex.txt', sep=",", header=None)
data.columns = data.iloc[0,:]
data = data[1:].apply(pd.to_numeric, errors='ignore')
poke_sum = data[['Type 1','HP','Attack','Defense','Speed']].groupby('Type 1').agg({'Type 1':['count'], 'HP':['mean'],'Attack':['mean'],'Defense':['mean'],'Speed':['mean']})

poke_sum.to_csv('poke_sum.csv')

print(pd.read_csv('poke_sum.csv'))

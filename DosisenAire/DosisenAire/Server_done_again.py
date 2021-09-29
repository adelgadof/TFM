import pandas as pd 
import numpy as np 


from datetime import datetime

time0 = datetime.now()

# Cuadrados 100

## 5x5

pddopen5 = pd.read_csv('OPEN/txt/5x5/5x5pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])
pcropen5 = pd.read_csv('OPEN/txt/5x5/5x5pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])
pinopen5 = pd.read_csv('OPEN/txt/5x5/5x5pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])

pddFFF5 = pd.read_csv('FFF/txt/5x5/5x5pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pcrFFF5 = pd.read_csv('FFF/txt/5x5/5x5pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pinFFF5 = pd.read_csv('FFF/txt/5x5/5x5pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])


## 10x10

pddopen10 = pd.read_csv('OPEN/txt/10x10/10x10pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])
pcropen10 = pd.read_csv('OPEN/txt/10x10/10x10pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])
pinopen10 = pd.read_csv('OPEN/txt/10x10/10x10pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])

pddFFF10 = pd.read_csv('FFF/txt/10x10/10x10pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pcrFFF10 = pd.read_csv('FFF/txt/10x10/10x10pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pinFFF10 = pd.read_csv('FFF/txt/10x10/10x10pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])


## 20x20

pddopen20 = pd.read_csv('OPEN/txt/20x20/20x20pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])
pcropen20 = pd.read_csv('OPEN/txt/20x20/20x20pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])
pinopen20 = pd.read_csv('OPEN/txt/20x20/20x20pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])

pddFFF20 = pd.read_csv('FFF/txt/20x20/20x20pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pcrFFF20 = pd.read_csv('FFF/txt/20x20/20x20pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pinFFF20 = pd.read_csv('FFF/txt/20x20/20x20pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])







## 40x40

pddopen40 = pd.read_csv('OPEN/txt/40x40/40x40pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])
pcropen40 = pd.read_csv('OPEN/txt/40x40/40x40pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])
pinopen40 = pd.read_csv('OPEN/txt/40x40/40x40pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])

pddFFF40 = pd.read_csv('FFF/txt/40x40/40x40pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pcrFFF40 = pd.read_csv('FFF/txt/40x40/40x40pro-cr-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pinFFF40 = pd.read_csv('FFF/txt/40x40/40x40pro-in-100.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])


# Cuadrados 115

## 5x5

pddopen5_115 = pd.read_csv('OPEN/txt/5x5/5x5pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])
pcropen5_115 = pd.read_csv('OPEN/txt/5x5/5x5pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])
pinopen5_115 = pd.read_csv('OPEN/txt/5x5/5x5pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])

pddFFF5_115 = pd.read_csv('FFF/txt/5x5/5x5pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pcrFFF5_115 = pd.read_csv('FFF/txt/5x5/5x5pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pinFFF5_115 = pd.read_csv('FFF/txt/5x5/5x5pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])


## 10x10

pddopen10_115 = pd.read_csv('OPEN/txt/10x10/10x10pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])
pcropen10_115 = pd.read_csv('OPEN/txt/10x10/10x10pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])
pinopen10_115 = pd.read_csv('OPEN/txt/10x10/10x10pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])

pddFFF10_115 = pd.read_csv('FFF/txt/10x10/10x10pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pcrFFF10_115 = pd.read_csv('FFF/txt/10x10/10x10pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pinFFF10_115 = pd.read_csv('FFF/txt/10x10/10x10pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])


## 20x20

pddopen20_115 = pd.read_csv('OPEN/txt/20x20/20x20pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])
pcropen20_115 = pd.read_csv('OPEN/txt/20x20/20x20pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])
pinopen20_115 = pd.read_csv('OPEN/txt/20x20/20x20pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])

pddFFF20_115 = pd.read_csv('FFF/txt/20x20/20x20pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pcrFFF20_115 = pd.read_csv('FFF/txt/20x20/20x20pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pinFFF20_115 = pd.read_csv('FFF/txt/20x20/20x20pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])


## 40x40

pddopen40_115 = pd.read_csv('OPEN/txt/40x40/40x40pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])
pcropen40_115 = pd.read_csv('OPEN/txt/40x40/40x40pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])
pinopen40_115 = pd.read_csv('OPEN/txt/40x40/40x40pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])

pddFFF40_115 = pd.read_csv('FFF/txt/40x40/40x40pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pcrFFF40_115 = pd.read_csv('FFF/txt/40x40/40x40pro-cr-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pinFFF40_115 = pd.read_csv('FFF/txt/40x40/40x40pro-in-115.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])


# 115

## 5x5

pddopen5_85 = pd.read_csv('OPEN/txt/5x5/5x5pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])
pcropen5_85 = pd.read_csv('OPEN/txt/5x5/5x5pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])
pinopen5_85 = pd.read_csv('OPEN/txt/5x5/5x5pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal open 5x5', 'error open 5x5'])

pddFFF5_85 = pd.read_csv('FFF/txt/5x5/5x5pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pcrFFF5_85 = pd.read_csv('FFF/txt/5x5/5x5pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pinFFF5_85 = pd.read_csv('FFF/txt/5x5/5x5pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 5x5', 'error fff 5x5'])


## 10x10

pddopen10_85 = pd.read_csv('OPEN/txt/10x10/10x10pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])
pcropen10_85 = pd.read_csv('OPEN/txt/10x10/10x10pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])
pinopen10_85 = pd.read_csv('OPEN/txt/10x10/10x10pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal open 10x10', 'error open 10x10'])

pddFFF10_85 = pd.read_csv('FFF/txt/10x10/10x10pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pcrFFF10_85 = pd.read_csv('FFF/txt/10x10/10x10pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pinFFF10_85 = pd.read_csv('FFF/txt/10x10/10x10pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 10x10', 'error fff 10x10'])


## 20x20

pddopen20_85 = pd.read_csv('OPEN/txt/20x20/20x20pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])
pcropen20_85 = pd.read_csv('OPEN/txt/20x20/20x20pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])
pinopen20_85 = pd.read_csv('OPEN/txt/20x20/20x20pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal open 20x20', 'error open 20x20'])

pddFFF20_85 = pd.read_csv('FFF/txt/20x20/20x20pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pcrFFF20_85 = pd.read_csv('FFF/txt/20x20/20x20pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pinFFF20_85 = pd.read_csv('FFF/txt/20x20/20x20pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 20x20', 'error fff 20x20'])


## 40x40

pddopen40_85 = pd.read_csv('OPEN/txt/40x40/40x40pdd.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])
pcropen40_85 = pd.read_csv('OPEN/txt/40x40/40x40pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])
pinopen40_85 = pd.read_csv('OPEN/txt/40x40/40x40pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal open 40x40', 'error open 40x40'])

pddFFF40_85 = pd.read_csv('FFF/txt/40x40/40x40pdd.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pcrFFF40_85 = pd.read_csv('FFF/txt/40x40/40x40pro-cr-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pinFFF40_85 = pd.read_csv('FFF/txt/40x40/40x40pro-in-85.txt', delimiter='		', engine='python', names=['r', 'señal fff 40x40', 'error fff 40x40'])


# Merge Data

## Z = 100; In = 1

FFF5 = pinFFF5.iloc[:,:2]
FFF5['FFF'] = 1
FFF5.columns = ['r', 'señal', 'FFF']
FFF5['Area'] = 25
FFF5['Limit'] = 25

Open5 = pinopen5.iloc[:,:2]
Open5['FFF'] = 0
Open5.columns = ['r', 'señal', 'FFF']
Open5['Area'] = 25
Open5['Limit'] = 25

FFF10 = pinFFF10.iloc[:,:2]
FFF10['FFF'] = 1
FFF10.columns = ['r', 'señal', 'FFF']
FFF10['Area'] = 100
FFF10['Limit'] = 50

Open10 = pinopen10.iloc[:,:2]
Open10['FFF'] = 0
Open10.columns = ['r', 'señal', 'FFF']
Open10['Area'] = 100
Open10['Limit'] = 50

FFF20 = pinFFF20.iloc[:,:2]
FFF20['FFF'] = 1
FFF20.columns = ['r', 'señal', 'FFF']
FFF20['Area'] = 400
FFF20['Limit'] = 100

Open20 = pinopen20.iloc[:,:2]
Open20['FFF'] = 0
Open20.columns = ['r', 'señal', 'FFF']
Open20['Area'] = 400
Open20['Limit'] = 100

FFF40 = pinFFF40.iloc[:,:2]
FFF40['FFF'] = 1
FFF40.columns = ['r', 'señal', 'FFF']
FFF40['Area'] = 1600
FFF40['Limit'] = 200

Open40 = pinopen40.iloc[:,:2]
Open40['FFF'] = 0
Open40.columns = ['r', 'señal', 'FFF']
Open40['Area'] = 1600
Open40['Limit'] = 200

MixedIN = pd.concat([Open5, FFF5, Open10, FFF10, Open20, FFF20, Open40, FFF40]) 
MixedIN['In'] = 1
MixedIN['Z'] = 100

## Z = 100; In = 0

FFF5 = pcrFFF5.iloc[:,:2]
FFF5['FFF'] = 1
FFF5.columns = ['r', 'señal', 'FFF']
FFF5['Area'] = 25
FFF5['Limit'] = 25

Open5 = pcropen5.iloc[:,:2]
Open5['FFF'] = 0
Open5.columns = ['r', 'señal', 'FFF']
Open5['Area'] = 25
Open5['Limit'] = 25

FFF10 = pcrFFF10.iloc[:,:2]
FFF10['FFF'] = 1
FFF10.columns = ['r', 'señal', 'FFF']
FFF10['Area'] = 100
FFF10['Limit'] = 50

Open10 = pcropen10.iloc[:,:2]
Open10['FFF'] = 0
Open10.columns = ['r', 'señal', 'FFF']
Open10['Area'] = 100
Open10['Limit'] = 50

FFF20 = pcrFFF20.iloc[:,:2]
FFF20['FFF'] = 1
FFF20.columns = ['r', 'señal', 'FFF']
FFF20['Area'] = 400
FFF20['Limit'] = 100

Open20 = pcropen20.iloc[:,:2]
Open20['FFF'] = 0
Open20.columns = ['r', 'señal', 'FFF']
Open20['Area'] = 400
Open20['Limit'] = 100

FFF40 = pcrFFF40.iloc[:,:2]
FFF40['FFF'] = 1
FFF40.columns = ['r', 'señal', 'FFF']
FFF40['Area'] = 1600
FFF40['Limit'] = 200

Open40 = pcropen40.iloc[:,:2]
Open40['FFF'] = 0
Open40.columns = ['r', 'señal', 'FFF']
Open40['Area'] = 1600
Open40['Limit'] = 200

MixedCR = pd.concat([Open5, FFF5, Open10, FFF10, Open20, FFF20, Open40, FFF40]) 
MixedCR['In'] = 0
MixedCR['Z'] = 100

## Z = 85; In = 1

FFF5 = pinFFF5_85.iloc[:,:2]
FFF5['FFF'] = 1
FFF5.columns = ['r', 'señal', 'FFF']
FFF5['Area'] = 25
FFF5['Limit'] = 25

Open5 = pinopen5_85.iloc[:,:2]
Open5['FFF'] = 0
Open5.columns = ['r', 'señal', 'FFF']
Open5['Area'] = 25
Open5['Limit'] = 25

FFF10 = pinFFF10_85.iloc[:,:2]
FFF10['FFF'] = 1
FFF10.columns = ['r', 'señal', 'FFF']
FFF10['Area'] = 100
FFF10['Limit'] = 50

Open10 = pinopen10_85.iloc[:,:2]
Open10['FFF'] = 0
Open10.columns = ['r', 'señal', 'FFF']
Open10['Area'] = 100
Open10['Limit'] = 50

FFF20 = pinFFF20_85.iloc[:,:2]
FFF20['FFF'] = 1
FFF20.columns = ['r', 'señal', 'FFF']
FFF20['Area'] = 400
FFF20['Limit'] = 100

Open20 = pinopen20_85.iloc[:,:2]
Open20['FFF'] = 0
Open20.columns = ['r', 'señal', 'FFF']
Open20['Area'] = 400
Open20['Limit'] = 100

FFF40 = pinFFF40_85.iloc[:,:2]
FFF40['FFF'] = 1
FFF40.columns = ['r', 'señal', 'FFF']
FFF40['Area'] = 1600
FFF40['Limit'] = 200

Open40 = pinopen40_85.iloc[:,:2]
Open40['FFF'] = 0
Open40.columns = ['r', 'señal', 'FFF']
Open40['Area'] = 1600
Open40['Limit'] = 200

MixedIN85 = pd.concat([Open5, FFF5, Open10, FFF10, Open20, FFF20, Open40, FFF40]) 
MixedIN85['In'] = 1
MixedIN85['Z'] = 85

FFF5 = pcrFFF5_85.iloc[:,:2]
FFF5['FFF'] = 1
FFF5.columns = ['r', 'señal', 'FFF']
FFF5['Area'] = 25
FFF5['Limit'] = 25

Open5 = pcropen5_85.iloc[:,:2]
Open5['FFF'] = 0
Open5.columns = ['r', 'señal', 'FFF']
Open5['Area'] = 25
Open5['Limit'] = 25

FFF10 = pcrFFF10_85.iloc[:,:2]
FFF10['FFF'] = 1
FFF10.columns = ['r', 'señal', 'FFF']
FFF10['Area'] = 100
FFF10['Limit'] = 50

Open10 = pcropen10_85.iloc[:,:2]
Open10['FFF'] = 0
Open10.columns = ['r', 'señal', 'FFF']
Open10['Area'] = 100
Open10['Limit'] = 50

FFF20 = pcrFFF20_85.iloc[:,:2]
FFF20['FFF'] = 1
FFF20.columns = ['r', 'señal', 'FFF']
FFF20['Area'] = 400
FFF20['Limit'] = 100

Open20 = pcropen20_85.iloc[:,:2]
Open20['FFF'] = 0
Open20.columns = ['r', 'señal', 'FFF']
Open20['Area'] = 400
Open20['Limit'] = 100

FFF40 = pcrFFF40_85.iloc[:,:2]
FFF40['FFF'] = 1
FFF40.columns = ['r', 'señal', 'FFF']
FFF40['Area'] = 1600
FFF40['Limit'] = 200

Open40 = pcropen40_85.iloc[:,:2]
Open40['FFF'] = 0
Open40.columns = ['r', 'señal', 'FFF']
Open40['Area'] = 1600
Open40['Limit'] = 200

MixedCR85 = pd.concat([Open5, FFF5, Open10, FFF10, Open20, FFF20, Open40, FFF40]) 
MixedCR85['In'] = 0
MixedCR85['Z'] = 85

FFF5 = pinFFF5_115.iloc[:,:2]
FFF5['FFF'] = 1
FFF5.columns = ['r', 'señal', 'FFF']
FFF5['Area'] = 25
FFF5['Limit'] = 25

Open5 = pinopen5_115.iloc[:,:2]
Open5['FFF'] = 0
Open5.columns = ['r', 'señal', 'FFF']
Open5['Area'] = 25
Open5['Limit'] = 25

FFF10 = pinFFF10_115.iloc[:,:2]
FFF10['FFF'] = 1
FFF10.columns = ['r', 'señal', 'FFF']
FFF10['Area'] = 100
FFF10['Limit'] = 50

Open10 = pinopen10_115.iloc[:,:2]
Open10['FFF'] = 0
Open10.columns = ['r', 'señal', 'FFF']
Open10['Area'] = 100
Open10['Limit'] = 50

FFF20 = pinFFF20_115.iloc[:,:2]
FFF20['FFF'] = 1
FFF20.columns = ['r', 'señal', 'FFF']
FFF20['Area'] = 400
FFF20['Limit'] = 100

Open20 = pinopen20_115.iloc[:,:2]
Open20['FFF'] = 0
Open20.columns = ['r', 'señal', 'FFF']
Open20['Area'] = 400
Open20['Limit'] = 100

FFF40 = pinFFF40_115.iloc[:,:2]
FFF40['FFF'] = 1
FFF40.columns = ['r', 'señal', 'FFF']
FFF40['Area'] = 1600
FFF40['Limit'] = 200

Open40 = pinopen40_115.iloc[:,:2]
Open40['FFF'] = 0
Open40.columns = ['r', 'señal', 'FFF']
Open40['Area'] = 1600
Open40['Limit'] = 200

MixedIN115 = pd.concat([Open5, FFF5, Open10, FFF10, Open20, FFF20, Open40, FFF40]) 
MixedIN115['In'] = 1
MixedIN115['Z'] = 115

FFF5 = pcrFFF5_115.iloc[:,:2]
FFF5['FFF'] = 1
FFF5.columns = ['r', 'señal', 'FFF']
FFF5['Area'] = 25
FFF5['Limit'] = 25

Open5 = pcropen5_115.iloc[:,:2]
Open5['FFF'] = 0
Open5.columns = ['r', 'señal', 'FFF']
Open5['Area'] = 25
Open5['Limit'] = 25

FFF10 = pcrFFF10_115.iloc[:,:2]
FFF10['FFF'] = 1
FFF10.columns = ['r', 'señal', 'FFF']
FFF10['Area'] = 100
FFF10['Limit'] = 50

Open10 = pcropen10_115.iloc[:,:2]
Open10['FFF'] = 0
Open10.columns = ['r', 'señal', 'FFF']
Open10['Area'] = 100
Open10['Limit'] = 50

FFF20 = pcrFFF20_115.iloc[:,:2]
FFF20['FFF'] = 1
FFF20.columns = ['r', 'señal', 'FFF']
FFF20['Area'] = 400
FFF20['Limit'] = 100

Open20 = pcropen20_115.iloc[:,:2]
Open20['FFF'] = 0
Open20.columns = ['r', 'señal', 'FFF']
Open20['Area'] = 400
Open20['Limit'] = 100

FFF40 = pcrFFF40_115.iloc[:,:2]
FFF40['FFF'] = 1
FFF40.columns = ['r', 'señal', 'FFF']
FFF40['Area'] = 1600
FFF40['Limit'] = 200

Open40 = pcropen40_115.iloc[:,:2]
Open40['FFF'] = 0
Open40.columns = ['r', 'señal', 'FFF']
Open40['Area'] = 1600
Open40['Limit'] = 200

MixedCR115 = pd.concat([Open5, FFF5, Open10, FFF10, Open20, FFF20, Open40, FFF40]) 
MixedCR115['In'] = 0
MixedCR115['Z'] = 115

Mixed = pd.concat([MixedCR, MixedIN, MixedCR85, MixedIN85, MixedCR115, MixedIN115]).reset_index(drop=True)

Mixed = Mixed.loc[:,['r', 'señal', 'FFF', 'Limit', 'In', 'Z']]

MixedNoFFF = Mixed[Mixed['FFF']==0].reset_index(drop=True)



print('Loading data finished')



# Ya tenemos todos los achivos cargados, ahora operamos sobre ellos, primero obtenemos la primera parte la 'Z' grande.



MixedNoFFF['Big Z'] = (0.25*50.9*42.6)/(MixedNoFFF['Z']**2)


print('Obtained Z')


# Ahora buscamos como obtener las 'T' grandes.







z_x_u = 43.1
z_y_u = 29.8

z_x_d = 50.9
z_y_d = 42.6


def pos_neg(number):

    x_01pos = []
    x_01neg = []
    x_02pos = []
    x_02neg = []
    y_01pos = []
    y_01neg = []
    y_02pos = []
    y_02neg = []

    for i in np.arange(number, MixedNoFFF.shape[0]):
        if MixedNoFFF[['In']].loc[i].to_numpy() == 1:
            x_01pos.append(float((z_x_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_u*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_u))))
            x_01neg.append(float((z_x_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() + z_x_u*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_u))))
            x_02pos.append(float((z_x_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_d*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_d))))
            x_02neg.append(float((z_x_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() + z_x_d*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_d))))


            y_01pos.append(float((z_y_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_u))))
            y_01neg.append(float((z_y_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_u))))
            y_02pos.append(float((z_y_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_d))))
            y_02neg.append(float((z_y_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_d))))


        else:    
            x_01pos.append(float((z_x_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_u))))
            x_01neg.append(float((z_x_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_u))))
            x_02pos.append(float((z_x_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_d))))
            x_02neg.append(float((z_x_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_x_d))))


            y_01pos.append(float((z_y_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_u*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_u))))
            y_01neg.append(float((z_y_u*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() + z_y_u*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_u))))
            y_02pos.append(float((z_y_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_d*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_d))))
            y_02neg.append(float((z_y_d*MixedNoFFF[['Limit']].loc[i].to_numpy()*MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_d*2*100*MixedNoFFF[['r']].loc[i].to_numpy())/(2*100*(MixedNoFFF[['Z']].loc[i].to_numpy() - z_y_d))))



    x_0pos = []
    for i, j in zip(x_01pos, x_02pos):
        if i<j:
            x_0pos.append(float(i))
        else:
            x_0pos.append(float(j))

    y_0pos = []
    for i, j in zip(y_01pos, y_02pos):
        if i<j:
            y_0pos.append(float(i))
        else:
            y_0pos.append(float(j))


    x_0neg = []
    for i, j in zip(x_01neg, x_02neg):
        if i<j:
            x_0neg.append(float(i))
        else:
            x_0neg.append(float(j))

    y_0neg = []
    for i, j in zip(y_01neg, y_02neg):
        if i<j:
            y_0neg.append(float(i))
        else:
            y_0neg.append(float(j))

    MixedIn0 = MixedNoFFF[MixedNoFFF['In']==0]
    MixedIn1 = MixedNoFFF[MixedNoFFF['In']==1]


    MixedNoFFF['xpos'] = x_0pos
    MixedNoFFF['xneg'] = x_0neg

    MixedNoFFF['ypos'] = y_0pos
    MixedNoFFF['yneg'] = y_0neg

pos_neg(0)
            
    

#Volviendo a la ecuación mostrada antes

# \\[ \Phi_\alpha = \frac{542.085}{z^2}* (\frac{\frac{x_0^+}{0.185}}{\sqrt{1+\frac{x_0^+}{0.185}}} + \frac{\frac{x_0^-}{0.185}}{\sqrt{1-\frac{x_0^-}{0.185}}}) * (\frac{\frac{y_0^+}{0.185}}{\sqrt{1+\frac{y_0^+}{0.185}}} + \frac{\frac{y_0^-}{0.185}}{\sqrt{1-\frac{y_0^-}{0.185}}}) \\]





print('Obtained pos and neg ts')

print(datetime.now()-time0)


# \\[ \Phi_\gamma (x,y,z) = w_0 \Phi_0(x,y,z) \Phi_{horn}^\gamma (x,y,z) \\]

# w_0 es la importancia de la fluencia primaria, que es la que estamos usando únicamente.

# \\[ \Phi_\gamma (x,y,z) = \Phi_0(x,y,z) * \Phi_{horn}^\gamma (x,y,z) \\]


# Por lo que tenemos ya una de las dos partes, ahora calculamos \\(\phi^\gamma_{horn}\\)

# \\[\Phi_{horn} = 1+ \rho^2\sum^4_{j=0} h_j^{\gamma, e} \rho^j \\]


 
print('Iterating...')


MixedNoFFF['Rho'] = np.abs(MixedNoFFF['r'])/(MixedNoFFF['Z'])

def Iterator(number):
    for delt0 in np.linspace(0.001, 4, number):

        Arg1 = (MixedNoFFF['xpos']/delt0)/((1 + (MixedNoFFF['xpos']/delt0)**2)**(1/2))
        Arg2 = (MixedNoFFF['xneg']/delt0)/((1 + (MixedNoFFF['xneg']/delt0)**2)**(1/2))

        Arg3 = (MixedNoFFF['ypos']/delt0)/((1 + (MixedNoFFF['ypos']/delt0)**2)**(1/2))
        Arg4 = (MixedNoFFF['yneg']/delt0)/((1 + (MixedNoFFF['yneg']/delt0)**2)**(1/2))
        
        for h0 in np.linspace(50, 300, number):
            for h1 in np.linspace(-7000, -2000, number):
                for h2 in np.linspace(30000, 80000, number):
                    for h3 in np.linspace(-450000, -1500000, number):
                        for h4 in np.linspace(800000, 200000, number):

                            MixedNoFFF['delta0 = ' + str(delt0) + ' h0 = ' + str(h0) + ' h1 = ' + str(h1) + ' h2 = ' + str(h2) + ' h3 = ' + str(h3) + ' h4 = ' + str(h4)] = MixedNoFFF['Big Z'] * (Arg1+Arg2) * (Arg3+Arg4) * (1 + MixedNoFFF['Rho']**2 * (h0 * MixedNoFFF['Rho'] + h1 * MixedNoFFF['Rho'] + h2 * MixedNoFFF['Rho'] + h3 * MixedNoFFF['Rho']+ h4 * MixedNoFFF['Rho']))

Iterator(2)
print(datetime.now()-time0)
             
                        
print('Finished iterations, now on to obtain both MAE from analytic equation and MAE from RF')

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler


RF = RandomForestRegressor()


y = MixedNoFFF[['señal']]

ScoresMAE = []
ScoresRF = []


def RFIterator(Start):
    for i in np.arange(Start, MixedNoFFF.shape[1]):

        x = MixedNoFFF.iloc[:,[i]]

        ScoresMAE.append(mean_absolute_error(x, y))
                        
        RFx = MixedNoFFF.iloc[:,[0, 3, 4, 5, 6, 7, 8, 9, 10, 11, i]]
                        
        x_train, x_test, y_train, y_test = train_test_split(RFx, y)
        
        RF.fit(x_train, np.ravel(y_train))
        ScoresRF.append((mean_absolute_error(RF.predict(x_test), y_test)))

RFIterator(12)

## Save best result and error associated
                     
                     
print('Best analytic solution MAE: ' + str(pd.DataFrame(ScoresMAE).sort_values(0).iloc[[0],:]))
print('Best RF solution MAE: ' + str(pd.DataFrame(ScoresRF).sort_values(0).iloc[[0],:]))

                     
MixedNoFFF.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, pd.DataFrame(ScoresMAE).sort_values(0).index[0]+12]].to_csv('x.csv')

MixedNoFFF.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,  pd.DataFrame(ScoresRF).sort_values(0).index[0]+12]].to_csv('RFX.csv')
print(datetime.now()-time0)

import pandas as pd 
import numpy as np 
pd.options.plotting.backend = 'plotly'

# Cuadrados 100

## 5x5

pddopen5 = pd.read_csv('OPEN/txt/5x5/5x5pdd.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])
pcropen5 = pd.read_csv('OPEN/txt/5x5/5x5pro-cr-100.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])
pinopen5 = pd.read_csv('OPEN/txt/5x5/5x5pro-in-100.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])

pddFFF5 = pd.read_csv('FFF/txt/5x5/5x5pdd.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pcrFFF5 = pd.read_csv('FFF/txt/5x5/5x5pro-cr-100.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pinFFF5 = pd.read_csv('FFF/txt/5x5/5x5pro-in-100.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])


## 10x10

pddopen10 = pd.read_csv('OPEN/txt/10x10/10x10pdd.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])
pcropen10 = pd.read_csv('OPEN/txt/10x10/10x10pro-cr-100.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])
pinopen10 = pd.read_csv('OPEN/txt/10x10/10x10pro-in-100.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])

pddFFF10 = pd.read_csv('FFF/txt/10x10/10x10pdd.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pcrFFF10 = pd.read_csv('FFF/txt/10x10/10x10pro-cr-100.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pinFFF10 = pd.read_csv('FFF/txt/10x10/10x10pro-in-100.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])


## 20x20

pddopen20 = pd.read_csv('OPEN/txt/20x20/20x20pdd.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])
pcropen20 = pd.read_csv('OPEN/txt/20x20/20x20pro-cr-100.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])
pinopen20 = pd.read_csv('OPEN/txt/20x20/20x20pro-in-100.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])

pddFFF20 = pd.read_csv('FFF/txt/20x20/20x20pdd.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pcrFFF20 = pd.read_csv('FFF/txt/20x20/20x20pro-cr-100.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pinFFF20 = pd.read_csv('FFF/txt/20x20/20x20pro-in-100.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])


## 40x40

pddopen40 = pd.read_csv('OPEN/txt/40x40/40x40pdd.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])
pcropen40 = pd.read_csv('OPEN/txt/40x40/40x40pro-cr-100.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])
pinopen40 = pd.read_csv('OPEN/txt/40x40/40x40pro-in-100.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])

pddFFF40 = pd.read_csv('FFF/txt/40x40/40x40pdd.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pcrFFF40 = pd.read_csv('FFF/txt/40x40/40x40pro-cr-100.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pinFFF40 = pd.read_csv('FFF/txt/40x40/40x40pro-in-100.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])


# Cuadrados 115

## 5x5

pddopen5_115 = pd.read_csv('OPEN/txt/5x5/5x5pdd.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])
pcropen5_115 = pd.read_csv('OPEN/txt/5x5/5x5pro-cr-115.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])
pinopen5_115 = pd.read_csv('OPEN/txt/5x5/5x5pro-in-115.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])

pddFFF5_115 = pd.read_csv('FFF/txt/5x5/5x5pdd.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pcrFFF5_115 = pd.read_csv('FFF/txt/5x5/5x5pro-cr-115.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pinFFF5_115 = pd.read_csv('FFF/txt/5x5/5x5pro-in-115.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])


## 10x10

pddopen10_115 = pd.read_csv('OPEN/txt/10x10/10x10pdd.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])
pcropen10_115 = pd.read_csv('OPEN/txt/10x10/10x10pro-cr-115.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])
pinopen10_115 = pd.read_csv('OPEN/txt/10x10/10x10pro-in-115.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])

pddFFF10_115 = pd.read_csv('FFF/txt/10x10/10x10pdd.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pcrFFF10_115 = pd.read_csv('FFF/txt/10x10/10x10pro-cr-115.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pinFFF10_115 = pd.read_csv('FFF/txt/10x10/10x10pro-in-115.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])


## 20x20

pddopen20_115 = pd.read_csv('OPEN/txt/20x20/20x20pdd.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])
pcropen20_115 = pd.read_csv('OPEN/txt/20x20/20x20pro-cr-115.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])
pinopen20_115 = pd.read_csv('OPEN/txt/20x20/20x20pro-in-115.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])

pddFFF20_115 = pd.read_csv('FFF/txt/20x20/20x20pdd.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pcrFFF20_115 = pd.read_csv('FFF/txt/20x20/20x20pro-cr-115.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pinFFF20_115 = pd.read_csv('FFF/txt/20x20/20x20pro-in-115.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])


## 40x40

pddopen40_115 = pd.read_csv('OPEN/txt/40x40/40x40pdd.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])
pcropen40_115 = pd.read_csv('OPEN/txt/40x40/40x40pro-cr-115.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])
pinopen40_115 = pd.read_csv('OPEN/txt/40x40/40x40pro-in-115.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])

pddFFF40_115 = pd.read_csv('FFF/txt/40x40/40x40pdd.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pcrFFF40_115 = pd.read_csv('FFF/txt/40x40/40x40pro-cr-115.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pinFFF40_115 = pd.read_csv('FFF/txt/40x40/40x40pro-in-115.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])


# 115

## 5x5

pddopen5_85 = pd.read_csv('OPEN/txt/5x5/5x5pdd.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])
pcropen5_85 = pd.read_csv('OPEN/txt/5x5/5x5pro-cr-85.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])
pinopen5_85 = pd.read_csv('OPEN/txt/5x5/5x5pro-in-85.txt', delimiter='		', names=['r', 'señal open 5x5', 'error open 5x5'])

pddFFF5_85 = pd.read_csv('FFF/txt/5x5/5x5pdd.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pcrFFF5_85 = pd.read_csv('FFF/txt/5x5/5x5pro-cr-85.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])
pinFFF5_85 = pd.read_csv('FFF/txt/5x5/5x5pro-in-85.txt', delimiter='		', names=['r', 'señal fff 5x5', 'error fff 5x5'])


## 10x10

pddopen10_85 = pd.read_csv('OPEN/txt/10x10/10x10pdd.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])
pcropen10_85 = pd.read_csv('OPEN/txt/10x10/10x10pro-cr-85.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])
pinopen10_85 = pd.read_csv('OPEN/txt/10x10/10x10pro-in-85.txt', delimiter='		', names=['r', 'señal open 10x10', 'error open 10x10'])

pddFFF10_85 = pd.read_csv('FFF/txt/10x10/10x10pdd.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pcrFFF10_85 = pd.read_csv('FFF/txt/10x10/10x10pro-cr-85.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])
pinFFF10_85 = pd.read_csv('FFF/txt/10x10/10x10pro-in-85.txt', delimiter='		', names=['r', 'señal fff 10x10', 'error fff 10x10'])


## 20x20

pddopen20_85 = pd.read_csv('OPEN/txt/20x20/20x20pdd.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])
pcropen20_85 = pd.read_csv('OPEN/txt/20x20/20x20pro-cr-85.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])
pinopen20_85 = pd.read_csv('OPEN/txt/20x20/20x20pro-in-85.txt', delimiter='		', names=['r', 'señal open 20x20', 'error open 20x20'])

pddFFF20_85 = pd.read_csv('FFF/txt/20x20/20x20pdd.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pcrFFF20_85 = pd.read_csv('FFF/txt/20x20/20x20pro-cr-85.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])
pinFFF20_85 = pd.read_csv('FFF/txt/20x20/20x20pro-in-85.txt', delimiter='		', names=['r', 'señal fff 20x20', 'error fff 20x20'])


## 40x40

pddopen40_85 = pd.read_csv('OPEN/txt/40x40/40x40pdd.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])
pcropen40_85 = pd.read_csv('OPEN/txt/40x40/40x40pro-cr-85.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])
pinopen40_85 = pd.read_csv('OPEN/txt/40x40/40x40pro-in-85.txt', delimiter='		', names=['r', 'señal open 40x40', 'error open 40x40'])

pddFFF40_85 = pd.read_csv('FFF/txt/40x40/40x40pdd.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pcrFFF40_85 = pd.read_csv('FFF/txt/40x40/40x40pro-cr-85.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])
pinFFF40_85 = pd.read_csv('FFF/txt/40x40/40x40pro-in-85.txt', delimiter='		', names=['r', 'señal fff 40x40', 'error fff 40x40'])


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

Mixed['r'] = np.abs(Mixed.loc[:,['r']])

Mixed = Mixed.loc[:,['r', 'señal', 'FFF', 'Area', 'In', 'Z']]




MixedF0 = Mixed[Mixed['FFF']==0].reset_index(drop=True)
MixedF00 = MixedF0[MixedF0['señal']>0.5]
MixedF00.reset_index(drop=True, inplace=True)



## Defining T plus and T minus





tplus_1 = []
tplus_2 = []

tplus_ = []



tminus_1 = []
tminus_2 = []

tminus_ = []


tplus1 = []
tplus2 = []

tplus = []



tminus1 = []
tminus2 = []

tminus = []


tplus_1 = []
tplus_2 = []

tplus_ = []



tminus_1 = []
tminus_2 = []

tminus_ = []


for k in np.arange(0, MixedF00.shape[0]):
    
    if MixedF00['In'][k]==1:
        tplus1.append(((MixedF00['Area'][k] * 43.1 + 2*np.abs(MixedF00['r'][k]) * -43.1)/(2*((MixedF00['Z'][k]) - 43.1))))
        tplus2.append(((MixedF00['Area'][k] * 50.9 + 2*np.abs(MixedF00['r'][k]) * -50.9)/(2*((MixedF00['Z'][k]) - 50.9))))
        tminus1.append(((MixedF00['Area'][k] * 43.1 - 2*np.abs(MixedF00['r'][k]) * -43.1)/(2*((MixedF00['Z'][k]) - 43.1))))
        tminus2.append(((MixedF00['Area'][k] * 50.9 - 2*np.abs(MixedF00['r'][k]) * -50.9)/(2*((MixedF00['Z'][k]) - 50.9))))
        
        tplus_1.append(((MixedF00['Area'][k] * 43.1)/(2*((MixedF00['Z'][k]) - 43.1))))
        tplus_2.append(((MixedF00['Area'][k] * 50.9)/(2*((MixedF00['Z'][k]) - 50.9))))
        tminus_1.append(((MixedF00['Area'][k] * 43.1)/(2*((MixedF00['Z'][k]) - 43.1))))
        tminus_2.append(((MixedF00['Area'][k] * 50.9)/(2*((MixedF00['Z'][k]) - 50.9))))
    else :
        tplus1.append(((MixedF00['Area'][k] * 29.8 + 2*np.abs(MixedF00['r'][k]) * -29.8)/(2*((MixedF00['Z'][k]) - 29.8))))
        tplus2.append(((MixedF00['Area'][k] * 42.6 + 2*np.abs(MixedF00['r'][k]) * -42.6)/(2*((MixedF00['Z'][k]) - 42.6))))
        tminus1.append(((MixedF00['Area'][k] * 29.8 - 2*np.abs(MixedF00['r'][k]) * -29.8)/(2*((MixedF00['Z'][k]) - 29.8))))
        tminus2.append(((MixedF00['Area'][k] * 42.6 - 2*np.abs(MixedF00['r'][k]) * -42.6)/(2*((MixedF00['Z'][k]) - 42.6))))

        tplus_1.append(((MixedF00['Area'][k] * 43.1)/(2*((MixedF00['Z'][k]) - 43.1))))
        tplus_2.append(((MixedF00['Area'][k] * 50.9)/(2*((MixedF00['Z'][k]) - 50.9))))
        tminus_1.append(((MixedF00['Area'][k] * 43.1)/(2*((MixedF00['Z'][k]) - 43.1))))
        tminus_2.append(((MixedF00['Area'][k] * 50.9)/(2*((MixedF00['Z'][k]) - 50.9))))

        
                
                
for i, j in zip(tplus1, tplus2):
    if i <= j :
        tplus.append(i)
    else:
        tplus.append(j)
        
for i, j in zip(tminus1, tminus2):
    if i <= j :
        tminus.append(i)
    else:
        tminus.append(j)
        
for i, j in zip(tplus_1, tplus_2):
    if i <= j :
        tplus_.append(i)
    else:
        tplus_.append(j)
        
for i, j in zip(tminus_1, tminus_2):
    if i <= j :
        tminus_.append(i)
    else:
        tminus_.append(j)

        
MixedF00['tplus'] = tplus 
MixedF00['tminus'] = tminus 
MixedF00['tplus_'] = tplus_
MixedF00['tminus_'] = tminus_  

## Obtaining Phi0



MixedF00['phi0 minus delta'] = ((542.085/(MixedF00['Z'].to_numpy())**2))*(MixedF00['tplus'].to_numpy()+MixedF00['tminus'].to_numpy())*(MixedF00['tplus_'].to_numpy()+MixedF00['tminus_'].to_numpy())

MixedF00

from sklearn.preprocessing import MinMaxScaler

MMS = MinMaxScaler()

NormX = pd.DataFrame(MMS.fit_transform(MixedF00.iloc[:,[0, 3, 4, 5, 6, 7, 9, 10]]), columns = MixedF00.iloc[:,[0, 3, 4, 5, 6, 7, 9, 10]].columns)


y = MixedF00['señal']

print('Adding phi_0')

for i in np.arange(0.05, 0.5, 0.0001):
    NormX['analytic ' + str(i)] = (i**2)/MixedF00['phi0 minus delta']

                        

## Iterate through possible values of phi_0 

### Random Forest

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler


RF = RandomForestRegressor()

print('Using Random Forest to select best phi_0 value')


ScoresRF = []
for i in np.arange(8, NormX.shape[1]):

    x = NormX.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, i]]
    print(i)

    x_train, x_test, y_train, y_test = train_test_split(x, y)

    RF.fit(x_train, y_train)
    ScoresRF.append((mean_absolute_error(RF.predict(x_test), y_test)))

print('Best result before adding the different "hs": ' + str(pd.DataFrame(ScoresRF).sort_values(0)))

pd.DataFrame(RF.feature_importances_, index=x_test.columns)

### Gradient Boosting

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler




x1 = NormX.iloc[:,[0, 1, 2, 3, 4, 5, 6, int(pd.DataFrame(ScoresRF).sort_values(0).iloc[[0],[0]].index.to_numpy())]]

x_train, x_test, y_train, y_test = train_test_split(x1, y, random_state=15)

RF.fit(x_train, y_train)
RFC = RF.predict(x_test)




## Rho

NormX = NormX.iloc[:,[0, 1, 2, 3, 4, 5, 6, int(pd.DataFrame(ScoresRF).sort_values(0).iloc[[0],[0]].index.to_numpy())]]

Rho = []
Rho.append(MixedF00['r']/MixedF00['Z'])

NormX['Rho'] = np.abs(np.ravel(Rho))


from sklearn.preprocessing import MinMaxScaler

MMS = MinMaxScaler()

SecondNormX = pd.DataFrame(MMS.fit_transform(NormX), columns = NormX.columns)

del NormX

y = MixedF00['señal']

## Iterating through possible values for h's

print('Creating equations using h')

for k in np.linspace(100, 200, 12):
    for l in np.linspace(-6000, -3000, 12):
        for m in np.linspace(40000, 70000, 12):
            for n in np.linspace(-400000, -150000, 12):
                for ñ in np.linspace(800000, 300000, 12):
        
        
                    SecondNormX['analytic ' + str(k)+' ' + str(l)+' ' + str(m)+' ' + str(n)+' ' + str(ñ)] = (SecondNormX.iloc[:,[7]]*(1+SecondNormX['Rho'].to_numpy()**2)*(k*SecondNormX['Rho'].to_numpy()+l*SecondNormX['Rho'].to_numpy()+m*SecondNormX['Rho'].to_numpy()+n*SecondNormX['Rho'].to_numpy()+ñ*SecondNormX['Rho'].to_numpy()))

                        
          

## Random Forests for h's

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler


SecondRF = RandomForestRegressor()

print('Using Random Forest through the possible equations')
Scores = []
for i in np.arange(9, SecondNormX.shape[1]):

    x = SecondNormX.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, i]]

    x_train, x_test, y_train, y_test = train_test_split(x, y)

    SecondRF.fit(x_train, y_train)
    Scores.append((mean_absolute_error(SecondRF.predict(x_test), y_test)))

## Save best result and error associated


print('Saving results')

LastX = SecondNormX.iloc[:,[0, 1, 2, 3, 4, 5, 6, 7, 8, int(pd.DataFrame(Scores).sort_values(0).iloc[[0],[0]].index.to_numpy())+8]]
LastX.to_csv('Result.csv')

pd.DataFrame(Scores).sort_values(0).iloc[[0],[0]].to_csv('Min_Error.csv')



NormalizedLastX = pd.DataFrame(MMS.fit_transform(LastX), columns=LastX, index=LastX)

x_train, x_test, y_train, y_test = train_test_split(NormalizedLastX, y, random_state=15)

SecondRF.fit(x_train, y_train)
RFC = SecondRF.predict(x_test)


RFC.to_csv('BestRF_Result.csv')
y_test.to_csv('y_test.csv')
y_test.to_csv('x_test.csv')

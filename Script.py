import pandas as pd
df1 = pd.read_csv('../input/african-development-bank/agri1.csv', encoding='latin-1')
df2 = pd.read_csv('../input/african-development-bank/finance1.csv', encoding='latin-1')
df3 = pd.read_csv('../input/african-development-bank/multisector1.csv', encoding='latin-1')
df4 = pd.read_csv('../input/african-development-bank/power1.csv', encoding='latin-1')
df5 = pd.read_csv('../input/african-development-bank/transport1.csv', encoding='latin-1')
#to check the data
df1.info()
df2.info()
df3.info()
df4.info()
df5.info()
a = df1.dropna()
f = df2.dropna()
m = df3.dropna()
p = df4.dropna()
t = df5.dropna()

a['Starting Date'] = pd.to_datetime(t['Starting Date'])
f['Starting Date'] = pd.to_datetime(t['Starting Date'])
m['Starting Date'] = pd.to_datetime(t['Starting Date'])
p['Starting Date'] = pd.to_datetime(t['Starting Date'])
t['Starting Date'] = pd.to_datetime(t['Starting Date'])

a['Starting_Year'] = a['Starting Date'].dt.year
f['Starting_Year'] = f['Starting Date'].dt.year
m['Starting_Year'] = m['Starting Date'].dt.year
p['Starting_Year'] = p['Starting Date'].dt.year
t['Starting_Year'] = t['Starting Date'].dt.year

ag = a[a['Starting_Year'] == 2019]
fi = f[f['Starting_Year'] == 2019]
mu = m[m['Starting_Year'] == 2019]
po = p[p['Starting_Year'] == 2019]
tr = t[t['Starting_Year'] == 2019]
agr = ag.drop(['Project Code', 'Title', 'Starting Date', 'Status', 'Source of Financing', 'Sovereign'], axis = 1)
fin = fi.drop(['Project Code', 'Title', 'Starting Date', 'Status', 'Source of Financing', 'Sovereign'], axis = 1)
mul = mu.drop(['Project Code', 'Title', 'Starting Date', 'Status', 'Source of Financing', 'Sovereign'], axis = 1)
por = po.drop(['Project Code', 'Title', 'Starting Date', 'Status', 'Source of Financing', 'Sovereign'], axis = 1)
tra = tr.drop(['Project Code', 'Title', 'Starting Date', 'Status', 'Source of Financing', 'Sovereign'], axis = 1)
data = [agr, fin, mul, por, tra]
df = pd.concat(data)
df['Commitment in U.A'] = df['Commitment in U.A'].str.replace(r',', '') #error raise because of , when we try to make this column as numeric
df['Commitment in U.A'] = df['Commitment in U.A'].apply(pd.to_numeric)
df.info()
df.to_csv('mydata.csv')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('mydata.csv')
%matplotlib inline
df.head()
df1_agri = df.query('Sector == "Agriculture and Rural Development"')
df1_fin = df.query('Sector == "Finance"')
df1_tra = df.query('Sector == "Transport"')
df1_mul = df.query('Sector == "Multi-Sector"')
df1_pow = df.query('Sector == "Power"')

df1_fin.plot(x ='Country', y = 'Commitment in U.A' ,kind ='bar', figsize = (8,8))
# first multinational, second Morocco, third Kenya
df1_agri.plot(x ='Country', y = 'Commitment in U.A' ,kind ='bar', figsize = (8,8))
# first Côte d'Ivoire, second congo, third sudan
df1_pow.plot(x ='Country', y = 'Commitment in U.A' ,kind ='bar', figsize = (8,8))
# first angola, second Mozambique, third Morocco
df1_tra.plot(x ='Country', y = 'Commitment in U.A' ,kind ='bar', figsize = (8,8))
# first tanzania, second Uganda, third Kenya
df1_mul.plot(x ='Country', y = 'Commitment in U.A' ,kind ='bar', figsize = (8,8))
# first niger, second rwanda, third Madagascar

xm = df1_mul['Commitment in U.A'].sum()
xt = df1_tra['Commitment in U.A'].sum()
xp = df1_pow['Commitment in U.A'].sum()
xa = df1_agri['Commitment in U.A'].sum()
xf = df1_fin['Commitment in U.A'].sum()
#Finance
yf1 = df1_fin.query('Country == "Multinational"')
yf2 = df1_fin.query('Country == "Morocco"')
yf3 = df1_fin.query('Country == "Kenya"')
multinational_percent = (yf1['Commitment in U.A'].sum() / xf) * 100
# 50.274878045406936
morocco1_percent = (yf2['Commitment in U.A'].sum() / xf) * 100
# 17.308766996498854
kenya1_percent = (yf3['Commitment in U.A'].sum() / xf) * 100
# 17.104531773436218
#Agriculture
ya1 = df1_agri.query('Country == "Côte d\'Ivoire"')
ya2 = df1_agri.query('Country == "Congo"')
ya3 = df1_agri.query('Country == "Sudan"')
cote_percent = (ya1['Commitment in U.A'].sum() / xa) * 100
# 31.50741594033916
congo_percent = (ya2['Commitment in U.A'].sum() / xa) * 100
# 18.711099794684774
sudan_percent = (ya3['Commitment in U.A'].sum() / xa) * 100
# 13.336644343098406
#Power
yp1 = df1_pow.query('Country == "Angola"')
yp2 = df1_pow.query('Country == "Mozambique"')
yp3 = df1_pow.query('Country == "Morocco"')
angola_percent = (yp1['Commitment in U.A'].sum() / xp) * 100
# 22.607751209625953
mozambique_percent = (yp2['Commitment in U.A'].sum() / xp) * 100
# 19.404458459382017
morocco2_percent = (yp3['Commitment in U.A'].sum() / xp) * 100
# 12.89769995885802
#Transport
yt1 = df1_tra.query('Country == "Uganda"')
yt2 = df1_tra.query('Country == "Kenya"')
yt3 = df1_tra.query('Country == "Tanzania, United Republic of"')
uganda_percent = (yt1['Commitment in U.A'].sum() / xt) * 100
# 14.39372966123651
kenya2_percent = (yt2['Commitment in U.A'].sum() / xt) * 100
# 10.677509240332622
tanzania_percent = (yt3['Commitment in U.A'].sum() / xt) * 100
# 17.001848235170208
#multi-Sector
ym1 = df1_mul.query('Country == "Niger"')
ym2 = df1_mul.query('Country == "Rwanda"')
ym3 = df1_mul.query('Country == "Madagascar"')
niger_percent = (ym1['Commitment in U.A'].sum() / xm) * 100
# 12.729731880022277
rwanda_percent = (ym2['Commitment in U.A'].sum() / xm) * 100
# 11.29763704351977
madagascar_percent = (ym3['Commitment in U.A'].sum() / xm) * 100
# 9.547298910016707

rest_finance = 100 - (multinational_percent + morocco1_percent + kenya1_percent)
rest_agriculture = 100 - (cote_percent + congo_percent + sudan_percent)
rest_power = 100 - (angola_percent + mozambique_percent + morocco2_percent)
rest_transport = 100 - (uganda_percent + kenya2_percent + tanzania_percent)
rest_multi = 100 - (niger_percent + rwanda_percent + madagascar_percent)

dfchart1 = pd.DataFrame({'finance sector':[multinational_percent, morocco1_percent, kenya1_percent, rest_finance]}, index = ['Multinational', 'Morocco', 'Kenya', 'Rest of Africa'])
dfchart2 = pd.DataFrame({'agriculture sector': [cote_percent, congo_percent, sudan_percent, rest_agriculture]}, index = ['Cote d\'Ivoire', 'Congo', 'Sudan', 'Rest of Africa'])
dfchart3 = pd.DataFrame({'power sector': [angola_percent, mozambique_percent, morocco2_percent, rest_power]}, index = ['Angola', 'Mozambique', 'Morocco', 'Rest of Africa'])
dfchart4 = pd.DataFrame({'transport sector': [uganda_percent, kenya2_percent, tanzania_percent, rest_transport]}, index = ['Uganda', ' Kneya', 'Tanzania', 'Rest of Africa'])
dfchart5 = pd.DataFrame({'multi sector': [niger_percent, rwanda_percent, madagascar_percent, rest_multi]}, index = ['Niger', 'Rwanda', 'Madagascar', 'Rest of Africa'])

dfchart1.plot.pie(y = 'finance sector', figsize = (8,8))

dfchart2.plot.pie(y = 'agriculture sector', figsize = (8,8))

dfchart3.plot.pie(y = 'power sector', figsize = (8,8))

dfchart4.plot.pie(y = 'transport sector', figsize = (8,8))

dfchart5.plot.pie(y = 'multi sector', figsize = (8,8))

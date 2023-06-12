import pandas as pd
#table_MN = pd.read_html('https://hydro.chmi.cz/hpps/pov/objekt/307081')
table_MN = pd.read_html('307081')
df = table_MN[1]
row0 = df.iloc[1]
time0= row0.iloc[1]
value0= row0.iloc[2]
print("Stav vody Mělník", time0, "je", value0, "cm" )

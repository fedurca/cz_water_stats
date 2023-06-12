import pandas as pd
table_MN = pd.read_html('https://hydro.chmi.cz/hpps/pov/objekt/307081')
print("Stav vody Mělník", table_MN[1].iloc[1,1], "je", table_MN[1].iloc[1,2], "cm" )

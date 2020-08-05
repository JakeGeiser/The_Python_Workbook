columns = df.columns()
for col in columns:
    if 'name' in col == True or 'Name' in col == True:
        df['Name'] = df.loc[:,col]






try:
    df['Name'] = df.loc[:,'name1']
except:
    print("")
try:
    df['Name'] = df.loc[:'Name1']
except:
    print("")
try:
    df['Name'] = df.loc[:'name 1']
except:
    print("")

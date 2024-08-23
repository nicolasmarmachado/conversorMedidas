import pandas as pd

def cmAPulgadas(cm):
    return cm/2.54

df=pd.read_excel('conversorDeMedidas.xlsx')

df['Pulgadas'] = df['centimetros'].apply(cmAPulgadas)

df.to_excel('MueblesMedidasConvertidas.xlsx', index=False)

print('Conversión completada')


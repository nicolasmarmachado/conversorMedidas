import pandas as pd

data= {
'piezas': ['pata','tablero','puerta','estante','panel Lateral'],
'centimetros': [40,120,60,30,180]
}

df=pd.DataFrame(data)

df.to_excel('./conversorMedidas/conversorDeMedidas.xlsx', index=False)


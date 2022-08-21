#import types
#from django.db import models

import pandas as pd

p="C:\\Users\\support\\Documents\\all\\in\\"
pout="C:\\Users\\support\\Documents\\all\\out\\"

df=pd.read_excel(p+"2022-01-07_CSI.xlsx")
df2=pd.read_excel(p+"reply_codes_ru_202207151130.xlsx")
df['ABC_DEF']=df.loc[df['Номер Б']>0,'Номер Б'].astype(str).str[1:4].astype('int64')


'''
a=[1,2,4]
b2=['2','2',5]

#print(len(a),len(b2))
d=pd.DataFrame(
	{'a':[1,2,4,4],
	 'b':['1','2',6,4]}
)
d2=pd.DataFrame(
	{'a':[1,2,4,2,1,1,2],
	 'b2':['2','2',5,'2',2,3,2],
	 'b3':['2','2',5,'2',3,4,4],
	 'b4':['2','2',5,'2',3,4,5]}
)'''
#d2.loc[d2['a'].index==1,'a']=str(d2['a'][1])
#print(len(d2['a']),len(d2['b2']))
#d4=d2.join(d,lsuffix='_left',rsuffix='_right')
try:
    d4= df.merge(df2,suffixes=('_x','_y'),how='left')

#print(d3)
#print('da:',d,'\n','d2a:',d2)
#print(d4)
    d4.to_excel(pout+"out3.xlsx")
except Exception as e:
    print(e)
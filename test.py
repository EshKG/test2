#import types
from django.db import models

import pandas as pd
a=[1,2,4]
b2=['2','2',5]
print(len(a),len(b2))
d=pd.DataFrame(
	{'a':[1,2,4],
	 'b':['1','2',6]}
)
d2=pd.DataFrame(
	{'a':[1,2,4,2,4],
	 'b2':['2','2',5,'2',4],
	 'b3':['2','2',5,'2',4,],
	 'b4':['2','2',5,'2',4,]}
)
#d2.loc[d2['a'].index==1,'a']=str(d2['a'][1])
#print(len(d2['a']),len(d2['b2']))
#d4=d2.join(d,lsuffix='_left',rsuffix='_right')
d4= d.join(d2,lsuffix='_x',rsuffix='_y') #left_on='a',right_on='a')
d['a']=d.loc[d.a>=0,'a'].astype(str)[0:].astype('int64')


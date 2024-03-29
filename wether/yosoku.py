from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import interval

df=pd.read_csv('kion10y.csv', encoding="utf-8")

train_year=(df["年"]<=2017)
test_year=(df["年"]>=2018)
interval=6

def make_data(data):
    x=[]
    y=[]
    temps=list(data["気温"])
    for i in range(len(temps)):
        if i<interval:continue
        y.append(temps[i])
        xa=[]
        for p in range(interval):
            d=i+p-interval
            xa.append(temps[d])
        x.append(xa)
    return(x,y)

train_x,train_y=make_data(df[train_year])
test_x,test_y=make_data(df[test_year])

lr=LinearRegression(normalize=True)
lr.fit(train_x,train_y)
pre_y=lr.predict(test_x)

plt.figure(figsize=(10,6),dpi=100)
plt.plot(test_y,c='r')
plt.plot(pre_y,c='b')
plt.savefig('tenki-kion-lr.png')
plt.show()

print(pre_y-test_y)

diff_y=abs(pre_y-test_y)
print("average=",sum(diff_y)/len(diff_y))
print("max=",max(diff_y))
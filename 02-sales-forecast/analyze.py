from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

base=Path(__file__).resolve().parent; out=base/'output'; out.mkdir(exist_ok=True)
df=pd.read_csv(base/'data/monthly_sales.csv',parse_dates=['month'])
df['index']=np.arange(len(df))
# Simple trend + seasonal month indicators; last 6 months held out for evaluation.
features=pd.get_dummies(df.month.dt.month,prefix='month').reindex(columns=[f'month_{j}' for j in range(1,13)],fill_value=0)
features['index']=df['index']
train=30
model=LinearRegression().fit(features.iloc[:train],df.revenue_usd.iloc[:train])
mae=mean_absolute_error(df.revenue_usd.iloc[train:],model.predict(features.iloc[train:]))
model.fit(features,df.revenue_usd)
future_dates=pd.date_range(df.month.max()+pd.offsets.MonthBegin(1),periods=3,freq='MS')
future=pd.DataFrame(0,index=range(3),columns=features.columns)
future['index']=np.arange(len(df),len(df)+3)
for j,m in enumerate(future_dates.month): future.loc[j,f'month_{m}']=1
pred=np.maximum(model.predict(future),0)
pd.DataFrame({'month':future_dates.strftime('%Y-%m-%d'),'forecast_usd':pred.round(2)}).to_csv(out/'forecast.csv',index=False)
plt.plot(df.month,df.revenue_usd,label='Historical'); plt.plot(future_dates,pred,marker='o',label='Forecast'); plt.title('Sales forecast (3 months)'); plt.ylabel('Revenue (USD)'); plt.legend(); plt.xticks(rotation=30); plt.tight_layout(); plt.savefig(out/'sales_forecast.png',dpi=150); plt.close()
summary=f'Holdout MAE (last 6 months): ${mae:,.2f}\n3-month forecasts (USD):\n'+ '\n'.join(f'{d:%Y-%m}: ${v:,.2f}' for d,v in zip(future_dates,pred))+'\n'
(out/'summary.txt').write_text(summary);print(summary)

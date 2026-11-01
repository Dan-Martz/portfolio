from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
base=Path(__file__).resolve().parent;out=base/'output';out.mkdir(exist_ok=True)
df=pd.read_csv(base/'data/daily_sales.csv',parse_dates=['date'])
df['month']=df.date.dt.month;df['weekday']=df.date.dt.day_name()
months=df.groupby('month').sales_usd.mean()
weekdays=df.groupby('weekday').sales_usd.mean().reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
fig,ax=plt.subplots(); months.plot(kind='bar',ax=ax,color='#4073ad');ax.set_title('Average daily sales by month');ax.set_ylabel('Average daily sales (USD)');fig.tight_layout();fig.savefig(out/'monthly_seasonality.png',dpi=150);plt.close(fig)
summary=f'Highest average month: {months.idxmax()} (${months.max():,.0f}/day)\nHighest average weekday: {weekdays.idxmax()} (${weekdays.max():,.0f}/day)\n'
(out/'summary.txt').write_text(summary); print(summary)

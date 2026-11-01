from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
base=Path(__file__).resolve().parent;out=base/'output';out.mkdir(exist_ok=True)
df=pd.read_csv(base/'data/transactions.csv')
# Rules flag anomalies, not proven fraud. Thresholds are illustrative.
df['high_amount']=df.amount_usd>=800
df['night_transaction']=df.hour.between(0,4)
df['review_flag']=df.high_amount | (df.night_transaction & (df.amount_usd>150))
review=df[df.review_flag].copy();review.to_csv(out/'transactions_for_review.csv',index=False)
fig,ax=plt.subplots();df.groupby('hour').size().plot(kind='bar',ax=ax,color='#4073ad');ax.set_title('Transactions by hour');ax.set_xlabel('Hour of day');fig.tight_layout();fig.savefig(out/'transactions_by_hour.png',dpi=150);plt.close(fig)
summary=f'Total transactions: {len(df)}\nFlagged for manual review: {len(review)} ({len(review)/len(df):.1%})\nImportant: flags are NOT verified fraud. No ground-truth fraud labels are included.\n'
(out/'summary.txt').write_text(summary);print(summary)

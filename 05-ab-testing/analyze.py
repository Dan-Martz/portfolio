from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
base=Path(__file__).resolve().parent;out=base/'output';out.mkdir(exist_ok=True)
df=pd.read_csv(base/'data/experiment.csv')
g=df.groupby('variant').converted.agg(['sum','count','mean']);p1,p2=g.loc['A','mean'],g.loc['B','mean'];n1,n2=g.loc['A','count'],g.loc['B','count']
pool=(g['sum'].sum())/(n1+n2)
se=np.sqrt(pool*(1-pool)*(1/n1+1/n2))
z=(p2-p1)/se if se else 0
p_value=2*norm.sf(abs(z)) if se else 1
ax=(g['mean']*100).plot(kind='bar',color=['#4073ad','#69a88f'],title='Conversion by landing page');ax.set_ylabel('Conversion rate (%)');plt.tight_layout();plt.savefig(out/'conversion_rates.png',dpi=150);plt.close()
summary=f'Variant A: {p1:.2%} ({int(g.loc["A","sum"])}/{n1})\nVariant B: {p2:.2%} ({int(g.loc["B","sum"])}/{n2})\nDifference B minus A: {(p2-p1)*100:.2f} percentage points\nTwo-sided z-test p-value: {p_value:.4f}\nSignificant at 0.05: {p_value<0.05}\nNote: synthetic data; significance does not imply business impact.\n'
(out/'summary.txt').write_text(summary);print(summary)

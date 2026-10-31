from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

base=Path(__file__).resolve().parent
out=base/'output'; out.mkdir(exist_ok=True)
df=pd.read_csv(base/'data/customers.csv')
df['tenure_group']=pd.cut(df.tenure_months,[0,12,24,36,60],labels=['1-12','13-24','25-36','37-60'])
rates=df.groupby('tenure_group',observed=True).churned.mean()
X=df[['tenure_months','monthly_fee_usd','support_tickets','annual_contract']]
y=df.churned
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
model=LogisticRegression(max_iter=1000).fit(X_train,y_train)
auc=roc_auc_score(y_test,model.predict_proba(X_test)[:,1])
ax=(rates*100).plot(kind='bar',title='Churn rate by customer tenure',color='#4073ad')
ax.set_ylabel('Churn rate (%)'); ax.set_xlabel('Tenure (months)')
plt.tight_layout(); plt.savefig(out/'churn_by_tenure.png',dpi=150); plt.close()
summary=f'Overall churn rate: {y.mean():.1%}\nTest ROC AUC: {auc:.3f}\nChurn by tenure:\n{(rates*100).round(1).to_string()}\n'
(out/'summary.txt').write_text(summary)
print(summary)

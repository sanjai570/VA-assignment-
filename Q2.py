!pip install plotly

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

df = sns.load_dataset("titanic")
df.head()

df.dropna(subset=['age', 'fare', 'embarked'], inplace=True)  # Example cleaning
df.reset_index(drop=True, inplace=True)

sns.countplot(x='sex', hue='survived', data=df)
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

corr = df[['age', 'fare', 'pclass']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

fig = px.scatter(df, x='age', y='fare', color='pclass',
                 size='fare', hover_data=['sex', 'survived'],
                 title='Fare vs Age by Class (Interactive)')
fig.show()

print("🔍 Inference:")
print("- Females had a significantly higher survival rate than males.")
print("- Fare is negatively correlated with passenger class, suggesting higher prices for better classes.")
print("- The scatter plot highlights how younger passengers vary in fare across classes.")

     
Requirement already satisfied: plotly in /usr/local/lib/python3.11/dist-packages (5.24.1)
Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly) (9.1.2)
Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from plotly) (24.2)


🔍 Inference:
- Females had a significantly higher survival rate than males.
- Fare is negatively correlated with passenger class, suggesting higher prices for better classes.
- The scatter plot highlights how younger passengers vary in fare across classes.

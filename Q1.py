!pip install plotly

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

try:
    df = pd.read_csv("data.csv", encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv("data.csv", encoding='ISO-8859-1')

print("✅ Columns in Dataset:")
print(df.columns)

print("\n🔎 Dataset Info:")
print(df.info())

print("\n🧹 Missing Values:")
print(df.isnull().sum())

print("\n📊 Summary Stats:")
print(df.describe(include='all'))

if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

if 'Region' in df.columns and 'Sales' in df.columns:
    region_sales = df.groupby("Region")["Sales"].sum().reset_index()
    fig1 = px.bar(region_sales, x="Region", y="Sales", color="Sales",
                  title="Total Sales by Region", color_continuous_scale="Blues")
    fig1.show()

if 'Order Date' in df.columns and 'Sales' in df.columns:
    monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
    fig2 = px.line(monthly_sales, x="Month", y="Sales",
                   title="Monthly Sales Trend")
    fig2.show()

if 'Category' in df.columns and 'Profit' in df.columns:
    profit_by_category = df.groupby("Category")["Profit"].sum().reset_index()
    fig3 = px.pie(profit_by_category, names='Category', values='Profit',
                  title='Profit Distribution by Category')
    fig3.show()

if all(col in df.columns for col in ['Sales', 'Profit', 'Region']):
    fig4 = px.scatter(df, x='Sales', y='Profit', color='Region',
                      hover_data=['Category'] if 'Category' in df.columns else None,
                      title="Sales vs Profit by Region")
    fig4.show()

print("\n📈 Inference Summary:")
if 'Region' in df.columns:
    print("- Identify underperforming regions for resource reallocation.")
if 'Order Date' in df.columns:
    print("- Monthly sales trend helps in planning promotions or restocking.")
if 'Category' in df.columns and 'Profit' in df.columns:
    print("- Profitable categories help prioritize inventory and marketing.")

     
Requirement already satisfied: plotly in /usr/local/lib/python3.11/dist-packages (5.24.1)
Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly) (9.1.2)
Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from plotly) (24.2)
✅ Columns in Dataset:
Index(['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
       'UnitPrice', 'CustomerID', 'Country'],
      dtype='object')

🔎 Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype  
---  ------       --------------   -----  
 0   InvoiceNo    541909 non-null  object 
 1   StockCode    541909 non-null  object 
 2   Description  540455 non-null  object 
 3   Quantity     541909 non-null  int64  
 4   InvoiceDate  541909 non-null  object 
 5   UnitPrice    541909 non-null  float64
 6   CustomerID   406829 non-null  float64
 7   Country      541909 non-null  object 
dtypes: float64(2), int64(1), object(5)
memory usage: 33.1+ MB
None

🧹 Missing Values:
InvoiceNo           0
StockCode           0
Description      1454
Quantity            0
InvoiceDate         0
UnitPrice           0
CustomerID     135080
Country             0
dtype: int64

📊 Summary Stats:
       InvoiceNo StockCode                         Description       Quantity  \
count     541909    541909                              540455  541909.000000   
unique     25900      4070                                4223            NaN   
top       573585    85123A  WHITE HANGING HEART T-LIGHT HOLDER            NaN   
freq        1114      2313                                2369            NaN   
mean         NaN       NaN                                 NaN       9.552250   
std          NaN       NaN                                 NaN     218.081158   
min          NaN       NaN                                 NaN  -80995.000000   
25%          NaN       NaN                                 NaN       1.000000   
50%          NaN       NaN                                 NaN       3.000000   
75%          NaN       NaN                                 NaN      10.000000   
max          NaN       NaN                                 NaN   80995.000000   

             InvoiceDate      UnitPrice     CustomerID         Country  
count             541909  541909.000000  406829.000000          541909  
unique             23260            NaN            NaN              38  
top     10/31/2011 14:41            NaN            NaN  United Kingdom  
freq                1114            NaN            NaN          495478  
mean                 NaN       4.611114   15287.690570             NaN  
std                  NaN      96.759853    1713.600303             NaN  
min                  NaN  -11062.060000   12346.000000             NaN  
25%                  NaN       1.250000   13953.000000             NaN  
50%                  NaN       2.080000   15152.000000             NaN  
75%                  NaN       4.130000   16791.000000             NaN  
max                  NaN   38970.000000   18287.000000             NaN  

📈 Inference Summary:

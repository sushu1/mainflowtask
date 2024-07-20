 
import pandas as pd

path="/content/drive/MyDrive/ Dataset/students.csv"
df=pd.read_csv(path)
print(df)

df.fillna(0,inplace=True)
df

data=df[df['ChipRate']<50]
print(data.head())



filtered_df = df[df['BlowFlow'] < 50]
print(filtered_df.head())

selected_columns=df[['Y-Kappa', 'ChipRate', 'BF-CMratio']]
summary_statistics=selected_columns.describe()
print(summary_statistics)

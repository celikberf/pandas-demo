import pandas as pd
df = pd.read_csv('pandas_demo1.csv')

#1- İlk 10 kaydı getiriniz.

result = df.head(10)

#2- Toplam kaç kayıt vardır?

result = len(df.index)

#3- Tüm  oyuncuların yaş ortalaması nedir ? 

result = df['age'].mean()

#4 - En büyük yaş nedir ? 

result = df['age'].max()

#5- En büyük yaştaki oyuncu?

result = df[df['age'] == df['age'].max()]['player_name'].iloc[0]

#6- Yaşı 20-25 arası olan oyuncuların isim ve oynadıkları takımları azalan şeklinde gösteriniz.

result = df[(df['age'] >= 20) & (df['age'] < 25)][["player_name","college"]]

#7- "Steve Kerr" isimli oyuncunun oynadığı takım hangisidir ? 

result = df[df["player_name"] == "Steve Kerr"][["college"]].iloc[0]

#8- Takımlara göre oyuncuların ortalama yaş bilgileri nedir ? 

result = df.groupby("age").mean()["college"]

#9 - Kaç farklı takım mevcut ? 

result = len(df.groupby("college"))
result = df["college"].nunique()

#10- Her takımda kaç oyuncu oynamaktadır ? 

result = df["college"].value_counts()

#11- ismi içinde 'an' geçen kayıtları bulunuz.

df.dropna(inplace=True)
result = df[df["player_name"].str.contains("an")]






print(result)
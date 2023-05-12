
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_can = pd.read_excel(
    "Canada.xlsx",
    sheet_name="Canada by Citizenship",
    skiprows=range(20),  # lambda x: x in [0, 20].
    skipfooter=2
)

print(df_can.head())
print(df_can.shape)

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage', 'DevName'], axis=1, inplace=True)

df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

# Sütunların başlıklarının tipi string mi diye baktık.
for column in df_can.columns:
    print(type(column))
    print(isinstance(column, str))  # isinstance() fonsiyonu içerisine verilen değer ve tip ile ilgili değer o tipte mi diye bakar buarada sütun başlığı string mi dye baktı ve bize true false döndü.

# Burada bütün sütunların başlıklarını string tipine dönüştürüyoruz.
df_can.columns = list(map(str, df_can.columns))
# map() fonksiyonu bize yinelenebilir bir öğedeki her öğe için bir işlemi yürütür onu execute eder. Burada yinelenen ifade "df_can.columns". uygulanan işlem iste bu sütun baçlıklarının string dönüştürülmesidir. yani her bir sütun başlığı için string dönüştürme işlemi yütürülmüştür.
# df'in sütun başlıkları list tipinde olduğundan listeye dönüştürek "df_can.columns" elde ettiğimiz değeri assigned ettik.


df_can.set_index('Country', inplace=True)  # set_index() fonsiyonu ile Country sütununda bulunan bilgilere çok daha hızlı ve etkili bir şekilde erişebilecceğiz. Index'lemeye verilebilecek en güzel örnek şu olabilir. 1000 sayfalık bir kitapta şayet içindekiler bölümü yoksa aradığımız konuya erişmek için sayfa sayfa dolaşmak gerekecektir. Ama içindekiler bölümü varsa aradığımız konuyu nokta atışı bulabiliriz. Index'lemede kitaptaki içindekiler kısmı görevini veri setimizde görecektir.

# Veri çerçevesinde yıl yıl göçmen sayıları bulunmaktadır. Bu yıllara göre göçmen sayısını toplayarak Total isimli yeni bir sütuna yazalım
df_can["Total"] = df_can.sum(axis=1)
print(df_can["Total"])

# 1980-2013 yıllarını içeren bir liste oluşturalım
years = list(map(str, range(1980, 2014)))

# Bütün veri setimizi kendimiz oluşturduğumuz Total sütunana göre çoktan aza sıralayalım
df_can.sort_values(["Total"], ascending=False, axis=0, inplace=True)
print(df_can.head())  # artık en çok göçmen vermiş ilk 5 ülkeyi göreceğiz


df_top5 = df_can.head()  # en çok göçmen vermiş ilk 5 ülkeyi fakrlı bir df'e yazdık

# Transpose() => Bir df'in sutunlar başlıklarını satır başlığına satır başlıklarınıda sütun başlığına dönüştürür.
df_top5 = df_top5[years].transpose()

print(df_top5)

# Alan Grafiği
# df_top5.plot(
#     kind="area",
#     stacked=False,
#     alpha=0.25,
#     figsize=(20, 10)
# )
#
# plt.title('Immigrant Trend of Top 5 Country', color="red")
# plt.ylabel("Number of Immigrants", color="red")
# plt.xlabel("Years")
# plt.show()

Histogram
count, bin_edges = np.histogram(df_can["2013"])
print(count)
print(bin_edges)

df_can["2013"].plot(
    kind="hist",
    figsize=(10, 7),
    xticks=bin_edges,
    color='b'
)

plt.title("Histogram of Immigration from 195 Countries in 2013")
plt.ylabel("Number of Countries")
plt.xlabel("Number of Immigrant")
plt.grid(True)
plt.show()


# df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
# print(df_t.head())
#
# count, bin_edges = np.histogram(df_t, 15)
#
# print(count)
# print(bin_edges)
#
# df_t.plot(
#     kind='hist',
#     figsize=(10, 7),
#     xticks=bin_edges,
#     color=['coral', 'darkslateblue', 'mediumseagreen']
# )
#
# plt.title('Immigrat from Denmark, Norway and Sweden from 1980 - 2013')
# plt.ylabel('Number of Years')
# plt.xlabel('Number of Immigrants')
# plt.grid(True)
# plt.show()

#  Çubuk Grafikler
# df_icleand = df_can.loc['Iceland', years]
#
# df_icleand.plot(
#     kind='bar',
#     figsize=(10, 7)
# )
#
# plt.title('Icelandic Immigrats of Canada from 1980 to 2013')
# plt.ylabel('Number of Immigrats')
# plt.xlabel('Year')
# plt.show()


# Pasta Grafiği
# df_continets = df_can.groupby('Continent', axis=0).sum()
# print(df_continets.head())
#
# df_continets["Total"].plot(
#     kind="pie",
#     figsize=(10, 7),
#     autopct='%1.1f%%',
#     startangle=90,
#     shadow=True,
#     labels=None,
#     explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
#     pctdistance=1.1
# )
#
# plt.title('Immigrant to Canada by Continen', y=1.1)
# plt.axis('equal')
# plt.legend(labels=df_continets.index, loc="upper left")
# plt.show()

# Dağılım Grafiği
# df_total = pd.DataFrame(df_can[years].sum(axis=0))
# # print(df_total.head())
#
# df_total.reset_index(inplace=True)
#
# df_total.columns = ["year", 'total']
#
# # print(df_total.head())
#
# df_total.plot(kind='scatter', x='year', y='total', figsize=(10, 7), color="darkblue")
#
# plt.title('Total Immigrants to Canada from 1980 - 2013')
# plt.xlabel('Year')
# plt.ylabel('Number of Immigrant')
# plt.show()



# AB Testi ile BiddingYöntemlerinin Dönüşümünün Karşılaştırılması
# Veri Seti Hikayesi

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri ab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç


import pandas as pd
# !pip install statsmodels
from scipy.stats import shapiro, levene, ttest_ind, mannwhitneyu, f_oneway, kruskal

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

dataframe_control = pd.read_excel("C:/Users/ipeks/PycharmProjects/pythonProject/WEEK4/datasets/ab_testing.xlsx",
                                  sheet_name="Control Group")
dataframe_test = pd.read_excel("C:/Users/ipeks/PycharmProjects/pythonProject/WEEK4/datasets/ab_testing.xlsx",
                               sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()


# Kontrol ve test grubu verilerini analizi
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head())
    print("##################### Tail #####################")
    print(dataframe.tail())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df_control)
check_df(df_test)

# Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştirme.
df_control["group"] = "control"
df_test["group"] = "test"

df = pd.concat([df_control, df_test], axis=0, ignore_index=False)
df.head()

#####################################################
# A/B Testinin Hipotezinin Tanımlanması
#####################################################
# Adım 1: Hipotezi tanımlama.

# H0 : M1 = M2 (Kontrol grubu ve test grubu satın alma ortalamalarıarasında fark yoktur.)
# H1 : M1!= M2 (Kontrol grubu ve test grubu satın alma ortalamalarıarasında fark vardır.)

# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analizi
df.groupby("group").agg({"Purchase": "mean"})

#####################################################
# Hipotez Testinin Gerçekleştirilmesi
#####################################################
# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapılır.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.

# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test edilir
# Normallik Varsayımı :
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır
# p < 0.05 H0 RED
# p > 0.05 H0 REDDEDİLEMEZ
# Test sonucuna göre normallik varsayımı kontrol ve test grupları için sağlanıyor mu ?
# Elde edilen p-valuedeğerlerini yorumlanır.

test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value=0.5891
# HO reddedilemez. Control grubunun değerleri normal dağılım varsayımını sağlamaktadır.


# Varyans Homojenliği :
# H0: Varyanslarhomojendir.
# H1: Varyanslarhomojen Değildir.
# p < 0.05 H0 RED
# p > 0.05 H0 REDDEDİLEMEZ
# Kontrol ve test grubu için varyans homojenliğinin sağlanıp sağlanmadığını Purchase değişkeni üzerinden test edilir.
# Test sonucuna göre normallik varsayımı sağlanıyor mu? Elde edilen p-valuedeğerlerini yorumlanır

test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
                           df.loc[df["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value=0.1083
# HO reddedilemez. Control ve Test grubunun değerleri varyans homejenliği varsayımını sağlamaktadır.
# Varyanslar Homojendir.

# Adım 2: Normallik Varsayımı ve VaryansHomojenliği sonuçlarına göre uygun testi seçilir

# Varsayımlar sağlandığı için bağımsız iki örneklem t testi (parametrik test) yapılmaktadır.
# H0: M1 = M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında ist. ol.anl.fark yoktur.)
# H1: M1 != M2 (Kontrol grubu ve test grubu satın alma ortalamaları arasında ist. ol.anl.fark vardır)
# p<0.05 HO RED , p>0.05 HO REDDEDİLEMEZ

test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value=0.3493
# HO reddedilemez. Kontrol ve test grubu satın alma ortalamaları arasında istatistiksel olarak anlamlı farklılık yoktur.


############################
# UYGULAMA 2: Titanic Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında İstatistiksel Olarak Anl. Fark. var mıdır?
############################
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.groupby("sex").agg({"age": "mean"})

# 1. Hipotezleri kur:
# H0: M1  = M2 (Kadın ve Erkek Yolcuların Yaş Ortalamaları Arasında İstatistiksel Olarak Anl. Fark. Yoktur)
# H1: M1! = M2 (... vardır)


# 2. Varsayımları İncele

# Normallik varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır


test_stat, pvalue = shapiro(df.loc[df["sex"] == "female", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df.loc[df["sex"] == "male", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Varyans homojenliği
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(df.loc[df["sex"] == "female", "age"].dropna(),
                           df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Varsayımlar sağlanmadığı için nonparametrik

test_stat, pvalue = mannwhitneyu(df.loc[df["sex"] == "female", "age"].dropna(),
                                 df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# 90 280

######################################################
# ANOVA (Analysis of Variance)
######################################################

# İkiden fazla grup ortalamasını karşılaştırmak için kullanılır.

df = sns.load_dataset("tips")
df.head()

df.groupby("day")["total_bill"].mean()

# 1. Hipotezleri kur

# HO: m1 = m2 = m3 = m4
# Grup ortalamaları arasında fark yoktur.

# H1: .. fark vardır

# 2. Varsayım kontrolü

# Normallik varsayımı
# Varyans homojenliği varsayımı

# Varsayım sağlanıyorsa one way anova
# Varsayım sağlanmıyorsa kruskal

# H0: Normal dağılım varsayımı sağlanmaktadır.

for group in list(df["day"].unique()):
    pvalue = shapiro(df.loc[df["day"] == group, "total_bill"])[1]
    print(group, 'p-value: %.4f' % pvalue)

# H0: Varyans homojenliği varsayımı sağlanmaktadır.

test_stat, pvalue = levene(df.loc[df["day"] == "Sun", "total_bill"],
                           df.loc[df["day"] == "Sat", "total_bill"],
                           df.loc[df["day"] == "Thur", "total_bill"],
                           df.loc[df["day"] == "Fri", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# 3. Hipotez testi ve p-value yorumu

# Hiç biri sağlamıyor.
df.groupby("day").agg({"total_bill": ["mean", "median"]})

# HO: Grup ortalamaları arasında ist ol anl fark yoktur

# parametrik anova testi:
f_oneway(df.loc[df["day"] == "Thur", "total_bill"],
         df.loc[df["day"] == "Fri", "total_bill"],
         df.loc[df["day"] == "Sat", "total_bill"],
         df.loc[df["day"] == "Sun", "total_bill"])

# Nonparametrik anova testi:
kruskal(df.loc[df["day"] == "Thur", "total_bill"],
        df.loc[df["day"] == "Fri", "total_bill"],
        df.loc[df["day"] == "Sat", "total_bill"],
        df.loc[df["day"] == "Sun", "total_bill"])

from statsmodels.stats.multicomp import MultiComparison

comparison = MultiComparison(df['total_bill'], df['day'])
tukey = comparison.tukeyhsd(0.05)
print(tukey.summary())

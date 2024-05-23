# A-B_Testing
- İki farklı versiyonun performansını karşılaştırmak amacıyla kullanılır.Adımları şu şekilde:
  
   - Hipotez belirleme
   - Kontol ve Varyant grupları
   - Rastgele Atama
   - Veri toplama
   - Analiz
   - Karar verme
                       
- Sampling ana kitlenin temsilcisidir.
- Confidence Intervals, ana kitle parametresinin tahmini değerini kapsayabilecek aralıktır.
- İçinde aykırı değerler bulunan veride medyan kullanmak daha mantıklıdır(descriptive analysis)
- Hipotez testleri: Grup karşılaştırmalarında temel amaç farklılıkların şans eseri ortaya çıkıp çıkmadığını göstermeye çalışmaktır.

- Bağımsız iki örneklem T testi: iki grup ortalaması arasında karşılaştırma yapılmak istedndiğinde kullanılır.   

Hipotez kurmada takip edilmesi gereken adımlar:  
    1- Hipotezlerin Belirlenmesi
       (μ1 = μ2)
       (μ1 ≠ μ2) 
       
  2- Varsayımların Kontrol Edilmesi
     
        2.1-Normallik Testi
            Shapiro-Wilk Testi: Her iki grup için normallik testi yapılır.
            Sonuçlar:
            Eğer p-değeri < 0.05 ise, normallik varsayımı reddedilir (veri normal dağılmamıştır).
            Eğer p-değeri ≥ 0.05 ise, normallik varsayımı sağlanır (veri normal dağılmıştır).
            Normallik sağlanmıyorsa: Normallik varsayımı sağlanmadığında non-parametrik testler tercih edilmelidir.

        2.2- Varyans Homojenlik Testi
             Levene Testi: İki grubun varyanslarının homojen olup olmadığını test etmek için kullanılır.
             Sonuçlar:
             Eğer p-değeri < 0.05 ise, varyans homojenlik varsayımı reddedilir (varyanslar eşit değildir).
             Eğer p-değeri ≥ 0.05 ise, varyans homojenlik varsayımı sağlanır (varyanslar eşittir).


  3) Varsayımlar Sağlanıyorsa
        Eğer hem normallik varsayımı hem de varyans homojenliği sağlanıyorsa, Bağımsız İki Örneklem t-Testi (parametrik test) uygulanır.

  4) Varsayımlar Sağlanmıyorsa
        Eğer normallik varsayımı sağlanmıyorsa veya varyans homojenliği sağlanmıyorsa, Mann-Whitney U Testi (non-parametrik test) uygulanır.


- 2 Örneklem oran testi:
  İki örneklem oran testi, iki bağımsız grup arasında kategorik değişkenlerin oranlarını karşılaştırmak için kullanılan bir istatistiksel testtir. 
  Bu test, oranların farklı olup olmadığını belirlemek için hipotezlerin belirlenmesi, veri toplama, oranların hesaplanması, Z-testi uygulanması ve 
  sonuçların yorumlanması adımlarını içerir.

- ANOVA(Analysis of Variance):
  İkiden fazla grup ortalamasını karşılaştırmak için kullanılır. Bu test, grupların ortalamaları arasındaki varyans farklarını karşılaştırarak gruplar arasında anlamlı bir fark olup olmadığını belirler.
  Grupların varyanslarının farklılık gösterip göstermediğini belirlemek için F testi yapılır. Hesaplanan F değeri, F dağılımından elde edilen kritik değerle 
  karşılaştırılır.
    - f_oneway fonksiyonu, F istatistiği ve p-değeri döndürür. P-değeri, null hipotezin (grup ortalamaları arasında fark yoktur) geçerliliğini değerlendirmek
      için kullanılır. Eğer p-değeri belirlenen anlamlılık düzeyinden (genellikle 0.05) küçükse, null hipotez reddedilir ve gruplar arasında anlamlı bir fark
      olduğu sonucuna varılır.
      
    - kruskal fonksiyonu, H istatistiği ve p-değeri döndürür. P-değeri, null hipotezin (gruplar arasında fark yoktur) geçerliliğini değerlendirmek için 
      kullanılır. Eğer p-değeri belirlenen anlamlılık düzeyinden (genellikle 0.05) küçükse, null hipotez reddedilir ve gruplar arasında anlamlı bir fark
      olduğu sonucuna varılır.
      
    - Multicomparison özelliği, genellikle statsmodels kütüphanesindeki AnovaRM sınıfı veya anova_lm fonksiyonu ile birlikte kullanılır. 
      Bu özellik, ANOVA analizi sonrasında gruplar arasındaki farkların çoklu karşılaştırmasını gerçekleştirmek için kullanılır.











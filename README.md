# YouTube Video ve Kanal Verisi Analizi

## Proje Hakkında
Bu proje, YouTube kanallarına ve videolarına ait verilerin analiz edilmesi, görselleştirilmesi ve modelleme yapılmasını içermektedir. Veri analizi ve makine öğrenimi yöntemleri kullanılarak videoların görüntülenme sayısını tahmin etme amaçlanmıştır. 

Bu çalışma, Python programlama dili kullanılarak gerçekleştirilmiş ve aşağıdaki adımları içermektedir:

1. Veri setlerinin yüklenmesi ve ön işleme adımları.
2. Verilerin görselleştirilmesi ve ilişkilerinin analizi.
3. İstatistiksel yöntemlerle değişkenlerin değerlendirilmesi.
4. Farklı makine öğrenimi algoritmalarının karşılaştırılması ve performans değerlendirmesi.
5. Modellerin avantaj ve dezavantajlarının yorumlanması.

---
## Kullanılan Dosyalar

GitHub deposunda yer alan dosyalar ve bu dosyaların işlevleri şu şekildedir:

- makk.py

Bu dosya, YouTube'den verilerin çekilmesi için yazılmış Python kodlarını içermektedir. İçeriğinde aşağıdaki işlemler gerçekleştirilir:

Belirli bir kanalın videolarına erişim sağlanır.

Videolara ait beğeni, yorum, görüntülenme sayısı gibi metrikler toplanır.

Toplanan veriler, CSV formatında saklanır.
Bu dosya, projenin veri toplama adımında kritik bir rol oynamaktadır.

- youtube_video_info.csv

Bu dosya, YouTube'dan elde edilen videolara ilişkin bilgileri içerir. İçerdiği sütunlar arasında şunlar yer alır:

`(Likes + Comments) / Views:` Beğeni ve yorum sayısının toplam izlenmeye oranı.

`Published Date:` Videonun yayınlanma tarihi.

`Video ID:` Videonun ID numarası.

`Video Title:` Videonun başlığı.

`Likes:` Videonun aldığı beğeni sayısı.

`Comments:` Videoya yapılan yorum sayısı.

`Views:` Videonun toplam görüntülenme sayısı.

`Daily Views:` Videonun günlük ortalama görüntülenme sayısı.

`Daily Likes:` Videonun günlük beğeni sayısı.

`Video Age (Days):` Videonun yayımlandığı günden itibaren geçen gün sayısı.

- youtube_channel_info.csv 

Bu dosya, kanallara ilişkin bilgileri içerir. Aşağıdaki gibi kanal hakkında genel bilgiler sağlar:

`Channel Name:` Kanalın adı.

`Channel ID:` Kanalın ID numarası.

`Subscribers:` Kanalın abone sayısı.

`Total Videos:` Kanalda yayınlanan toplam video sayısı.

`Views:` Kanalın toplam görüntülenme sayısı.
Bu dosya, kanal düzeyindeki genel istatistiklerin analizine olanak tanır.

- youtubeviews.py

Makine öğrenimi modellerinin uygulanması için geliştirilmiş bir Python betiğidir. Bu dosyada şunlar bulunur:

Veri ön işleme: Eksik verilerin temizlenmesi, aykırı değerlerin çıkarılması ve verilerin ölçeklenmesi.

Model oluşturma: Linear Regression, Random Forest Regressor ve K-Nearest Neighbors gibi algoritmaların eğitim ve testi.

Model performansı: Mean Squared Error ve R² metrikleri kullanılarak her modelin performansının değerlendirilmesi.

- youtubeviews.ipynb

Bu Jupyter Notebook dosyası, projenin tüm analizlerini adım adım gerçekleştiren bir not defteri olarak kullanılmıştır. İçerdiği başlıca işlemler şunlardır:

Veri yükleme ve görselleştirme.

ANOVA testi ve korelasyon analizi.

Farklı makine öğrenimi algoritmalarının performansının karşılaştırılması.

Görsellerle desteklenmiş detaylı analizler.
Bu dosya, projenin en önemli kod ve analiz kısımlarını içermektedir.

---
## Kullanılan Teknolojiler ve Kütüphaneler
Bu proje için aşağıdaki teknolojiler ve kütüphaneler kullanılmıştır:

### Temel Kütüphaneler
- **NumPy**: Sayısal veri işlemleri için kullanılmıştır.
- **Pandas**: Veri manipülasyonu ve analizi için tercih edilmiştir.

### Görselleştirme
- **Matplotlib**: Çeşitli grafikler oluşturulmuştur.
- **Seaborn**: Daha ayrıntılı ve estetik görselleştirme araçları için kullanılmıştır.

### Makine Öğrenimi
- **scikit-learn**: Model eğitimi, değerlendirme metrikleri ve veri ön işleme işlemleri için.
- **XGBoost**: Gelişmiş gradyan artışı algoritması.

---

## Veri Setleri
Proje, YouTube'dan elde edilen iki farklı veri setini kullanmıştır:

1. `youtube_channel_info.csv`: Kanala ilişkin bilgiler.
2. `youtube_video_info.csv`: Videolara ilişkin detaylı bilgiler.

### Veri Seti Özellikleri
- **Likes**: Videonun aldığı beğeni sayısı.
- **Comments**: Videoya yapılan yorum sayısı.
- **Views**: Videonun toplam görüntülenme sayısı.
- **Daily Views**: Videonun günlük ortalama görüntülenme sayısı.
- **Daily Likes**: Videonun günlük beğeni sayısı.
- **Video Age (Days)**: Videonun yayımlandığı günden itibaren geçen gün sayısı.
- **(Likes + Comments) / Views**: Beğeni ve yorumların toplam görüntülenme sayısına oranı.

---

## Uygulama Adımları

### 1. Veri Yükleme ve Ön İşleme
- Veri setleri Pandas kütüphanesi kullanılarak yüklendi.
- "Video Title", "Video ID" ve "Published Date" gibi analizle ilgisiz sütunlar kaldırıldı.
- Eksik veriler kontrol edildi ve temizlendi.
- "Views" sütunundaki değerler, MinMaxScaler kullanılarak 0 ile 1000 arasında ölçeklendi.

### 2. Veri Görselleştirme
- **Likes vs Views** ve **Comments vs Views** gibi ilişkiler scatterplot grafikleriyle incelendi.
- Korelasyon matrisi oluşturularak değişkenler arasındaki ilişkiler analiz edildi.

### 3. İstatistiksel Analiz
- ANOVA testi ile "Views" ile diğer sayısal değişkenler arasındaki anlamlı ilişkiler değerlendirildi.
- Aykırı değerler Z-skoru yöntemiyle belirlendi ve veri seti bu değerlere göre temizlendi.

### 4. Makine Öğrenimi Modelleri
Üç farklı makine öğrenimi algoritması, görüntülenme sayısını tahmin etmek için kullanıldı:

#### Linear Regression
Bu algoritma, bağımsız değişkenler ile hedef değişken arasındaki doğrusal ilişkiyi modellemek için kullanılmıştır. Linear Regression, basit yapısı ve açıklanabilirliği ile öne çıkmaktadır. Model, veri setindeki ilişkilerin doğrusallığı varsayımına dayanmaktadır. Ancak, karmaşık ilişkilerin bulunduğu durumlarda performans düşüklüğü gösterebilir. Modelin performansı, hedef değişkeni tahmin etme yeteneğinde oldukça başarılıdır, ancak yüksek değişkenlik içeren veri setlerinde sınırlı kalabilir.

#### Random Forest Regressor
Bu model, birden fazla karar ağacının birleşiminden oluşan bir gradyan artışı algoritmasıdır. Random Forest, doğrusal olmayan ilişkileri modelleme yeteneği ile Linear Regression'dan ayrılır. Model, özellikle karmaşık veri setlerinde ve çoklu değişkenler arasında güçlü ilişkilerin olduğu durumlarda daha başarılıdır. Ancak, bu modelde overfitting riski bulunmaktadır ve büyük veri setlerinde eğitim süresi daha uzun olabilir. Random Forest, daha fazla esneklik sağlamakla birlikte, açıklanabilirlik açısından Linear Regression'a kıyasla daha karmaşık bir yapıya sahiptir.

#### K-Nearest Neighbors Regressor
KNN Regressor, verilerin en yakın komşularını baz alarak tahmin yapar. Bu model, basit yapısı nedeniyle bazı durumlarda etkili olsa da, büyük ölçekli veri setlerinde performans sorunları yaşayabilir. Yüksek boyutlu verilerde doğruluğun azalması ve tahmin süresinin uzaması, KNN algoritmasının temel dezavantajlarıdır. Bununla birlikte, veri setindeki ilişkilere bağlı olarak güçlü bir performans gösterebilir. Bu model, genellikle doğrusal olmayan ilişkilerde daha etkili sonuçlar üretebilir, ancak parametre seçimi (örneğin, komşu sayısı) model performansını büyük ölçüde etkileyebilir.

---

## Modellerin Genel Karşılaştırması

1. **Linear Regression**:
   - Basit ve anlaşılır bir modeldir.
   - Doğrusal ilişkileri iyi modelleyebilir, ancak karmaşık ilişkilerde sınırlı kalabilir.
   - Hızlı çalışır ve açıklanabilirliği yüksektir.

2. **Random Forest Regressor**:
   - Doğrusal olmayan ilişkilerde üstün performans gösterir.
   - Esnek bir modeldir ancak eğitim süresi daha uzundur.
   - Overfitting riski taşır, ancak doğru hiperparametre ayarları ile bu risk azaltılabilir.

3. **KNN Regressor**:
   - Özellikle küçük ve orta boyutlu veri setlerinde etkili sonuçlar verir.
   - Büyük veri setlerinde performansı düşebilir.
   - Parametre seçiminde dikkatli olunması gerekir.

---

## Sonuç ve Öneriler
- **Linear Regression**, açıklanabilirliği ve hızlı çalışması nedeniyle tercih edilebilir. Ancak karmaşık ilişkilerin olduğu durumlarda daha güçlü modellerle desteklenmelidir.
- **Random Forest Regressor**, genelde en iyi performansı sağlayan modeldir ve doğrusal olmayan ilişkileri iyi bir şekilde modelleyebilir. Karmaşık veri setlerinde tercih edilmelidir.
- **KNN Regressor**, veri seti küçük olduğunda etkili bir alternatif olabilir. Ancak yüksek boyutlu veri setlerinde dikkatli bir şekilde değerlendirilmelidir.

---

## Projenin Kullanımı
Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Python ve gerekli kütüphaneler sisteminizde kurulu olmalıdır.
2. Veri setleri, proje dizininde yer almalıdır.
3. Python betiği veya Jupyter Notebook üzerinde kod çalıştırılabilir.
4. Kod çalıştırıldığında sonuçlar görselleştirme ve metrikler ile birlikte ekranda görüntülenir.

---

## Youtube Video Linkim: 
https://www.youtube.com/watch?v=dFGk1Jw18o8


## Lisans
Bu proje MIT lisansı altında paylaşılmıştır.


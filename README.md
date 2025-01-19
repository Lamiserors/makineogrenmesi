# YouTube Video ve Kanal Verisi Analizi

## Proje Hakkında
Bu proje, YouTube kanallarına ve videolarına ait verilerin analiz edilmesi, görselleştirilmesi ve modelleme yapılmasını içermektedir. Veri analizi ve makine öğrenimi yöntemleri kullanılarak videoların görüntülenme sayısını tahmin etme amaçlanmıştır. 

Proje, Python programlama dili kullanılarak geliştirilmiş ve aşağıdaki adımları içermektedir:
1. Veri yükleme ve ön işleme
2. Veri görselleştirme
3. İstatistiksel analiz
4. Makine öğrenimi modelleriyle tahmin
5. Model performans değerlendirmesi

---

## Kullanılan Teknolojiler ve Kütüphaneler
Proje, aşağıdaki kütüphaneleri ve araçları kullanmaktadır:

### Temel Kütüphaneler
- **NumPy**: Sayısal hesaplamalar
- **Pandas**: Veri işleme ve analizi

### Görselleştirme
- **Matplotlib**: Grafikler oluşturma
- **Seaborn**: Veri görselleştirme için gelişmiş araçlar

### Makine Öğrenimi
- **scikit-learn**: Model seçimi, eğitimi ve değerlendirmesi
- **XGBoost**: Güçlü gradyan artış modelleri

---

## Veri Setleri
Proje, iki farklı CSV dosyasından yüklenen YouTube verilerini kullanır:

1. `youtube_channel_info.csv`: Kanallara ait bilgiler.
2. `youtube_video_info.csv`: Videolara ait bilgiler.

### Veri Seti Özellikleri
- **Video Title**: Videonun başlığı
- **Video ID**: Videonun benzersiz kimliği
- **Published Date**: Yayınlanma tarihi
- **Likes**: Beğeni sayısı
- **Comments**: Yorum sayısı
- **Views**: Görüntülenme sayısı
- **Daily Views**: Günlük görüntülenme sayısı
- **Daily Likes**: Günlük beğeni sayısı
- **Video Age (Days)**: Videonun yayınlandığı günden bu yana geçen gün sayısı
- **(Likes + Comments) / Views**: Beğeni ve yorumların görüntülenme sayısına oranı

---

## Uygulama Adımları

### 1. Veri Yükleme ve Ön İşleme
- Veri setleri `read_csv` ile yüklendi.
- İlgisiz sütunlar ("Video Title", "Video ID", "Published Date") veri setinden kaldırıldı.
- Eksik veriler kontrol edildi.

### 2. Veri Görselleştirme
- Scatterplot kullanılarak değişkenler arasındaki ilişkiler incelendi:
  - Likes vs Views
  - Comments vs Views
  - Daily Likes vs Daily Views
- Korelasyon matrisi oluşturuldu ve ısı haritası ile görselleştirildi.

### 3. İstatistiksel Analiz
- ANOVA testi ile farklı değişkenlerin "Views" üzerinde anlamlı bir etkisi olup olmadığı analiz edildi.
- Z-skoru yöntemi ile aykırı değerler filtrelendi.

### 4. Makine Öğrenimi Modelleri
Aşağıdaki modeller kullanılarak "Views" değerinin tahmini yapıldı:

#### 4.1. Linear Regression

- **Değerlendirme**: Linear Regression modeli yüksek bir R² (0.9824) skoru ile başarılı bir performans sergiledi. Ancak, bu model doğrusallık varsayımına dayandığı için karmaşık ilişkilerde daha düşük performans gösterebilir. MSE değerinin büyük olması, yüksek ölçekli veri setlerinden kaynaklanabilir.

#### 4.2. Random Forest Regressor

- **Değerlendirme**: Random Forest modeli, veri setinin karmaşıklığını yakalayarak oldukça iyi bir tahmin gerçekleştirmiştir. Ancak, MSE değerinin Linear Regression modelinden daha yüksek olması, overfitting riskine işaret edebilir. Yine de, bu model geniş veri setlerinde ve karmaşık ilişkilerde etkili bir yöntemdir.

#### 4.3. K-Nearest Neighbors Regressor

- **Değerlendirme**: KNN Regressor, diğer modellere kıyasla daha düşük bir performans sergilemiştir. Özellikle büyük veri setlerinde ve yüksek boyutlu uzaylarda KNN algoritmasının performansı genellikle düşer. Bu durum, modelin yavaş çalışmasına ve doğruluğun azalmasına neden olmuştur.

---

## Model Performans Karşılaştırması


- **Linear Regression** en yüksek R² skoruna sahip olup, verilere iyi bir uyum sağlamıştır.
- **Random Forest Regressor**, karmaşık ilişkileri modellemede etkili olsa da, biraz daha düşük bir performans sergilemiştir.
- **KNN Regressor**, diğer modellere kıyasla daha düşük bir doğruluk sunmuş ve özellikle büyük ölçekli verilere karşı hassasiyet göstermiştir.

---

## Gereksinimler
Projeyi çalıştırabilmek için aşağıdaki kütüphanelerin kurulu olması gerekir:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
```

---

## Çalıştırma Adımları
1. Veri setlerini proje dizinine ekleyin.
2. Python betiğini çalıştırın ya da Jupyter Notebook üzerinde kodu çalıştırın.

---

---

## Lisans
Bu proje MIT lisansı altında paylaşılmıştır.


# Küçük İşletme Kasa Defteri ve Günlük Rapor Uygulaması

Bu proje, **Bahçeşehir Üniversitesi GEP1316 Kodlama Okuryazarlığı** dersi **Ara Değerlendirme Ödevi 1** kapsamında geliştirilmiş bir Python komut satırı (CLI) uygulamasıdır.

## Projenin Amacı
Küçük ölçekli işletmelerde günlük gelir ve gider takibinin kağıt üzerinde yapılması sırasında oluşan KDV hesaplama hatalarını ve yanlış veri girişlerini önlemek amacıyla geliştirilmiştir. Uygulama; işlemleri doğrular, KDV dahil tutarları otomatik hesaplar, gün sonu kâr/zarar durumunu analiz eder ve sonuçları `.csv` formatında kaydeder.

## Özellikler
- **Girdi Doğrulama:** İşlem türü, açıklama, KDV hariç tutar ve KDV oranı (%1, %10, %20) kontrol edilir; hatalı veya negatif girdilerde program çökmez, uyarı verir.
- **Karar Yapıları ve Döngüler:** Menü yönetimi, girdi doğrulama ve gün sonu net kasa değerlendirmesi için `while`, `for` ve `if/elif/else` yapıları kullanılmıştır.
- **Fonksiyonlar ve Veri Yapıları:** Uygulama 5 modüler fonksiyondan (`gecerli_tutar_al`, `gecerli_kdv_al`, `yeni_islem_ekle`, `ozet_hesapla`, `raporu_goster`, `dosyaya_kaydet`) oluşur ve verileri liste (`list`) içinde sözlük (`dict`) olarak saklar.
- **Dosya Çıktısı:** Sonuçlar `kasa_raporu.csv` dosyasına kaydedilir.

## Nasıl Çalıştırılır?
1. Depoyu bilgisayarınıza indirin:
   ```bash
   git clone [https://github.com/alitalhaucuncu-boop/Kasa-defteri-uygulamasi.git](https://github.com/alitalhaucuncu-boop/Kasa-defteri-uygulamasi.git)

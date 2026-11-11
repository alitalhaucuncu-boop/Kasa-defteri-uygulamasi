# GEP1316 Kodlama Okuryazarlığı - Ara Değerlendirme Ödevi 1
# Öğrenci: Ali Taha Üçüncü
# Proje: Küçük İşletme Kasa Defteri ve Günlük Rapor Uygulaması

# Tüm kasa işlemlerini içinde tutacağımız ana liste
islemler = []


def gecerli_tutar_al():
    """Kullanıcıdan pozitif bir tutar alır, harf veya eksi girilirse uyarır."""
    while True:
        girilen = input("KDV Hariç Tutar (TL): ")
        # Kullanıcı virgül girdiyse noktaya çeviriyoruz ki float() hata vermesin
        girilen = girilen.replace(",", ".")
        try:
            tutar = float(girilen)
            if tutar <= 0:
                print("Uyarı: Tutar 0 veya negatif olamaz! Lütfen tekrar girin.")
            else:
                return round(tutar, 2)
        except ValueError:
            print("Hata: Lütfen tutar kısmına sadece sayı giriniz! (Örn: 750.50)")


def gecerli_kdv_al():
    """Kullanıcıdan Türkiye'deki geçerli KDV oranlarından (1, 10, 20) birini alır."""
    while True:
        girilen = input("KDV Oranı (%1, %10 veya %20 için 1, 10, 20 yazın): ")
        try:
            kdv = int(girilen)
            if kdv == 1 or kdv == 10 or kdv == 20:
                return kdv
            else:
                print("Uyarı: Sadece 1, 10 veya 20 KDV oranlarından birini seçebilirsiniz.")
        except ValueError:
            print("Hata: KDV oranı için lütfen tam sayı giriniz!")


def yeni_islem_ekle():
    """Kullanıcıdan bilgileri alıp sözlük (dict) olarak listeye ekler."""
    print("\n--- YENİ İŞLEM GİRİŞİ ---")

    # 1. Girdi: İşlem Türü (Gelir / Gider)
    while True:
        tur_secim = input("İşlem Türü (1: Gelir / 2: Gider): ").strip()
        if tur_secim == "1":
            tur = "Gelir"
            break
        elif tur_secim == "2":
            tur = "Gider"
            break
        else:
            print("Hatalı seçim! Gelir için 1, Gider için 2 yazmalısınız.")

    # 2. Girdi: Açıklama
    while True:
        aciklama = input("İşlem Açıklaması (Örn: Günlük Satış, Kira, Fatura): ").strip()
        if len(aciklama) > 1:
            break
        else:
            print("Uyarı: Açıklama kısmı boş bırakılamaz!")

    # 3. ve 4. Girdiler: Tutar ve KDV (Yukarıdaki fonksiyonlarla doğrulanarak alınır)
    tutar = gecerli_tutar_al()
    kdv_orani = gecerli_kdv_al()

    # KDV ve Toplam Tutar Hesaplaması
    kdv_tutari = round(tutar * (kdv_orani / 100), 2)
    toplam_tutar = round(tutar + kdv_tutari, 2)

    # Bilgileri bir sözlük (dictionary) yapısında topluyoruz
    islem_sozlugu = {
        "no": len(islemler) + 1,
        "tur": tur,
        "aciklama": aciklama,
        "tutar": tutar,
        "kdv_orani": kdv_orani,
        "kdv_tutari": kdv_tutari,
        "toplam": toplam_tutar
    }

    islemler.append(islem_sozlugu)
    print(f"--> Başarıyla eklendi: {aciklama} ({tur}) - KDV Dahil: {toplam_tutar} TL")


def ozet_hesapla():
    """Listedeki gelir ve giderleri toplayıp net bakiyeyi ve kasa durumunu döndürür."""
    toplam_gelir = 0.0
    toplam_gider = 0.0
    toplam_kdv = 0.0

    for kayit in islemler:
        toplam_kdv = toplam_kdv + kayit["kdv_tutari"]
        if kayit["tur"] == "Gelir":
            toplam_gelir = toplam_gelir + kayit["toplam"]
        else:
            toplam_gider = toplam_gider + kayit["toplam"]

    net_kasa = round(toplam_gelir - toplam_gider, 2)

    # Karar yapısı ile işletmenin günlük durumu
    if net_kasa > 5000:
        durum = "Çok İyi (Günlük kâr hedefi aşıldı)"
    elif net_kasa > 0:
        durum = "Pozitif (Kasa kârda)"
    elif net_kasa == 0:
        durum = "Başabaş (Gelir ve gider eşit)"
    else:
        durum = "Dikkat: Kasa ekside (Giderler gelirden fazla!)"

    ozet = {
        "gelir": round(toplam_gelir, 2),
        "gider": round(toplam_gider, 2),
        "kdv": round(toplam_kdv, 2),
        "net": net_kasa,
        "durum": durum
    }
    return ozet


def raporu_goster():
    """Kasa hareketlerini ve gün sonu özetini ekrana düzenli şekilde yazdırır."""
    if len(islemler) == 0:
        print("\nHenüz hiç işlem eklenmedi! Önce menüden 1'i seçip işlem ekleyin.")
        return

    print("\n================================================================")
    print("                GÜNLÜK KASA HAREKETLERİ RAPORU                  ")
    print("================================================================")
    print("No | Tür   | Açıklama             | KDV Oranı | KDV Dahil Tutar")
    print("----------------------------------------------------------------")

    for k in islemler:
        print(f"{k['no']:<2} | {k['tur']:<5} | {k['aciklama']:<20} | %{k['kdv_orani']:<8} | {k['toplam']} TL")

    ozet_bilgi = ozet_hesapla()
    print("================================================================")
    print(f"Toplam Gelir (KDV Dahil) : {ozet_bilgi['gelir']} TL")
    print(f"Toplam Gider (KDV Dahil) : {ozet_bilgi['gider']} TL")
    print(f"Toplam Hesaplanan KDV    : {ozet_bilgi['kdv']} TL")
    print(f"NET KASA BAKİYESİ        : {ozet_bilgi['net']} TL")
    print(f"Gün Sonu Değerlendirmesi : {ozet_bilgi['durum']}")
    print("================================================================")


def dosyaya_kaydet():
    """Verileri hem okunabilir metin hem de Excel uyumlu olarak kasa_raporu.csv dosyasına yazar."""
    if len(islemler) == 0:
        print("\nKaydedilecek işlem yok! Lütfen önce işlem ekleyin.")
        return

    ozet_bilgi = ozet_hesapla()

    # Dosyayı yazma ('w') modunda açıyoruz
    dosya = open("kasa_raporu.csv", "w", encoding="utf-8")

    # CSV sütun başlıkları (Noktalı virgül ile ayrılmış)
    dosya.write("Islem No;Tur;Aciklama;KDV Haric Tutar;KDV Orani;KDV Tutari;KDV Dahil Toplam\n")

    # Tüm işlemleri döngü ile satır satır dosyaya yazıyoruz
    for k in islemler:
        satir = f"{k['no']};{k['tur']};{k['aciklama']};{k['tutar']};%{k['kdv_orani']};{k['kdv_tutari']};{k['toplam']}\n"
        dosya.write(satir)

    # En alta özet satırlarını ekliyoruz
    dosya.write("\n--- GUN SONU OZETI ---\n")
    dosya.write(f"Toplam Gelir;{ozet_bilgi['gelir']} TL\n")
    dosya.write(f"Toplam Gider;{ozet_bilgi['gider']} TL\n")
    dosya.write(f"Net Kasa Bakiyesi;{ozet_bilgi['net']} TL\n")
    dosya.write(f"Durum;{ozet_bilgi['durum']}\n")

    dosya.close()
    print("\n--> Rapor başarıyla 'kasa_raporu.csv' dosyasına kaydedildi!")


# --- ANA PROGRAM DÖNGÜSÜ ---
print("***************************************************")
print("  KÜÇÜK İŞLETME KASA DEFTERİ UYGULAMASINA HOŞ GELDİNİZ")
print("***************************************************")

while True:
    print("\n--- ANA MENÜ ---")
    print("1 - Yeni Gelir / Gider Ekle")
    print("2 - Günlük Kasa Raporunu Göster")
    print("3 - Raporu Dosyaya Kaydet (kasa_raporu.csv)")
    print("4 - Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ").strip()

    if secim == "1":
        yeni_islem_ekle()
    elif secim == "2":
        raporu_goster()
    elif secim == "3":
        dosyaya_kaydet()
    elif secim == "4":
        print("Program kapatılıyor... İyi çalışmalar!")
        break
    else:
        print("Hatalı seçim yaptınız! Lütfen menüden 1, 2, 3 veya 4 giriniz.")

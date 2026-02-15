# Furkan Dalmaz
# Python öğrenme sürecimde geliştirdiğim basit not ortalaması hesaplama programı
# Kullanıcıdan alınan notlara göre ortalama hesaplar ve sonucu gösterir

print("📚 Öğrenci Not Ortalaması Hesaplama Programı")

try:
    not1 = float(input("1. notu girin: "))
    not2 = float(input("2. notu girin: "))
    not3 = float(input("3. notu girin: "))

    ortalama = (not1 + not2 + not3) / 3

    print(f"\nOrtalamanız: {ortalama:.2f}")

    if ortalama >= 85:
        print("Harf Notu: AA 🎉")
    elif ortalama >= 70:
        print("Harf Notu: BB 👍")
    elif ortalama >= 50:
        print("Harf Notu: CC 🙂")
    else:
        print("Harf Notu: FF 😔")

    if ortalama >= 50:
        print("✅ Tebrikler dersi geçtiniz")
    else:
        print("❌ Maalesef kaldınız")

except ValueError:
    print("⚠️ Lütfen geçerli bir sayı giriniz")

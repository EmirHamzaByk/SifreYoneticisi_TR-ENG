import os

def update_password(website, kullanici_adi, sifre):
    lines = []
    with open("sifreler.txt", "r" , encoding="utf-8") as f:
        for line in f:
            if website in line:
                line = website + " : " + kullanici_adi + " : " + sifre + "\n"
            lines.append(line)
    with open("sifreler.txt", "w" , encoding="utf-8") as f:
        f.writelines(lines)

def delete_password(website):
    lines = []
    with open("sifreler.txt", "r" , encoding="utf-8") as f:
        for line in f:
            if website not in line:
                lines.append(line)
    with open("sifreler.txt", "w" , encoding="utf-8") as f:
        f.writelines(lines)

def save_password(website,kullanici_adi,sifre):
    with open("sifreler.txt", "a" , encoding="utf-8") as f:
        f.write(website + " : " + kullanici_adi + " : " + sifre + "\n")

def get_passwords():
    with open("sifreler.txt", "r" , encoding="utf-8") as f:
        return f.read()

def main():
    while True:
        secim = input("1. URL, kullanıcı adı ve şifre girin.\n2. Kayıtlı bilgileri göster.\n3. Kayıtlı bilgileri güncelle.\n4. Kayıtlı bilgilerden sil.\n5. Cikis\nSeciminizi yapin-->  ")
        if secim == "1":
            website = input("URL: ")
            kullanici_adi = input("Kullaniıcı adı: ")
            sifre = input("Şifre: ")
            save_password(website,kullanici_adi,sifre)
            print("Bilgiler kaydedildi.")
        elif secim == "2":
            print("Kayitli Bilgiler: ")
            print(get_passwords())
        elif secim == "3":
            website = input("URL gir: ")
            kullanici_adi = input("Yeni kullanici adi gir: ")
            sifre = input("Yeni sifre gir: ")
            update_password(website, kullanici_adi, sifre)
            print("Bilgiler güncellendi. ")
        elif secim == "4":
            website = input("URL gir: ")
            delete_password(website)
            print("Bilgiler silindi.")
        elif secim == "5":
            print("Çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.Lütfen 1-5 arasında bir sayı seçiniz.")

if __name__ == "__main__":
    main()

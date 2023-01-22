# Şifre Yöneticisi
Bu kod, kullanıcının girdiği website, kullanıcı adı ve şifre bilgilerini saklamak ve düzenlemek için kullanılan bir Python uygulamasıdır. Kod, bir kullanıcı arayüzü aracılığıyla çalışır ve kullanıcıya birkaç seçenek sunar seçenekler ve açıklamaları:

1."URL, kullanıcı adı ve şifre girin": Kullanıcıya , bir website adresi, bir kullanıcı adı ve bir şifre girme seçeneği sunulur. Bu bilgiler "sifreler.txt" dosyasına kaydedilir.

2."Kayıtlı bilgileri göster": Kullanıcı, kayıtlı olan tüm website, kullanıcı adı ve şifre bilgilerini görüntüleyebilir.

3."Kayıtlı bilgileri güncelle": Kullanıcı, daha önce kaydedilmiş bir website adresi için kullanıcı adı ve şifre bilgilerini güncelleyebilir. Kullanıcı, güncellemek istediği website adresini girer ve yeni kullanıcı adı ve şifre bilgilerini girir. Kod, "sifreler.txt" dosyasını okur ve güncellemek istediği website adresi için bilgileri günceller.

4."Kayıtlı bilgilerden sil": Kullanıcı, daha önce kaydedilmiş bir website adresi için bilgileri silebilir. Kullanıcı, silmek istediği website adresini girer ve kod, "sifreler.txt" dosyasını okur ve silmek istediği website adresi için bilgileri siler.

5."Çıkış": Kullanıcı, uygulamadan çıkmak istediğinde bu seçeneği kullanır.
Kod, "sifreler.txt" dosyasını kullanır ve kullanıcının girdiği bilgileri bu dosyaya kaydeder veya siler veya günceller.

Kod kullanıcının yaptığı seçimleri anlamak için "if" ve "elif" yapılarını kullanır. Eğer kullanıcı geçersiz bir seçim yaparsa, kod "Geçersiz seçim. Lütfen 1-5 arasında bir sayı seçiniz." uyarısını verir.

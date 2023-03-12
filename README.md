# Pizza Sipariş Sistemi
## Proje Genel Bakışı
Bu proje, kullanıcıların kendi pizzalarını tasarlamalarını ve ödeme yaptıktan sonra kullanıcıyı veri tabanına eklemelerini hedeflemektedir. Sistem, kullanıcıların menüdeki pizzayı ve istedikleri sosu seçmesiyle başlar. İkinci aşama olarak seçtikleri sos ve pizzayı seçtikten sonra ödemeye kısmına geçiş yaparlar. Kullanıcılar ödemelerini kredi kartı ile yapacaktır. Her pizzanın bir açıklaması ve fiyatı vardır.

# Proje Adımları
## Google Colab Dosyası Oluşturma:

Projenizin .ipynb veya .py uzantısına sahip olduğundan emin olun.
Projenizde ayrıntıları açıklayan yorum satırları olduğundan emin olun.
Gerekli Kitaplıkları İçe Aktarma:

csv kitaplığını içe aktarın.
datetime kitaplığını içe aktarın.
Menu.txt Dosyasını Oluşturma:

Menu.txt adlı bir dosya oluşturun ve içine aşağıdaki metni yazın.

yaml
``` * Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
* ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Mısır
* Teşekkür ederiz! ```

### Pizza Üst Sınıfını Oluşturma:

Pizza sınıfını oluşturun.
Bu sınıfın içindeki encapsulation(kapsülleme) için ``` get_description()``` ve ```get_cost() ``` methodlarını tanımlayın.
NOT: Bu açıklama hazırlanan pizzanın kısa bir açıklaması olmalıdır!

### Pizza Alt Sınıflarını Oluşturma:
Klasik, Margherita, Türk Pizzası, Dominos Pizza vb. pizza sınıflarını oluşturun.
Her pizzanın kendine ait bir fiyatı ve sahip olduğu değişkenin içinde pizzaların açıklamasının yer alması gerektiğini unutmayın.
Decorator Üst Sınıfını Oluşturma:

### Bir Decorator sınıfı oluşturun.
Decorator, burada tüm sos sınıflarının süper sınıfı olarak adlandırılır.
Decorator sınıfı, Pizza sınıfının özell

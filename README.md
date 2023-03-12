# Pizza Sipariş Sistemi

## Proje Genel Bakış

Bu proje, bir pizzacı dükkanının müşterilerinin kendi pizzalarını tasarlamalarını ve ödeme yaptıktan sonra veritabanına kaydetmelerini sağlayan bir sistemdir. Kullanıcılar menüdeki pizzayı ve istedikleri sosu seçerek başlarlar. Daha sonra ödeme yaparlar ve ödemelerini kredi kartı ile yaparlar. Her pizzanın bir açıklaması ve fiyatı vardır.

## Gereksinimler

- csv kütüphanesi
- datetime kütüphanesi

## Menü Dosyası Oluşturma

Menu.txt adlı bir dosya oluşturun ve içine aşağıdaki metni yazın.

Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Mısır
Teşekkür ederiz!


## Üst Sınıf Oluşturma: "Pizza"

Pizza sınıfını ve bu sınıfın içindeki encapsulation(kapsülleme) için get_description() ve get_cost() methodları tanımlayın.

```python
class Pizza:
    def __init__(self, description="", cost=0):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
```
# Alt Sınıf Oluşturma: "Pizza"
Klasik, Margherita, Türk Pizzası vb. pizza sınıfları oluşturun. Her bir pizzanın kendine ait bir fiyatı ve açıklaması olmalıdır.

```python
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 15)

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 18)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 20)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 12)
```

# Üst Sınıf Oluşturma: "Decorator"
Bir Decorator sınıfı oluşturun. Decorator, burada tüm sos sınıflarının süper sınıfı olarak adlandırılır.
Decorator sınıfı, pizza sınıfının özelliklerini kullanarak get_description() ve get_cost() yöntemlerini kullanacaktır.

```python
class SosDecorator(Pizza):
    def __init__(self, pizza, description="", cost=0):
        super().__init__(description, cost)
        self.component = pizza

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() +
```
## Not: 
Bu proje sadece bir örnek projedir ve gerçek bir pizzacı dükkanı için kullanılmamalıdır. 
Gerçek bir pizzacı dükkanı için daha kapsamlı bir sistem tasarlanmalıdır.

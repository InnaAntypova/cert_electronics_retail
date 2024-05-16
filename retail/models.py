from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Contacts(models.Model):
    """ Модель для сущности Contacts (Контакты) """
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=15, verbose_name='Номер дома', **NULLABLE)

    def __str__(self):
        return f'{self.country} / {self.city} / {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Products(models.Model):
    """ Модель для сущности Products (Продукты) """
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель', **NULLABLE)
    product_release_date = models.DateField(verbose_name='Дата выхода продукта на рынок', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.title} / {self.model} / {self.product_release_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Dealer(models.Model):
    """ Модель для сущности Dealer (Дилер) """
    TYPE = {
        'FACTORY': 'Завод',
        'RETAIL': 'Розничная сеть',
        'INDIVIDUAL': 'Индивидуальный предприниматель'
    }

    def get_level(self):
        """ Метод для вычисления уровня иерархии в торговой сети """
        if self.dealer_type == 'FACTORY':
            self.level = 0
        else:
            self.level = self.shipper.level + 1

    title = models.CharField(max_length=150, verbose_name='Название')
    contacts = models.ForeignKey('retail.Contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ForeignKey('retail.Products', on_delete=models.CASCADE, verbose_name='Продукты', **NULLABLE)
    shipper = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    dealer_type = models.CharField(choices=TYPE, verbose_name='Тип звена торговой сети')
    level = models.SmallIntegerField(default=get_level, verbose_name='Уровень иерархии в торговой сети')

    def __str__(self):
        return f'{self.title} / {self.debt}, {self.dealer_type} / {self.level}'

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'

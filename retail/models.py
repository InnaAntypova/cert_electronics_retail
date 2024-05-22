from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Products(models.Model):
    """ Модель для сущности Products (Продукты) """
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=50, verbose_name='Модель', **NULLABLE)
    product_release_date = models.DateField(verbose_name='Дата выхода продукта на рынок', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь владелец')

    def __str__(self):
        return f'{self.title} {self.model}'

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

    title = models.CharField(max_length=150, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=15, verbose_name='Номер дома', **NULLABLE)
    products = models.ManyToManyField('retail.Products', verbose_name='Продукты')
    shipper = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком', **NULLABLE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    dealer_type = models.CharField(choices=TYPE, verbose_name='Тип звена торговой сети')
    level = models.SmallIntegerField(verbose_name='Уровень иерархии в торговой сети', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь владелец')

    def save(self, *args, **kwargs):
        if not self.shipper or self.dealer_type == 'FACTORY':  # Нет поставщика выше\Завод всегда на нулевом уровне
            self.level = 0
        else:
            self.level = self.shipper.level + 1  # следующий уровень от поставщика
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}, {self.dealer_type}'

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилеры'

from django.contrib import admin
from retail.models import Products, Dealer
from django.utils.html import format_html


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'product_release_date', 'price', 'quantity')


@admin.action(description='Очистить задолженность')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'country', 'city', 'street', 'house_number', 'view_shipper_link', 'created',
                    'dealer_type', 'level', 'debt', 'get_debt', 'get_products_')
    list_filter = ('country',)
    actions = [clear_debt]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('products')

    @admin.display(description='Продукты')
    def get_products_(self, obj):
        return '\n'.join([str(i) for i in obj.products.all()])

    @admin.display(description='Поставщик')
    def view_shipper_link(self, obj):
        """ Ссылка на Поставщика """
        if obj.shipper:
            link = f'/admin/retail/dealer/{obj.shipper.id}/change/'
            return format_html(f'<a href={link}>{obj.shipper.title}</a>')
        return ''

    @admin.display(description='Долг поставщику')
    def get_debt(self, obj):
        if obj.shipper:
            for i in obj.products.all():
                return i.price * i.quantity

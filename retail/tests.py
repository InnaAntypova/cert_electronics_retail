from rest_framework.test import APITestCase
from rest_framework import status
from retail.models import Products, Dealer
from users.models import User


class ProductTestCase(APITestCase):
    """ Тестирование CRUD для модели Products """

    def setUp(self) -> None:
        # пользователь для теста
        self.user = User.objects.create_user(
            email='test@test.ru',
            password='12345',
            is_active=True
        )
        # продукт для теста
        self.product = Products.objects.create(
            title='Test_product_1',
            model='HP_01',
            price='15230.75',
            quantity='7',
            owner=self.user
        )

    def test_create_product(self):
        """ Тест на создание экземпляра модели Products """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test_product_2',
            'model': 'KGD-1',
            'price': '3650.50',
            'quantity': '3',
            'owner': self.user.id
        }
        response = self.client.post('/api/retail/products/', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEquals(
            response.json(),
            {'title': 'Test_product_2', 'model': 'KGD-1', 'product_release_date': None, 'price': '3650.50',
             'quantity': 3, 'owner': self.user.id}
        )

    def test_list_products(self):
        """ Тест на получение списка экземпляров модели Products """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/retail/products/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            [{'title': 'Test_product_1', 'model': 'HP_01', 'product_release_date': None, 'price': '15230.75',
             'quantity': 7, 'owner': self.user.id}]
        )

    def test_update_products(self):
        """ Тест на обновление экземпляра модели Products """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': self.product.title,
            'price': '15550',
            'quantity': '5'
        }
        response = self.client.patch(f'/api/retail/products/{self.product.id}/', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'title': 'Test_product_1', 'model': 'HP_01', 'product_release_date': None, 'price': '15550.00',
             'quantity': 5, 'owner': self.user.id}
        )

    def test_no_owner_product(self):
        """ Тест на владельца экземпляра модели Products"""
        self.user2 = User.objects.create_user(
            email='test2@test.ru',
            password='12345',
            is_active=True
        )
        self.client.force_authenticate(user=self.user2)
        data = {
            'title': self.product.title,
            'price': '1000',
            'quantity': '5'
        }
        response = self.client.patch(f'/api/retail/products/{self.product.id}/', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        response2 = self.client.delete(f'/api/retail/products/{self.product.id}/')
        self.assertEquals(
            response2.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_product(self):
        """ Тест на удаление экземпляра модели Products """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/retail/products/{self.product.id}/')
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class DealerTestCase(APITestCase):
    """ Тестирование CRUD модели Dealer (Дилер) """
    def setUp(self) -> None:
        # пользователь для теста
        self.user = User.objects.create_user(
            email='test@test.ru',
            password='12345',
            is_active=True
        )
        # продукт для теста
        self.product = Products.objects.create(
            title='Test_product_1',
            model='HP_01',
            price='15230.75',
            quantity='7',
            owner=self.user
        )
        # дилеры для теста
        self.dealer = Dealer.objects.create(
            title='Test_Dealer',
            email='test_dealer@test.ru',
            dealer_type='FACTORY',
            owner=self.user
        )
        self.dealer2 = Dealer.objects.create(
            title='Test_Dealer_2',
            email='test_dealer_2@test.ru',
            dealer_type='RETAIL',
            owner=self.user
        )

    def test_create_dealer(self):
        """ Тест на создание экземпляра модели Dealer """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Test_dealer2',
            'email': 'test_dealer2@test.ru',
            'dealer_type': 'RETAIL',
            'owner': self.user.id
        }
        response = self.client.post('/api/retail/', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEquals(
            response.json(),
            {'title': 'Test_dealer2', 'dealer_type': 'RETAIL', 'email': 'test_dealer2@test.ru', 'country': None,
             'city': None, 'street': None, 'house_number': None, 'shipper': None, 'owner': self.user.id}
        )

    def test_list_dealers(self):
        """ Тест на получение списка экземпляров модели Dealer """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/retail/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_dealer(self):
        """ Тест на обновление экземпляра модели Dealer """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': self.dealer2.title,
            'email': self.dealer2.email,
            'dealer_type': self.dealer2.dealer_type,
            'shipper': self.dealer.id,
            'owner': self.user.id
        }
        response = self.client.patch(f'/api/retail/{self.dealer2.id}/', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            {'title': 'Test_Dealer_2', 'dealer_type': 'RETAIL', 'email': 'test_dealer_2@test.ru', 'country': None,
             'city': None, 'street': None, 'house_number': None, 'products': [], 'shipper': self.dealer.id,
             'debt': '0.00', 'created': self.dealer2.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 'level': 1}
        )
        # добавить продукты (поле many-to-many)
        self.dealer2.products.add(self.product)
        response2 = self.client.get(f'/api/retail/{self.dealer2.id}/')
        self.assertEquals(
            response2.json(),
            {'title': 'Test_Dealer_2', 'dealer_type': 'RETAIL', 'email': 'test_dealer_2@test.ru', 'country': None,
             'city': None, 'street': None, 'house_number': None, 'products': [
                {'title': 'Test_product_1', 'model': 'HP_01', 'product_release_date': None, 'price': '15230.75',
                 'quantity': 7, 'owner': self.product.owner.pk}], 'shipper': self.dealer.id, 'debt': '0.00',
             'created': self.dealer2.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 'level': 1}
        )

    def test_no_owner(self):
        """ Тест на владельца экземпляра модели Dealer """
        self.user2 = User.objects.create_user(
            email='test2@test.ru',
            password='12345',
            is_active=True
        )
        self.client.force_authenticate(user=self.user2)
        data = {
            'title': self.dealer.title,
            'email': self.dealer.email,
            'dealer_type': self.dealer.dealer_type,
            'shipper': self.dealer2.id,
            'owner': self.user.id
        }
        response = self.client.patch(f'/api/retail/{self.dealer.id}/', data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
        response2 = self.client.delete(f'/api/retail/{self.dealer.id}/')
        self.assertEquals(
            response2.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_dealer(self):
        """ Тест на удаление экземпляра модели Dealer """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/retail/{self.dealer2.id}/')
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
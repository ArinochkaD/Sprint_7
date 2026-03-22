import allure
import requests

from utils.constants import Urls

class TestListOrders:
    @allure.feature('Функциональность получения списка заказа.')
    @allure.title('Проверка успешного получения списка заказа.')
    def test_get_list_orders(self):
        url = Urls.BASE_URL + Urls.CREATE_ORDER_PATH
        response = requests.get(url)
        assert response.status_code == 200 and response.json()['orders'] is not None

import json

import allure
import pytest
import requests

from utils.constants import Urls
from utils.credentials import Credentials
from utils.order_data import OrderData

class TestCreateOrder:
    @allure.feature('Функциональность создания заказа.')
    @allure.title('Проверка успешного создания заказа.')
    @allure.testcase('Различный выбор цветов.')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    def test_create_order(self, color, deafault_order: OrderData):
        url = Urls.BASE_URL + Urls.CREATE_ORDER_PATH
        data = deafault_order.copyWith(
            color = color
        )
        response = requests.post(url, json.dumps(data.toMap()), headers = {'Content-Type': 'application/json'})
        assert response.status_code == 201 and response.json()['track'] is not None

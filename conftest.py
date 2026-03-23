import sys
import os

import allure
import pytest
import requests

from utils.constants import Urls
from utils.credentials import Credentials, CredentialsGenerator
from utils.order_data import OrderData

# Добавляем текущую директорию в sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def credentials():
    return CredentialsGenerator.generate()

@pytest.fixture
def registered_credentials():
    return Credentials.registered_user()

@pytest.fixture
def deafault_order():
    return OrderData.test_order()

@pytest.fixture
def delete_courier():
    def _delete(credentials: Credentials):
        with allure.step("Запрос авторизация зареганного курьера."):
            login_response = requests.post(Urls.BASE_URL + Urls.LOGIN_PATH, credentials.toLoginMap())
        courier_id = login_response.json()['id']
        with allure.step("Запрос на удаление зарегистрированного курьера."):
            delete_response = requests.delete(Urls.BASE_URL + Urls.DELETE_PATH + str(courier_id))
        return delete_response.status_code == 200
    return _delete

import allure
import pytest
import requests

from utils.constants import SignInErrorsText, Urls
from utils.credentials import Credentials

class TestSignInCourier:
    @allure.feature('Функциональность авторизации курьера.')
    @allure.title('Проверка успешной авторизации курьера.')
    def test_sign_in_courier(self, registered_credentials: Credentials):
        url = Urls.BASE_URL + Urls.LOGIN_PATH
        with allure.step("Запрос авторизации курьера."):
            response = requests.post(url, registered_credentials.toLoginMap())
        assert response.status_code == 200 and response.json()['id'] is not None

    @allure.feature('Функциональность авторизации курьера.')
    @allure.title('Проверка ошибки авторизации курьера.')
    @allure.testcase('Авторизация с неправильным паролем или логином.')
    @pytest.mark.parametrize('data', [
        {
            "login": Credentials.registered_user().login,
            "password": Credentials.registered_user().password + 'wrong',
        },
        {
            "login": Credentials.registered_user().login + 'wrong',
            "password": Credentials.registered_user().password,
        }
    ])
    def test_error_sign_in_incorrect_data(self, data):
        url = Urls.BASE_URL + Urls.LOGIN_PATH
        with allure.step("Запрос авторизации курьера с неверными данными."):
            response = requests.post(url, data)
        assert response.status_code == 404 and SignInErrorsText.NOT_FOUND in response.json()['message']

    @allure.feature('Функциональность авторизации курьера.')
    @allure.title('Проверка ошибки авторизации курьера.')
    @allure.testcase('Авторизация без пароля или логина.')
    @pytest.mark.parametrize('data', [
        {
            "login": Credentials.registered_user().login,
            "password": "",
        },
        {
            "login": "",
            "password": Credentials.registered_user().password,
        }
    ])
    def test_error_sign_in_without_data(self, data):
        url = Urls.BASE_URL + Urls.LOGIN_PATH
        with allure.step("Запрос авторизации курьера с отсутствием данных."):
            response = requests.post(url, data)
        assert response.status_code == 400 and SignInErrorsText.BAD_REQUEST in response.json()['message']

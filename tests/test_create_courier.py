import allure
import requests

from utils.constants import RegisterErrorsText, Urls
from utils.credentials import Credentials

class TestCreateCourier:
    @allure.feature('Функциональность создания курьера.')
    @allure.title('Проверка успешной регистрации курьера.')
    def test_create_courier(self, credentials: Credentials):
        url = Urls.BASE_URL + Urls.CREATE_PATH
        response = requests.post(url, credentials.toRegisterMap())
        assert response.status_code == 201 and response.json()['ok'] == True

    @allure.feature('Функциональность создания курьера.')
    @allure.title('Проверка ошибки регистрации зарегистрированного курьера.')
    def test_error_create_registered_courier(self, credentials: Credentials):
        url = Urls.BASE_URL + Urls.CREATE_PATH
        requests.post(url, credentials.toRegisterMap())
        response = requests.post(url, credentials.toRegisterMap())
        assert response.status_code == 409 and RegisterErrorsText.BAD_REQUEST in response.json()['message']

    @allure.feature('Функциональность создания курьера.')
    @allure.title('Проверка ошибки регистрации курьера при неполных данных.')
    def test_error_create_incorrect_credentials(self, credentials: Credentials):
        url = Urls.BASE_URL + Urls.CREATE_PATH
        response = requests.post(url, credentials.toIncorrectRegisterMap())
        assert response.status_code == 400 and RegisterErrorsText.CONFLICT in response.json()['message']

    @allure.feature('Функциональность создания курьера.')
    @allure.title('Проверка успешности удаления зарегистрированного курьера.')
    def test_delete_registered_courier(self, credentials: Credentials):
        requests.post(Urls.BASE_URL + Urls.CREATE_PATH, credentials.toRegisterMap())
        login_response = requests.post(Urls.BASE_URL + Urls.LOGIN_PATH, credentials.toLoginMap())
        courier_id = login_response.json()['id']
        delete_response = requests.delete(Urls.BASE_URL + Urls.DELETE_PATH + str(courier_id))
        assert delete_response.status_code == 200 and delete_response.json()['ok'] == True

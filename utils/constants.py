class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_PATH = '/api/v1/courier'
    LOGIN_PATH = '/api/v1/courier/login'
    DELETE_PATH = '/api/v1/courier/'
    CREATE_ORDER_PATH = '/api/v1/orders'

class RegisterErrorsText:
    BAD_REQUEST = "Этот логин уже используется"
    CONFLICT = "Недостаточно данных для создания учетной записи"

class SignInErrorsText:
    NOT_FOUND = "Учетная запись не найдена"
    BAD_REQUEST = "Недостаточно данных для входа"

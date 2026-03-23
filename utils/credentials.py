from faker import Faker

class Credentials:
    def __init__(self, login, password, first_name):
        self.login = login
        self.password = password
        self.first_name = first_name

    def toRegisterMap(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }
    
    def toLoginMap(self):
        return {
            "login": self.login,
            "password": self.password
        }
    
    def toIncorrectRegisterMap(self):
        return {
            "login": self.login,
            "firstName": self.first_name
        }

    @staticmethod
    def registered_user():
        return Credentials('arinaTestCourier', 'testpass12', 'Arina')

class CredentialsGenerator:
    @staticmethod
    def generate():
        faker = Faker()
        return Credentials(faker.user_name(), faker.password(), faker.first_name())

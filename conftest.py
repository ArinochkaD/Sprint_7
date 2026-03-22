import sys
import os

import pytest

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

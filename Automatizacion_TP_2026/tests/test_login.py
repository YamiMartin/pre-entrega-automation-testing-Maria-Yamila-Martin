from pages.login_page import LoginPage
from data.users import USERS
from utils.helpers import load_user_csv, load_user_json
import pytest
from faker import Faker

load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")
fake = Faker()

@pytest.mark.parametrize("username, password", load_csv)
@pytest.mark.parametrize("username, password", load_json)
def test_login( driver, username, password):

    login_page =LoginPage(driver)

    login_page.openPage()
    login_page.login(username, password)

@pytest.mark.parametrize("i", range(5)) #aca digo cantidad de usuarios a generar
def test_login_ususario_invalido(driver, i):
    login_page =LoginPage(driver)

    fake_username = fake.user_name()
    fake_password = fake.password()

    login_page.openPage()
    login_page.login(fake_username, fake_password)

    assert "Epic sadface" in login_page.obtener_error()
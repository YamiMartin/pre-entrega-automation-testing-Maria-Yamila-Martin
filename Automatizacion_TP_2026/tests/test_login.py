from pages.login_page import LoginPage
from data.users import USERS
import pytest

@pytest.mark.parametrize("username, password", USERS)
def test_login( driver, username, password):

    login_page =LoginPage(driver)

    login_page.open()
    login_page.login("username, password")
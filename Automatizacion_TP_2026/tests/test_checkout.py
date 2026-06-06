from pages.login_page import LoginPage
from data.users import USERS
import pytest
from pages.checkout_page import CheckoutPage
from data.checkout_data import usuarios_checkout
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import load_user_csv, load_user_json

#load_csv = load_user_csv("data/users.csv")
#load_json = load_user_json(r"C:\Users\Yamila\Desktop\TESTER PYTHON\Automatizacion_TP_2026\data\users.json")


@pytest.mark.parametrize("username, password", USERS)
#@pytest.mark.parametrize("checkout_data", usuarios_checkout)

def test_checkout(driver, username, password):
    login_page = LoginPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.openPage()
    login_page.login(username, password)

    checkout_page.agregar_producto()
    checkout_page.ir_al_carrito()
    checkout_page.iniciar_carrito()
    
    assert "checkout-step-one.html" in driver.current_url

    checkout_page.completar_formulario()
    time.sleep(1)

    checkout_page.continuar()
    checkout_page.finish()
    # Validamos que el mensaje final sea el correcto
    assert "Thank you for your order!" in checkout_page.msj_exito()

    
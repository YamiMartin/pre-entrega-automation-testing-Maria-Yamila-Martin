from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
import time


fake = Faker()

class CheckoutPage:

    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID , "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_SUCCESS= (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def agregar_producto(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def ir_al_carrito(self):
        self.driver.find_element(*self.CART_BUTTON).click()

    def iniciar_carrito(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def completar_formulario(self):

        first_name = fake.first_name()
        last_name = fake.last_name()
        postal_code = fake.postcode()

       # 1. Esperamos que el campo sea visible primero para asegurar que la página asentó
        txt_first_name = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        txt_first_name.click() # Hacemos clic para asegurarnos de que tiene el foco activo
        txt_first_name.clear()
        txt_first_name.send_keys(first_name)
        time.sleep(0.5)
        
        # 2. El Apellido ya no tendrá problemas porque el formulario ya está asentado
        txt_last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        txt_last_name.click() # Hacemos clic para asegurarnos de que tiene el foco activo
        txt_last_name.clear()
        txt_last_name.send_keys(last_name)
        time.sleep(0.5)
        
        # 3. Lo mismo para el Código Postal
        txt_postal_code = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE))
        txt_postal_code.click() # Hacemos clic para asegurarnos de que tiene el foco activo
        txt_postal_code.clear()
        txt_postal_code.send_keys(postal_code)
        time.sleep(0.5)

    def continuar(self):
        # 1. Esperamos a que el botón sea visible y clickeable
        btn_continuar = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        
        # 2. Hacemos el click usando JavaScript para asegurar que la acción impacte en el navegador
        self.driver.execute_script("arguments[0].click();", btn_continuar)

        # 3. Le damos el margen de 7 segundos para reaccionar
        wait_cambio = WebDriverWait(self.driver, 7)
        try:
            # Esperamos a que la URL cambie al paso dos
            wait_cambio.until(EC.url_contains("checkout-step-two.html"))
        except TimeoutException:
            # 4. Si tira timeout, revisamos si apareció un cartel de error real
            error_elements = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='error']")
            if error_elements and error_elements[0].is_displayed():
                raise AssertionError(f"Error de validación en el formulario de Swag Labs: {error_elements[0].text}")
            
            # Si no hay cartel de error, nos aseguramos de reportar dónde quedó atrapado
            raise AssertionError(f"La página no navegó al paso 2. URL actual: {self.driver.current_url}")

    def finish(self):
       # 1. Esperamos a que el botón de finalizar sea clickeable
        btn_finish = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH)
        )
        # 2. Forzamos el click con JavaScript para asegurar la transición de pantalla
        self.driver.execute_script("arguments[0].click();", btn_finish)

    def msj_exito(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_SUCCESS)).text
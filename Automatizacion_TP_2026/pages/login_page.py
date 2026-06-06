from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:

    URL= "https://www.saucedemo.com/" #variable constante interna
    _USERNAME = (By.ID, "user-name")
    _PASSWORD = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID , "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    #constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) #establezco el tiempo de espera 

    def openPage(self):
        self.driver.get(self.URL) #ingresa a la URL

    #recibe el login-driver, aplico username y password e ingreso
    def login(self, username, password):
        
        #Evalua si hay presencia del elemento
        self.wait.until(
            EC.presence_of_element_located((self._USERNAME)) #aca no desempaqueto xq ya le llega la tupla
        ).send_keys(username)

        #En esta no evalua y ejecuta directamente, ambas validas, la de arriba mas profesional
        self.driver.find_element(*self._PASSWORD).send_keys(password) #con el * desempaqueto para que le llegue la tupla a python
        self.driver.find_element(*self._LOGIN_BUTTON).click()

    def obtener_error(self):
        return self.dirver.find_element(*self._ERROR_MESSAGE).text
    
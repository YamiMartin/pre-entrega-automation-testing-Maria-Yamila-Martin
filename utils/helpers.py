from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Estoy instalando la version compatible con mi navegador
def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    return driver

#recibe el login-driver, aplico username y password e ingreso
def login(driver, username, password):

    wait = WebDriverWait(driver, 10) #establezco el tiempo de espera 
    
    driver.get("https://www.saucedemo.com/") #ingresa a la url
    
    #Evalua si hay presencia del elemento
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)

    #En esta no evalua y ejecuta directamente, ambas validas, la de arriba mas profesional
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID , "login-button").click()

def obtener_precio_primer_producto(driver):
    return driver.find_element(By.CLASS_NAME, "inventory_item_price").text    

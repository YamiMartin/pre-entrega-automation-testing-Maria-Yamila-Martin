from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json

#Estoy instalando la version compatible con mi navegador
def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    return driver

def obtener_precio_primer_producto(driver):
    return driver.find_element(By.CLASS_NAME, "inventory_item_price").text    

def load_user_csv(path, newline=""):
    users = [] #lista de tuplas xq parametrizes recibe eso

    with open(path) as file:
        reader = csv.DictReader(file) #almacena diccionario que python puede interpretar
        for row in reader:
            if row["username"] and row["password"]: #me aseguro que no este vacio el dato
                users.append((row["username"], row["password"])) #recorro la lista y lo convierto a tuplas
    return users

def load_user_json (path):
    with open(path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return [(user["username"], user["password"]) for user in data]
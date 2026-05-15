from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#hago la prueba de ingresa a pag con usuario y contraseña, llego a inventario
def test_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url

    #Valido que el titulo diga eso "Products"
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"


def test_catalogo(driver):
    login(driver, "standard_user", "secret_sauce") #inicio sesion
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products" #busco que el titulo coincida

    #validar productos
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test ='inventory-item']")

    assert len(productos) > 0 # que en listado haya mas de 1 producto

    #veo el primer producto por el titulo
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name" ).text
    assert nombre == "Sauce Labs Backpack"

    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()

    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    assert len(productos) > 0 
    
    # Nombre y Precio
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Producto: {nombre} - Precio: {precio}") 
    assert "$" in precio

def test_agregar_productos_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)

    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    #agregar producto
    bnt_add= wait.until( # guardo todos los elementos clickeables que contengan add to cart
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
    )
    bnt_add.click()

    #valido contador de producto agregado en pantalla catalogo
    # Esperamos a que el badge aparezca en el DOM
    badge = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )  

    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    #validar producto agregado en carrito
    producto_dentro_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_dentro_carrito == nombre_producto

    
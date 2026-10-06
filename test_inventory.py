import pytest
# test_inventory.py
# QA el login en Sauce Demo y valida la URL y el título.
# https://github.com/jdmdtg/pre-entrega-automation-testing-jose-gilberto-medina.git|1a el título 'Products' y muestra el primer producto (nombre y precio).

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    
    try:
       # Abrir la pantalla de login
        driver.get("https://www.saucedemo.com")
    
        # Completar usuario y contraseña
        usuario = driver.find_element(By.ID, "user-name").send_keys("standard_user")
        contraseña = driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #  Enviar formulario
        boton = driver.find_element(By.CSS_SELECTOR, 'input[id="login-button"]').click() # type="submit"
        # Verificar URL = a /inventory.html
        assert "/inventory.html" in driver.current_url, "No se pudo redirigir al inventario."
    
        # — Verificar que existe el título —
        assert driver.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs", "Título No Encontrado"
            
        # — Verificar que existe la etiqueta producto —
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "Etiqueta Producto No Encontrada"
              

        # Verificar que exista al menos un producto
        products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        assert len(products) > 0, "No se encontraron productos"

        #Capturar nombre y precio del primer producto
        first_name  = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        first_price = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_price").text
        print(f"Primer producto → {first_name} – {first_price}")

        print("Evaluación Finalizada: Login Exitoso y validación de URL y Título correctamente.")
        
    finally:
        driver.quit()
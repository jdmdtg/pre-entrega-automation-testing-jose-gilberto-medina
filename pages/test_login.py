import pytest
import time
# test_login.py
# QA el login en Sauce Demo y valida la URL y el título.
# https://github.com/jdmdtg/pre-entrega-automation-testing-jose-gilberto-medina.git

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_exitoso():   
    # Crear el driver (Chrome por defecto)
    driver = webdriver.Chrome()
  
    try:
        # Abrir la página de login
        driver.get("https://www.saucedemo.com")

        # Completar identificar usuario, contraseña y completar el formulario de login
        usuario = driver.find_element(By.ID, "user-name")
        contraseña = driver.find_element(By.ID, "password")
        boton = driver.find_element(By.CSS_SELECTOR, 'input[id="login-button"]')

        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton.click()
        
        # Espera explícita para todos los find_element
        time.sleep(2)
    
        # Verificar URL = a /inventory.html
        assert "/inventory.html" in driver.current_url, "No se pudo redirigir al inventario."

        # — Verificar que existe el título Swag Labs —
        assert driver.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs", "Título No Encontrado"
        
        # — Verificar que existe la etiqueta products —
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products", "Etiqueta Producto No Encontrada"
        
        print("Evaluación Finalizada: Login Exitoso y validación de URL, Etiqueta Producto, Swag Labs completada correctamente.")
        
    finally:
        # Cerrar el navegador
        driver.quit()
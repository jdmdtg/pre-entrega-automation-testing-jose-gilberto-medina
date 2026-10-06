import pytest
# test_login.py
# QA el login en Sauce Demo y valida la URL y el título.
# https://github.com/jdmdtg/pre-entrega-automation-testing-jose-gilberto-medina.git

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():   
    # Crear el driver (Chrome por defecto)
    driver = webdriver.Chrome()
    # Espera implícita para todos los find_element
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
        
        print("Evaluación Finalizada: Login Exitoso y validación de URL y Título completada correctamente.")
    finally:
        # Cerrar el navegador
        driver.quit()
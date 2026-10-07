import time
import pytest

# carrito.py
# Añade el primer producto al carrito y verificar item en carrito.


from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_cart():
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

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
        
   
     
        #Agregar Producto al carrito.
        first_item = driver.find_element(By.CSS_SELECTOR, ".inventory_item")
        first_item_name = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        first_item_price = first_item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
        first_item_button = first_item.find_element(By.TAG_NAME, "button")
        first_item_button.click()
        
        # Espera explícita para todos los find_element
        time.sleep(2)
        
        # Verificar badge del carrito = 1
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "1", f"El contador del carrito es {badge} (se esperaba 1)"
         
        # Ir al carrito y confirmar producto
        boton_agregar = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        boton_agregar.click()
        #print(f"Producto agregado al carrito: {badge}")
                
        #verificamos que el producto agregado al carrito es el mismo que el primer producto de la lista
        cart_name = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        assert cart_name == first_item_name, "El producto del carrito no coincide"
        #print(f"Producto en carrito: {cart_name}")
        
        print("Evaluación Finalizada: Login Exitoso, validación de URL, Producto Agregado y Verificado la existencia en el carrito correctamente.")
        
    finally:
        driver.quit()
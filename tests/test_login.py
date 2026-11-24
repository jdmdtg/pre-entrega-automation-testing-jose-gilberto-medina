from pages.login_page import LoginPage
import pytest
from utils.reader import read_login_csv
from utils.logger import logger

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.flaky(reruns=2,reruns_delay=5)
@pytest.mark.parametrize(
        "data",read_login_csv())
def test_login(driver,data):
     # Crear el driver (Chrome por defecto)
    driver = webdriver.Chrome()
    try:
        logger.info("Iniciando prueba de login")
        login_page = LoginPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina Abierta.")

        login_page.login(data["usuario"],data["password"])
        logger.info("Ingreso de credenciales sin problemas")

        if (data["tipo_usuario"] == "True"):
            assert "/inventory.html" in driver.current_url
            logger.info("Login exitoso")
        elif data["tipo_usuario"] == "False":
            error = login_page.obtener_mensaje_error()
            assert "Epic sad" in error
            assert "Epic sadface" in error
            logger.info("Prueba de mensaje de error valida")          
    except Exception:
        logger.exception("Error durante la prueba de login")
        raise
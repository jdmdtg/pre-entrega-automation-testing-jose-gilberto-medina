import pytest
from selenium import webdriver

import pytest_html
import pathlib
import base64

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)


    yield driver

    driver.quit()
    
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return { "x-api-key": "pub_1af9b8cce1ebbd4f3f8145e4a4a0cf4e03ade473631f3ef2fb05f8d6f767e62d"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        carpeta = pathlib.Path("reports/screenshots")
        carpeta.mkdir(parents=True,exist_ok=True)
        archivo = carpeta / f"{item.name}.png"
        if driver is not None:
            driver.save_screenshot(str(archivo))

            imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")
            report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
        ]
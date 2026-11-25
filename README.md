# Entrega Final - Automatización de Testing

Este proyecto implementa una automatización de pruebas para el sitio **SauceDemo**, utilizando **Selenium WebDriver** y **Python**.

## 🎯 Propósito del Proyecto

El objetivo es automatizar los siguientes flujos en la Página SauceDemo:

- Navegar a la página de login de saucedemo.com.
- Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce").
- Validar login exitoso verificando que se haya  redirigido a la página de inventario.
- Verificar que el título de la página de inventario sea correcto.
- Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno).
- Validar que elementos importantes de la interfaz estén presentes (Etiqueta Products, Titulo).
- Navegar al carrito de compras.
- Añadir un producto al carrito haciendo clic en el botón correspondiente.
- Verificar que el contador del carrito se incremente correctamente.
- Comprobar que el producto añadido aparezca correctamente en el carrito
- Cierre de sesión.

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Pytest**: Framework de testing para estructurar y ejecutar pruebas.
- **Selenium WebDriver**: Para la automatización de la interfaz web.
- **Git/GitHub**: Para control de versiones y compartir el código.
- **requests**: Para el manejo de API.

## 📁 Estructura del Proyecto

pre-entrega-qa-a-tests


├──   data
		├── login.csv
		├── products.json

├──  features		
	├──environment.py
	├──login.features
	├── steps
		├──login_steps.py

├──	logs
	├── *.log

├──  pages
	├── cart_page.py
	├── inventory_page.py
	├── login_page.py

├──  reports
	├──reporte.html
	├──reporte_cart.html
	├──reporte_inventory.html
	├──reporte_login.html
	├──ui_api_reporte.html
	├── screenshots
		├── test_inventory.png
		├── test_login[data1].png

├── tests
	├── test_pai.py
	├── test_cart.py
	├── test_inventory.py
	├── test_login.py

├── utils
	├── logger.py
	├── reader.py
├── venv
├── README.md
├──conftest.py
├──pitest.ini
      
## ⚙️ Instalación de Dependencias

1. Asegúrate de tener Python 3.7 o superior instalado.
2. Instala las dependencias necesarias:
   * pip install pytest.
   * pip install selenium.
   * pip install pytest-html.
   * python -m venv venv.
   * pip install pytest-check
   * pip install pythes_html
   * pip install pytest-rerunfailures
   * pip install requests
   * pip install fake
   

**Descarga el WebDriver correspondiente a tu navegador:**

ChromeDriver


**Para verificar versión de Selenium, escribe en consola:.**

pip show selenium

▶️ Ejecución de las Pruebas:
- Para ejecutar todas las pruebas en un solo proceso escribe: pytest tests/ .(Verificar que la ruta este correcta para evitar errores.)
- Para ejecutar archivo por archivo, escribe pytest tests/ seguido el nombre del arhivo.py.

***¿Cómo ejecutar las pruebas?**

- Para todas las pruebas simultaneas, En la consola Escribir: pytest tests\ -v
- Para las pruebas individuales: En la consola escribir: 
	pytest tests\test_login.py 
	pytest tests\test_apy.py
	pytest tests\test_cart.py
	pytest tests\test_inventory.py


✅ Funcionalidades Implementadas

1. Automatización de Login
   Caso de éxito con credenciales válidas.
   Dos casos fallidos con credenciales invalidos.

3. Verificación del Catálogo
   Comprobación del título de la página.

4. Verificación de presencia de productos.

5. Validación de elementos de la interfaz.

6. Navegar al carrito.

7. Interacción con el Carrito.
   Añadir producto al carrito.

8. Comprobar que el producto añadido aparezca correctamente.

9. Automatización de Pruebas API Publica Nombre de la API: https://reqres.in/api
    - Uso del método GET para obtener usuario.
    - Uso del metodos POTS, para crear un usuario.  
    - Uso del método DELETE, para eliminar un usuario de la API.
    
*** ¿Cómo analizar los reportes de las pruebas?**

- Resumen General (Summary):

*Conteo de estados:* Verifica la proporción entre pruebas aprobadas (Passed), fallidas (Failed).

*Tiempo de ejecución:* Revisa la duración total de la suite para detectar cuellos de botella o esperas innecesarias en las pruebas de UI o API.

*Capturas:* Inspecciona la captura de pantalla adjunta en el detalle del test fallido para confirmar visualmente si el error se debió a un cambio en la interfaz, un mensaje de error inesperado o un problema de carga.


👤 Autor
José Gilberto Medina

Fecha de Presentación. 07/10/2026

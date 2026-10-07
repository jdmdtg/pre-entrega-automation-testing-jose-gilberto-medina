# Pre-entrega - Automatización de Testing

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

## 📁 Estructura del Proyecto

pre-entrega-qa-a-tests

      ├── test_login.py
      ├── test_inventory.py
      ├── test_cart.py
      ├── reports
            ├── reporte_cart.html
            ├── reporte_inventory.html
            ├── reporte_login.html
      
## ⚙️ Instalación de Dependencias

1. Asegúrate de tener Python 3.7 o superior instalado.
2. Instala las dependencias necesarias:
   * pip install pytest.
   * pip install selenium.
   * pip install pytest-html.
   * python -m venv venv.
   

**Descarga el WebDriver correspondiente a tu navegador:**

ChromeDriver


**Para verificar versión de Selenium, escribe en consola:.**

pip show selenium

▶️ Ejecución de las Pruebas:
- Para ejecutar todas las pruebas en un solo proceso escribe: pytest.(Verificar que la ruta este correcta para evitar errores.)
- Para ejecutar archivo por archivo, escribe pytest seguido el nombre del arhivo.py.


✅ Funcionalidades Implementadas

1. Automatización de Login
   Caso de éxito con credenciales válidas.

2. Verificación del Catálogo
   Comprobación del título de la página.

3. Verificación de presencia de productos.

4. Validación de elementos de la interfaz.

5. Navegar al carrito.

6. Interacción con el Carrito.
   Añadir producto al carrito.

7. Comprobar que el producto añadido aparezca correctamente.


👤 Autor
José Gilberto Medina

Fecha de Presentación. 07/10/2026
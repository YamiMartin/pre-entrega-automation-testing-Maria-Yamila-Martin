### Automatización de Pruebas con Python y Selenium - SauceDemo

Este proyecto forma parte de mi formación en **Automation QA** y consiste en una suite de pruebas automatizadas para la plataforma [SauceDemo](https://www.saucedemo.com/). El objetivo es validar los flujos críticos de la aplicación, como el inicio de sesión y la gestión del carrito de compras, asegurando la estabilidad del software.

## 🚀 Funcionalidades Automatizadas

*   **Autenticación de Usuarios:** Validación de acceso con credenciales estándar.
*   **Gestión de Inventario:** Selección de productos y verificación de nombres de artículos.
*   **Carrito de Compras:** 
    *   Adición de productos al carrito.
    *   Validación dinámica del contador (badge) del carrito.
    *   Sincronización de datos entre la vista de catálogo y la vista de carrito.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** [Python 3.14+](https://www.python.org/)
*   **Framework de Pruebas:** [Pytest](https://docs.pytest.org/)
*   **Automatización Web:** [Selenium WebDriver](https://www.selenium.dev/)
*   **Gestión de Drivers:** `webdriver-manager` (para configuración automática de ChromeDriver).
*   **Reportes:** `pytest-html` para la generación de reportes de ejecución en formato HTML.

## 📈 Buenas Prácticas Aplicadas

*   **Explicit Waits:** Uso de `WebDriverWait` y `ExpectedConditions` para manejar la asincronía del navegador y evitar "flaky tests".
*   **Modularización:** Organización de funciones comunes (como el login) para promover la reutilización de código.
*   **Validaciones Robustas:** Comparación de tipos de datos y extracción de texto de elementos (WebElements) para aserciones precisas.

## 📋 Requisitos Previos

Asegúrate de tener instalado:
- Python 3.x
- Google Chrome

## 🔧 Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/YamiMartin/pre-entrega-automation-testing-Maria-Yamila-Martin/tree/main/Automatizacion_TP_2026]
   cd Automatizacion_TP_2026
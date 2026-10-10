from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.evidence_builder import collector
from utils.screenshot_manager import take_screenshot
from config.config import Config

def test_acceso_inventory_sin_login(driver):
    """Intentar entrar a /inventory.html sin sesión debe redirigir al login."""
    collector.start_test("Acceso a Inventory sin Login")
    try:
        inventory = InventoryPage(driver)
        login = LoginPage(driver)

        # Navegar directo al recurso protegido (sin autenticarse)
        driver.get(Config.INVENTORY_URL)
        collector.add_step(f"Navegar directo a {Config.INVENTORY_URL}", "PASS")

        # La app debe redirigir a la pagina de login
        assert login.is_element_visible(LoginPage.LOGIN_BUTTON), "No redirigio al login: el recurso protegido quedo accesible"
        collector.add_step("Redirigido al login", "PASS", take_screenshot(driver, wait=1))

        # Y NO debe existir la vista de productos
        assert "/inventory.html" not in driver.current_url, "La URL sigue siendo inventory.html sin autenticacion"
        collector.add_step("Contenido de inventory no accesible", "PASS")

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise
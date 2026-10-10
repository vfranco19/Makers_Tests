from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object de la pagina principal."""

    # ── Localizadores ─────────────────────────────────────────────────
    LOGO = (By.XPATH, "//div[@class='app_logo']")
    MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")

    # ── Acciones ──────────────────────────────────────────────────────

    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO)

    def logout(self):
        """Hace logout desde el menu lateral."""
        self.click(self.MENU_BUTTON)
        self.click((By.XPATH, "//a[@id='logout_sidebar_link']"))

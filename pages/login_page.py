from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object de la pagina de login."""

    # ── Localizadores ─────────────────────────────────────────────────
    TITLE = (By.XPATH, "//div[@class='login_logo']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-test='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-test='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@data-test='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")
    CREDENTIALS_CONTAINER = (By.XPATH, "//div[@class='login_credentials_wrap-inner']")

    # ── Acciones ──────────────────────────────────────────────────────

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_title_visible(self):
        return self.is_element_visible(self.TITLE)

    def is_error_visible(self):
        return self.is_element_visible(self.ERROR_MESSAGE)

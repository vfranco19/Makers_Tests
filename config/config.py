class Config:
    """Configuracion centralizada del proyecto."""

    BASE_URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    # Tiempo de espera explicito para elementos (segundos)
    TIMEOUT = 10

    # Credenciales de testing
    TEST_USER_EMAIL = "standard_user"   
    TEST_USER_PASSWORD = "secret_sauce"

    BLOCKED_USER_EMAIL = "locked_out_user"
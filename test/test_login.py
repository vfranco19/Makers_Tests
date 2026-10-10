from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.evidence_builder import collector
from utils.screenshot_manager import take_screenshot
from config.config import Config

def test_login_exitoso(driver):
    """Login con credenciales correctas."""
    collector.start_test("Login - Credenciales Correctas")
    try:
        inventory = InventoryPage(driver)
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        # Realizar login
        collector.add_step(f"Credenciales username: '{Config.TEST_USER_EMAIL}' password: '{Config.TEST_USER_PASSWORD}'", "PASS")
        login.login(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)

        # Validar ingreso exitoso a la pagina de inventario
        assert inventory.is_logo_visible(), "No se cargo la pagina de inventario"
        collector.add_step("Login exitoso", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise

def test_login_password_invalido(driver):
    """Login con password incorrecto debe mostrar error."""
    collector.start_test("Login - Password Invalido")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.add_step(f"Credenciales username: '{Config.TEST_USER_EMAIL}' password: 'wrongpassword'", "PASS")
        login.login(Config.TEST_USER_EMAIL, "wrongpassword")

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise

def test_login_credenciales_vacias(driver):
    """Login con credenciales vacias debe mostrar error."""
    collector.start_test("Login - Credenciales Vacias")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.add_step(f"Credenciales username: '' password: ''", "PASS")
        login.login("", "")

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")        
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise    

def test_login_username_vacio(driver):
    """Login con username vacio debe mostrar error."""
    collector.start_test("Login - Username Vacio")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.add_step(f"Credenciales username: '' password: '{Config.TEST_USER_PASSWORD}'", "PASS")
        login.login("", Config.TEST_USER_PASSWORD)

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise    

def test_login_password_vacio(driver):
    """Login con password vacio debe mostrar error."""
    collector.start_test("Login - Password Vacio")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.add_step(f"Credenciales username: '{Config.TEST_USER_EMAIL}' password: ''", "PASS")
        login.login(Config.TEST_USER_EMAIL, "")

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise        

def test_login_usuario_inexistente(driver):
    """Login con usuario inexistente debe mostrar error."""
    collector.start_test("Login - Usuario Inexistente")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.add_step(f"Credenciales username: 'fake@email.com' password: 'wrongpassword'", "PASS")
        login.login("fake@email.com", "wrongpassword")

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")        
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise

def test_login_usuario_bloqueado(driver):
    """Login con usuario bloqueado debe mostrar error."""
    collector.start_test("Login - Usuario Bloqueado")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.add_step(f"Credenciales username: '{Config.BLOCKED_USER_EMAIL}' password: '{Config.TEST_USER_PASSWORD}'", "PASS")
        login.login(Config.BLOCKED_USER_EMAIL, Config.TEST_USER_PASSWORD)

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")        
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise

def test_login_con_espacios_en_blanco(driver):
    """Login con credenciales correctas mas espacios en blanco."""
    collector.start_test("Login - Credenciales Correctas con espacios en blanco")
    try:
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        # Realizar login
        collector.add_step(f"Credenciales username: '{Config.TEST_USER_EMAIL+ ' '}' password: '{Config.TEST_USER_PASSWORD+ ' '}' con espacios en blanco", "PASS")
        login.login(Config.TEST_USER_EMAIL+ " ", Config.TEST_USER_PASSWORD+ " ")

        assert login.is_error_visible(), "Deberia mostrar mensaje de error"
        error_msj = login.get_text(login.ERROR_MESSAGE)
        collector.add_step(f"Mensaje de error visible: {error_msj}", "PASS")        
        collector.add_step("Mensaje de error visible", "PASS", take_screenshot(driver, wait=1))

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise

def test_login_logout(driver):
    """Login con credenciales correctas y luego logout."""
    collector.start_test("Login - Credenciales Correctas y Logout")
    try:
        inventory = InventoryPage(driver)
        login = LoginPage(driver)

        # Verificar que estamos en la pagina de login
        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        # Realizar login
        collector.add_step(f"Credenciales username: '{Config.TEST_USER_EMAIL}' password: '{Config.TEST_USER_PASSWORD}'", "PASS")
        login.login(Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD)

        assert inventory.is_logo_visible(), "No se cargo la pagina de inventario"
        collector.add_step("Login exitoso", "PASS", take_screenshot(driver, wait=1))

        inventory.logout()

        assert login.is_title_visible(), "No se cargo la pagina de login"
        screenshot = take_screenshot(driver, wait=1)
        collector.add_step("Pagina de login visible", "PASS", screenshot)

        collector.end_test()

    except Exception as e:
        collector.add_step(str(e), "FAIL", take_screenshot(driver, wait=1))
        collector.end_test()
        raise
from datetime import datetime
from pathlib import Path
import shutil
import os
import time
from config.config import Config

SCREENSHOTS_DIR = "evidence/screenshots/"

def take_screenshot(driver, wait=None):
    """Toma un screenshot y retorna el nombre del archivo."""
    time.sleep(wait if wait is not None else Config.SCREENSHOT_WAIT)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    filename = datetime.now().strftime("imagen_%d_%m_%Y-%H_%M_%S.png")
    path = f"{SCREENSHOTS_DIR}{filename}"
    driver.save_screenshot(path)
    return filename


def limpiar_screenshots():
    """Elimina todos los screenshots anteriores."""
    carpeta = Path(SCREENSHOTS_DIR)
    if carpeta.exists():
        for item in carpeta.iterdir():
            if item.is_file():
                item.unlink()
            else:
                shutil.rmtree(item)

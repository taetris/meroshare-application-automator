import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils import take_screenshot

def go_to_apply_issue(driver, wait):
    print("➡️ Navigating to Apply for Issue...")
    my_asba = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'My ASBA')]")))
    driver.execute_script("arguments[0].click();", my_asba)
    time.sleep(1)

    apply_issue = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Apply for Issue')]")))
    driver.execute_script("arguments[0].click();", apply_issue)
    time.sleep(3)
    take_screenshot(driver, "apply_for_issue")

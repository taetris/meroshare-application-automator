import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils import take_screenshot

def login(driver, wait, dp_name, username, password):
    print("🌐 Opening MeroShare login page...")
    driver.get("https://meroshare.cdsc.com.np/")
    time.sleep(3)

    print(f"🔍 Selecting DP: {dp_name}")
    select2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.select2-selection")))
    select2.click()
    time.sleep(1)

    search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.select2-search__field")))
    search.send_keys(dp_name)
    time.sleep(2)

    option_xpath = f"//li[contains(text(),'{dp_name}')]"
    option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    option.click()

    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(3)

    # Check for login error
    try:
        error_msg = driver.find_element(By.CLASS_NAME, "error-message")
        if error_msg.is_displayed():
            take_screenshot(driver, "login_failed")
            raise Exception("🚫 Login failed: " + error_msg.text.strip())
    except:
        pass

    take_screenshot(driver, "logged_in")
    print("✅ Login successful.")

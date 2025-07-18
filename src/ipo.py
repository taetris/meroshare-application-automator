import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import take_screenshot

def list_open_ipos(driver, wait):
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "company-list")))
    ipo_blocks = driver.find_elements(By.CLASS_NAME, "company-list")

    open_ipos = []
    print("\n📢 Open IPOs:")
    for idx, block in enumerate(ipo_blocks, 1):
        try:
            name_span = block.find_element(By.CLASS_NAME, "company-name")
            name = name_span.text.strip()

            apply_button = block.find_element(By.CLASS_NAME, "btn-issue")
            if apply_button.is_displayed():
                open_ipos.append((idx, name, apply_button))
                print(f"{len(open_ipos)}. {name}")
        except:
            continue
    return open_ipos

def apply_to_ipo(driver, wait, apply_button, applied_kitta, crn, transaction_pin):
    print("📝 Opening apply form...")
    driver.execute_script("arguments[0].click();", apply_button)
    time.sleep(2)

    bank_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "selectBank")))
    bank_dropdown.click()
    time.sleep(1)
    bank_option = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='selectBank']/option[not(@value='')][1]")))
    bank_value = bank_option.get_attribute("value")
    driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", bank_dropdown, bank_value)
    time.sleep(2)

    account_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "accountNumber")))
    account_dropdown.click()
    time.sleep(1)
    account_option = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='accountNumber']/option[not(@value='')][1]")))
    acc_value = account_option.get_attribute("value")
    driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", account_dropdown, acc_value)
    time.sleep(2)

    qty_field = wait.until(EC.presence_of_element_located((By.ID, "appliedKitta")))
    qty_field.clear()
    qty_field.send_keys(str(applied_kitta))

    crn_field = wait.until(EC.presence_of_element_located((By.ID, "crnNumber")))
    crn_field.clear()
    crn_field.send_keys(crn)

    disclaimer = wait.until(EC.presence_of_element_located((By.ID, "disclaimer")))
    driver.execute_script("arguments[0].click();", disclaimer)
    time.sleep(1)

    proceed_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'Proceed') and not(@disabled)]")))
    driver.execute_script("arguments[0].click();", proceed_button)
    time.sleep(2)
    take_screenshot(driver, "after_proceed")

    print("🔒 Entering transaction PIN...")
    pin_field = wait.until(EC.presence_of_element_located((By.ID, "transactionPIN")))
    pin_field.clear()
    pin_field.send_keys(transaction_pin)

    apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Apply')]")))
    driver.execute_script("arguments[0].click();", apply_btn)

    try:
        toast = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "toast-message")))
        print("🎉 Success:", toast.text.strip())
    except:
        try:
            modal_error = driver.find_element(By.CLASS_NAME, "modal-body")
            if modal_error.is_displayed():
                print("⚠️ Modal error:", modal_error.text.strip())
        except:
            print("⚠️ Could not confirm success or error message.")

    take_screenshot(driver, "final_confirmation")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from utils import load_applicants_from_string
from login import login
from navigation import go_to_apply_issue
from ipo import list_open_ipos, apply_to_ipo

import time

from utils import init_screenshot_folder, take_screenshot

# Before processing applicants:
init_screenshot_folder()


chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080")

applicants = load_applicants_from_string(csv_data)

for i, applicant in enumerate(applicants, 1):
    driver = None
    wait = None
    try:
        print(f"\n Processing applicant {i}: {applicant['username']}")
        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 20)

        login(driver, wait, applicant['dp_name'], applicant['username'], applicant['password'])
        go_to_apply_issue(driver, wait)
        open_ipos = list_open_ipos(driver, wait)

        if not open_ipos:
            print(" No IPOs currently open.")
        else:
            print("\n Which IPO would you like to apply for?")
            for idx, (ipo_index, name, _) in enumerate(open_ipos, 1):
                print(f"{idx}. {name}")
            print("0.  Skip this applicant")

            while True:
                try:
                    choice = int(input("Enter the number of the IPO to apply for (or 0 to skip): "))
                    if 0 <= choice <= len(open_ipos):
                        break
                    else:
                        print(" Invalid choice. Please enter a number from the list.")
                except ValueError:
                    print(" Please enter a valid number.")

            if choice == 0:
                print(f" Skipping applicant {applicant['username']}.\n")
            else:
                apply_button = open_ipos[choice - 1][2]
                apply_to_ipo(driver, wait, apply_button, applicant['applied_kitta'], applicant['crn'], applicant['transaction_pin'])

    except Exception as e:
        print(f" Error for {applicant['username']}: {str(e)}")
        if driver:
            from utils import take_screenshot
            take_screenshot(driver, f"error_{applicant['username']}")

    finally:
        if driver:
            driver.quit()
        print("Moving to next applicant...\n")

print(" All applicants processed.")

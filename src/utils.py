import csv
import io
from PIL import Image
import IPython.display as display

def load_applicants_from_string(csv_string):
    applicants = []
    reader = csv.DictReader(io.StringIO(csv_string.strip()))
    for row in reader:
        applicants.append({
            'dp_name': row['dp_name'],
            'username': row['username'],
            'password': row['password'],
            'bank_name': row['bank_name'],
            'applied_kitta': int(row['applied_kitta']),
            'crn': row['crn'],
            'transaction_pin': row['transaction_pin'],
        })
    return applicants

def take_screenshot(driver, label="screen"):
    path = f"./screenshots/{label}.png"
    driver.save_screenshot(path)
    display.display(Image.open(path))

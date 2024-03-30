import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start background algorithm
class PhoneNumberGenerator():
    def __init__(self):
        self.country_prefixes = {'US': '+1', 'UK': '+44', 'FR': '+33', 'DK': '+45', 'IT': '+39'}
        self.country_digit_counts = {'US': 10, 'UK': 11, 'FR': 9, 'DK': 8, 'IT': 10}

    def generate_random_phone_number(self, country_code):
        prefix = self.country_prefixes.get(country_code, '+00')
        digits_count = self.country_digit_counts.get(country_code, 8 | 9 | 10)
        remaining_digits = digits_count - len(prefix)
        phone_number = prefix + ''.join(random.choices(string.digits, k=remaining_digits))
        return phone_number

def generate_random_name(existing_names):
    first_names = ['John', 'Alice', 'Michael', 'Emily', 'David', 'Sarah', "Jonas", "Luka", "Kamila", "Camilla", "Johan", "Frederik", "Frederikke", "Josef"]
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Lund', "Kjaer Jensen", "Modric", "Dirk", "Genzano", "Jensen"]
    true = True
    while true:
        new_name = random.choice(first_names) + ' ' + random.choice(last_names)
        if new_name not in existing_names:
            existing_names.add(new_name)
            return new_name

def generate_random_email(existing_emails, name):
    domains = ["gmail.com", "yahoo.com", "live.com", "hotmail.com", "apple.icloud.com"]
    true = True
    while true:
        username = ''.join(name.split()) + str(random.randint(1, 100))
        domain = random.choice(domains)
        email = f"{username}@{domain}"
        if email not in existing_emails:
            existing_emails.add(email)
            return email

def generate_random_contact(existing_names, existing_emails, generator, country_code):
    name = generate_random_name(existing_names)
    email = generate_random_email(existing_emails, name)
    phone = generator.generate_random_phone_number(country_code)
    return {'name': name, 'email': email, 'phone_number': phone}

def write_contacts_2_file(contacts):
    with open('contacts.txt', 'a') as file:
        for contact in contacts:
            file.write(f"Name: {contact['name']}, Email: {contact['email']}, Phone Number: {contact['phone_number']}\n")
# End background algorithm

# <-------------------------------------------- Start booking process on Website ---------------------------------------------> #
def booking (url, contact):
    by_css = By.CSS_SELECTOR
    by_ID = By.ID
    by_x_path = By.XPATH
    date_path = '//*[@id="sr-search-initial-comp"]/div/div/div/span[2]'
    day_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[6]' 
    # /html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[7]
    # Initial One: Day 15th - '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[6]'
    guest_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[3]/div/div/div/button[2]'
    time_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[4]/div/div/div/button[2]'
    search_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[5]/div/button'
    time1_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div/div[1]/div[1]/div[3]/button[6]'
    select_id = "sr-dining-additional-selection-first"
    surname_fill = '//*[@id="sr-last-name *"]'
    name_fill = '//*[@id="sr-first-name *"]'
    email_fill =  '//*[@id="sr-email-address *"]'
    flag_path = '//*[@id="sr-checkout-information"]/div[2]/form/div[3]/div/div/div[1]/div[1]/div/div[1]'
    country_code_path = '//*[@id="sr-checkout-information"]/div[2]/form/div[3]/div/div/div[1]/div[2]/ul/div[204]/div'
    phone_input = '//*[@id="sr-checkout-information"]/div[2]/form/div[3]/div/div/div[2]/div/input'

    browser = webdriver.Chrome()
    browser.get(url)
    date_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, date_path
            )
        )
    )
    date_button.click()
    time.sleep(5)
    day_date = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, day_path
            )
        )
    )
    day_date.click()
    time.sleep(5)
    guest_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, guest_path
            )
        )
    )
    guest_button.click()
    guest_button.click()
    time_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, time_path
            )
        )
    )
    time_button.click()
    time_button.click()
    time_button.click()
    search_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, search_path
            )
        )
    )
    search_button.click()
    time.sleep(5)
    time_btn_conf = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, time1_path
            )
        )
    )
    time_btn_conf.click()
    time.sleep(2)
    select_btn = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_ID, select_id
            )
        )
    )
    select_btn.click()
    time.sleep(5)
    fill_surname = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, surname_fill
            )
        )
    )
    fill_surname.send_keys(contact['name'].split[1])
    fill_name = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, name_fill
            )
        )
    )
    fill_name.send_keys(contact['name'].split[0])
    time.sleep(2)
    email_ = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, email_fill
            )
        )
    )
    email_.send_keys(contact['email'])
    time.sleep(2)
    flag = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, flag_path
            )
        )
    )
    flag.click()
    country_code = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, country_code_path
            )
        )
    )
    country_code.click()
    time.sleep(4)
    phone = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, phone_input
            )
        )
    )
    phone.send_keys(contact['phone_number'])

    # Uncomment lines(mainly): 194,195 & 196 below only when you are 100% sure of proceeding
    submit_btn = browser.find_element(by_x_path, '//*[@id="dining-widget-app"]/div/div/div[1]/div[6]/button').click()
    if submit_btn:
        print("Booking successful! Browser closing...")
    time.sleep(8)
    browser.delete_all_cookies()
    browser.quit()
# <--------------------------------------------------- End prankware -------------------------------------------------> #

# Main function that runs the whole script
def main():
    num_contacts = 5
    country_codes = ['US', 'UK', 'FR', 'IT', 'DK']  # Example country codes
    phone_number_generator = PhoneNumberGenerator()  # Instantiate the generator
    existing_names =  set()
    existing_emails = set() 
    
    # Generate contacts and write to file
    contacts = []
    for _ in range(num_contacts):
        selected_country_code = random.choice(country_codes)
        contact = generate_random_contact(existing_names, existing_emails, phone_number_generator, selected_country_code)
        contacts.append(contact)
    
    write_contacts_2_file(contacts)
    url = "https://www.sevenrooms.com/reservations/cafevictor"   # Your actual Booking website url

    #Perfom booking for each contact
    for contact in contacts:
        booking(url, contact)

# Calling "main()" function above-mentioned for executing script
if __name__ == "__main__":
    main()

# End of script
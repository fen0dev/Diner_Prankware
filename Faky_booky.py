import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

             
def booking (url, surname, name, email, tlf):
    by_css = By.CSS_SELECTOR
    by_ID = By.ID
    by_x_path = By.XPATH
    date_path = '//*[@id="sr-search-initial-comp"]/div/div/div/span[2]'
    day_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]'
    guest_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[3]/div/div/div/button[2]'
    time_path = '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[4]/div/div/div/button[2]'

    browser = webdriver.Chrome()
    browser.get(url)
    date_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, date_path
            )
        )
    )
    time.sleep(2)
    date_button.click()
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
    search_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div[5]/div/button'
            )
        )
    )
    search_button.click()
    time.sleep(5)
    time_btn_conf = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="dining-widget-app"]/div/div/div[1]/div[2]/div/div[1]/div[1]/div[3]/button[6]'
            )
        )
    )
    time_btn_conf.click()
    time.sleep(2)
    select_btn = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (
                by_ID, "sr-dining-additional-selection-first"
            )
        )
    )
    select_btn.click()
    time.sleep(5)
    fill_surname = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="sr-last-name *"]'
            )
        )
    )
    fill_surname.send_keys(surname)
    fill_name = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="sr-first-name *"]'
            )
        )
    )
    fill_name.send_keys(name)
    time.sleep(2)
    email_ = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="sr-email-address *"]'
            )
        )
    )
    email_.send_keys(email)
    time.sleep(2)
    flag = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="sr-checkout-information"]/div[2]/form/div[3]/div/div/div[1]/div[1]/div/div[1]'
            )
        )
    )
    flag.click()
    country_code = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="sr-checkout-information"]/div[2]/form/div[3]/div/div/div[1]/div[2]/ul/div[2]/div'
            )
        )
    )
    country_code.click()
    time.sleep(4)
    phone = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (
                by_x_path, '//*[@id="sr-checkout-information"]/div[2]/form/div[3]/div/div/div[2]/div/input'
            )
        )
    )
    phone.send_keys(tlf)
    submit_btn = browser.find_element(by_x_path, '//*[@id="dining-widget-app"]/div/div/div[1]/div[6]/button').click()
    if (submit_btn):
        print("Booking successful! Browser closing soon...")
    else:
        error = browser.get_issue_message()
        print("There was an error:", error)
    time.sleep(5)
    browser.delete_all_cookies()
    browser.quit()



    


if __name__ == '__main__':
    url = "https://www.sevenrooms.com/reservations/cafevictor/"
    surname = "Brown"
    name = "Alice"
    email = "alicebrown54@live.com"
    tlf = "02075629833"
    booking(url, surname, name, email, tlf)


              
              
            







import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By




class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        #close ad window
        gen=self.find_element(By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]') 
        gen.click()
        currency_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')    
        currency_element.click()

        #selected_currency_element = self.find_element(By.CSS_SELECTOR,f'button > div > div > span + div:contians("{currency}")')
        selected_currency_element=self.find_element(By.XPATH,f"//button/div/div/span/div[text()='{currency}']")
        #self.find_element(By.CSS_SELECTOR,'div:contains("JPY")^4')
        selected_currency_element.click()


    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

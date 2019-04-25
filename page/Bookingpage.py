from selenium.webdriver.common.by import By
from time import sleep
# from furl import furl

from page.Homepage import HomePage


class Bookflow(HomePage):
    '''订酒店流程'''
    def __init__(self,driver):
        self.driver = driver
        self.element_destination = By.XPATH, "/html/body/div[1]/div[10]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/textarea"
        self.element_london = By.XPATH, "/html/body/div[1]/div[10]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div/div/span/a[1]"
        self.element_book = By.CLASS_NAME, "dont-close-result"


    def book_room(self):
        '''选择一个酒店，订房间'''
        self.driver.find_element(*self.element_destination).click()
        sleep(2)
        self.driver.find_element(*self.element_london).click()
        self.driver.find_element(*self.element_book).click()
        self.driver.get_screenshot_as_file("../screenshot/ bookingpage.png")

    def verify_url(self):
        '''验证是否选中一个酒店'''
        currenturl = self.driver.current_url
        homepageurl = 'https://www.millenniumhotels.com/'
        print(currenturl)
        print(homepageurl)
        assert currenturl != homepageurl




from selenium.webdriver.common.by import By


class PropertyPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.link_hotels_xpath = '/html/body/div[1]/div[11]/div[2]/div[1]/ul/li[3]/a/span'
        self.link_hotel_name_xpath ='/html/body/div[1]/div[9]/div/div[3]/div/div[2]/div[6]/div[2]/a'   #'Grand Copthorne Waterfront' hotel
        self.link_room_section_text = 'Rooms'


    # def find_element_title(self):
    #     self.driver.find_element(self.text_page_title)


    def proceed_to_propertypage(self):
        '''Find ‘Hotels’ link then click'''
        self.link_hotels = self.driver.find_element_by_xpath(self.link_hotels_xpath)
        self.link_hotels.click()
        print('-------------------------'+self.driver.title+'--------------------')

        is_homepage_opened = "Millennium Hotels and Resorts" in self.driver.title
        assert is_homepage_opened

        # if is_homepage_opened == 'True':
        #     print('Home page property page is opened')
        # else:
        #     print('Failed open home page')


        '''Find specific hotel name then click'''
        self.link_hotel_name = self.driver.find_element_by_xpath(self.link_hotel_name_xpath)
        self.link_hotel_name.click()

        print('-------------------------'+self.driver.title+'-------------------------')
        is_hotelpage_opened = "Grand Copthorne Waterfront" in self.driver.title
        assert is_hotelpage_opened

        # if is_hotelpage_opened =='True':
        #     print('Hotel property page is opened')
        # else:
        #     print('Failed open hotel property page')

    def check_rooms_section(self):
        #
        self.link_room_section = self.driver.find_element_by_link_text(self.link_room_section_text)
        self.link_room_section.click()


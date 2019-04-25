import time
import unittest
from page.Homepage import HomePage
from driver.browser import chrome_browser
from ddt import ddt, data
from data.ExcelUtil_tool import ExcelUtil
import json
import requests

regions = ['Asia', 'Europe', 'MEA', 'New+Zealand', 'United+States']
hotels = []
logindata = ExcelUtil.readExcel('C:\millenniumhotels\data\email&password.xlsx','Sheet1')


@ddt
class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = chrome_browser()
        self.driver.get("https://www.millenniumhotels.com")
        self.home = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    # @data(*logindata)
    # def test_login_facebook(self,data):
    #     """测试facebook登录"""
    #     self.home.sign_in_facebook(data['face_email'],data['face_pass'])

    # def test_hotels_number(self):
    #     """测试酒店数"""
    #     for region in regions:
    #         url = "https://www.millenniumhotels.com/api/search/destinations?keywords=&regionName=%s" % region
    #         get_response = requests.get(url)
    #         if get_response.status_code == 200:
    #             result = json.loads(get_response.text)
    #             hotelMsgs = result.get('data').get('hotels')
    #             for hotelMsg in hotelMsgs:
    #                 hotels.append(hotelMsg.get('name'))
    #     print(len(hotels))
    #     assert len(hotels) == 125
    #
    # @data(*logindata)
    # def test_login_gmail(self,data):
    #     """测试gmail登录"""
    #     self.home.sign_in_google()
    #
    @data(*logindata)
    def test_login_linkedin(self,data):
        """linkedin登录"""
        try:
            self.home.sign_in_linkedin(data['link_acc'],data['link_pass'])
            self.current_url = self.driver.current_url
            self.assertEqual(self.current_url,"https://www.millenniumhotels.com/","跳转失败")

        except Exception as err:
            self.driver.get_screenshot_as_file("./screenshot/linkedin_err.png")
            raise

    if __name__ == '__main__':
        unittest.main()
#

# import unittest
# from ddt import ddt
# from driver.browser import chrome_browser
# from time import sleep
# from page.Homepage import HomePage
#
# @ddt
# class Test_Languages(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = chrome_browser()
#         cls.driver.get("https://www.millenniumhotels.com")
#         cls.home = HomePage(cls.driver, "ly", "pass")
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#
#     def test_select_arabic(self):
#         """阿拉伯语"""
#         try:
#             self.home.click_swictch_language()
#             self.home.switch_to_Arabic()
#         except Exception as err:
#             print(err)
#
#     def test_select_chinese(self):
#         """中文"""
#         self.home.click_swictch_language()
#         self.home.switch_to_chinese()
#     #
#     # def test_switch_spanish(self):
#     #     """西班牙语"""
#     #     self.home.click_swictch_language()
#     #     self.home.switch_to_spanish()
#     #
#     # def test_switch_franch(self):
#     #     """法语"""
#     #     self.home.click_swictch_language()
#     #     self.home.switch_to_franch()
#     #
#     # def test_switch_litalian(self):
#     #     """意大利语"""
#     #     self.home.click_swictch_language()
#     #     self.home.switch_to_litalian()
#     #
#     # def test_switch_chinese_traditional(self):
#     #     """繁体中文"""
#     #     self.home.click_swictch_language()
#     #     self.home.switch_to_chinese_traditional()
#     #
#     # def test_switch_japanese(self):
#     #     """日语"""
#     #     self.home.click_swictch_language()
#     #     self.home.switch_to_japanese()
#     #
#     # def test_switch_english(self):
#     #     """英语"""
#     #     self.home.click_swictch_language()
#     #     self.home.switch_to_emglish()
#
#     if __name__ == "__main__":
#         unittest.main()
#
#

# import unittest
# from driver.browser import chrome_browser
# from page.BookingPage import Bookflow
# from time import sleep
#
# class Test_Languages(unittest.TestCase):
#     def setUp(self):
#         self.driver = chrome_browser()
#         self.driver.get("https://www.millenniumhotels.com")
#
#     def tearDown(self):
#         self.driver.close()
#
#
#     def test_booking(self):
#         bookflow = Bookflow(self.driver)
#         bookflow.book_room()
#         bookflow.verify_url()
#
#
#     if __name__ == "__main__":
#         unittest.main()
#
#

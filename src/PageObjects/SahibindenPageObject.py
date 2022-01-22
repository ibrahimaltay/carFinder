import time

import src.PageElements.StaticPageElements as StaticPageElements
import src.Database.SqliteHelper as SqliteHelper
import src.PageElements.GenericPageElements as GenericPageElements
import src.Helpers.DriverHelper as DriverHelper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class Sahibinden:

    def __init__(self, searchUrl):
        self.searchUrl = searchUrl
        self.CreateDriver()
        self.driverHelper = DriverHelper.DriverHelper(driver=self.driver)
        self.sqlHelper = SqliteHelper.SqliteHelper('Cars.db')
        self.sqlHelper.CreateCarsTable()
        self.EnsureSearchPageIsOpen()

    def CreateDriver(self):
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options, executable_path="bin/drivers/linux/chromedriver")
        driver.maximize_window()
        self.driver = driver

    def EnsureSearchPageIsOpen(self):
        self.driver.get(self.searchUrl)
        self.driverHelper.ExplicitlyWaitForElementToExistByXpath(StaticPageElements.lastUpdatedDiv)

    def CheckIfNextPageButtonExists(self):
        return self.driverHelper.CheckIfElementExistsByXpath(StaticPageElements.nextPageButton)

    def ParseListings(self):
        while True:
            allListings = self.driver.find_elements_by_xpath(StaticPageElements.allListings)
            for listing in allListings:
                print('completeMePlease!')


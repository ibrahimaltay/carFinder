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
        self.sqlHelper.InsertDummyDataIntoTable()
        self.EnsureSearchPageIsOpen()

    def DisposeDriver(self):
        self.driver.close()

    def CreateDriver(self):
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options, executable_path="bin/drivers/linux/chromedriver")
        driver.maximize_window()
        self.driver = driver

    def EnsureSearchPageIsOpen(self):
        self.driver.get(self.searchUrl)
        self.driverHelper.ExplicitlyWaitForElementToExistByXpath(StaticPageElements.lastUpdatedDiv)
        if self.driverHelper.CheckIfElementExistsByXpath(StaticPageElements.closeCookiesButton):
            self.driver.find_element(by='xpath', value=StaticPageElements.closeCookiesButton).click()

    def CheckIfNextPageButtonExists(self):
        return self.driverHelper.CheckIfElementExistsByXpath(StaticPageElements.nextPageButton)

    def GoToNextPage(self):
        nextPageButton = self.driver.find_element(by="xpath", value=StaticPageElements.nextPageButton)
        self.driverHelper.ScrollToElement(nextPageButton)
        nextPageButton.click()
        time.sleep(2)
        self.driverHelper.ExplicitlyWaitForElementToExistByXpath(StaticPageElements.lastUpdatedDiv)

    def ParseListings(self):
        # While True until there is no next page button!
        while True:
            time.sleep(3)
            models = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.modelColumn)]
            titles = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.titleColumn)]
            years = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.yearColumn)]
            kilometers = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.kilometerColumn)]
            colors = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.colorColumn)]
            prices = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.priceColumn)]
            dates = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.dateColumn)]
            locations = [item.text for item in self.driver.find_elements(by='xpath', value=StaticPageElements.locationColumn)]
            urls = [item.get_attribute('href') for item in self.driver.find_elements(by='xpath', value=StaticPageElements.urlAnchor)]

            for i in range(len(models)):
                self.sqlHelper.InsertCarIfNotExists(str(models[i]), str(titles[i]), str(years[i]), str(kilometers[i]),
                                                    str(colors[i]),str(prices[i]), str(dates[i]), str(locations[i]),
                                                    str(urls[i]))


            print('listing complete!')
            if self.driverHelper.CheckIfElementExistsByXpath(StaticPageElements.nextPageButton):
                self.GoToNextPage()
            else:
                break


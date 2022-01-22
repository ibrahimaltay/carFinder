from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.action_chains import ActionChains

class DriverHelper:

    def __init__(self, driver):
        self.driver = driver
        self.maxWaitSeconds = 10

    def ExplicitlyWaitForElementToExistByXpath(self, elementToWaitXpath):
        element = WebDriverWait(self.driver, self.maxWaitSeconds).until(ExpectedConditions.presence_of_element_located((By.XPATH, elementToWaitXpath)))

    def ExplicitlyWaitForElementToBeClickableByXpath(self, elementToWaitXpath):
        element = WebDriverWait(self.driver, self.maxWaitSeconds).until(
            ExpectedConditions.element_to_be_clickable((By.XPATH, elementToWaitXpath)))

    # def ExplicitlyWaitForElementToBeClickable(self, elementToWait):
    #     element = WebDriverWait(self.driver, self.maxWaitSeconds).until(
    #         ExpectedConditions.element_to_be_clickable(elementToWait))

    def MouseHover(self, elementToHover):
        ActionChains(self.driver).move_to_element(elementToHover).perform()

    def DoubleClick(self, elementToDoubleClick):
        ActionChains(self.driver).double_click(elementToDoubleClick).perform()

    def SafeClickOnElement(self, elementToClick):
        self.ScrollToElement(elementToClick)
        self.MouseHover(elementToClick)
        elementToClick.click()

    def ScrollToElement(self, elementToScroll):
        ActionChains(self.driver).move_to_element(elementToScroll).perform()

    def CheckIfElementExistsByXpath(self, elementToCheckXpath):
        elementList = self.driver.find_elements_by_xpath(elementToCheckXpath)
        return len(elementList > 0)

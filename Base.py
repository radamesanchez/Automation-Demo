import json
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.chrome.service import Service



class Base:
    wait_time = 14
    servicePath = Service(r'')
    chromedriver = webdriver.Chrome(service=servicePath)
    url = 'https://en.wikipedia.org/'
    wait_variable = wait(chromedriver, wait_time)
    extractedLink = ''
    linkIsPresent = 0

    def __init__(self, driver):
        driver = self.chromedriver
        self.driver = driver
        self.wait_variable = wait(self.driver, self.wait_time)

    def click(self, element):
        self.wait_variable.until(expect.element_to_be_clickable(element)).click()

    def navigate(self, url):
        self.url = url
        self.chromedriver.get(url)

    def sendKeys(self, element, keys):
        self.wait_variable.until(expect.element_to_be_clickable(element)).send_keys(keys)

    def selectFromDropdown(self, element, elementToBeSelected):
        Select(self.wait_variable.until(expect.element_to_be_clickable(element))).select_by_visible_text(
            elementToBeSelected)

    def currentUrl(self, emptyLink):
        emptyLink = self.driver.current_url
        return emptyLink

    def extractProperty(self, element, property):
        elementProperty = self.wait_variable.until(expect.element_to_be_clickable(element)).get_property(property)
        self.extractedLink = elementProperty
        return elementProperty

    def assertLinkInList(self, listElementTagName, pageLink, attribute):
        counter = 0
        elements = self.driver.find_elements(By.TAG_NAME, listElementTagName)

        for element in elements:
            elementLink = elements[counter].get_attribute(attribute)
            counter = counter + 1

            if pageLink == elementLink:
                self.linkIsPresent += 1
                print(f'LINK FOUND: '
                      f'{elementLink}')

        if self.linkIsPresent == 1:
            print('    The page is on the bookmarks page')
        else:
            print('    The page was not properly saved on the bookmarks page')

        self.linkIsPresent = 0

    def selectFromList(self, listElementTagName, valueToBeSelected):
        listElement = self.driver.find_elements(By.TAG_NAME, listElementTagName)
        elementLink = listElement[valueToBeSelected]
        return elementLink

    def assertElementByProperty(self, expectedElement, actualElement, elementProperty):
        actualElementProperty = self.extractProperty(actualElement, str(elementProperty))
        expectedElementProperty = self.extractProperty(expectedElement, str(elementProperty))
        assert (actualElementProperty, expectedElementProperty)
        if actualElementProperty != expectedElementProperty:
            raise AssertionError(f'Element properties are not the same. '
                                 f'Expected: {expectedElementProperty}'
                                 f'Actual: {actualElementProperty}')
        else:
            print(f'Element properties are the same. '
                  f'Expected: {expectedElementProperty} '
                  f'Actual: {actualElementProperty} ')

    def assertElementByContent(self, expectedElementContent, actualElementContent):
        assert (actualElementContent, expectedElementContent)
        if actualElementContent != expectedElementContent:
            raise AssertionError(f'The content of the elements are not the same. '
                                 f''
                                 f'Expected: {expectedElementContent}.'
                                 f''
                                 f'Actual: {actualElementContent}')
        else:
            print(f'The content of the elements are the same. '
                                 f''
                                 f'Expected: {expectedElementContent}.'
                                 f''
                                 f'Actual: {actualElementContent}')

    def presenceOfPopupWindow(self,By ,popupWindowElement):
        assert popupWindowElement
        if not self.wait_variable.until(expect.element_to_be_clickable((By, popupWindowElement))).is_displayed():
            raise AssertionError(f''
                                 f'Window is not present')
        else:
            print(f''
                  f'Window is present')


    def teardown(self):
        self.driver.quit()


class Search(Base):
    searchField = (By.ID, 'searchInput')
    searchBtn = (By.ID, 'searchButton')
    logo = (By.ID, 'nav-logo')

    def searchArticle(self, sample):
        self.click(self.searchField)
        self.sendKeys(self.searchField, sample)

    def clickSearchButton(self):
        self.click(self.searchBtn)

    # another helper method could be useful here for other pages that may not want to multiple lines to search for something
    #   similar to login

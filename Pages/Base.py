import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as expect


class Base:
    wait_time = 7
    chrome_path = r'C:\Users\radam\OneDrive\Desktop\chromedriver'
    chrome = webdriver.Chrome(executable_path=chrome_path)
    wait_variable = wait(chrome, wait_time)

    def __init__(self, driver):

        driver = Base.chrome
        self.driver = driver
        wait_time = Base.wait_time
        self.wait_time = wait_time
        self.wait_variable = wait(self.driver, self.wait_time)

    def finalize_session(self):
        self.driver.quit()


class Search:
    baseObj = Base(Base.chrome)
    wait_variable = baseObj.wait_variable
    searchField = (By.ID, 'twotabsearchtextbox')
    searchButton = (By.ID, 'nav-search-submit-button')
    ##For adding
    firstItem = (By.CLASS_NAME, 's-image')
    addToCartButton = (By.ID, 'add-to-cart-button')
    cart = (By.ID, 'nav-cart')
    logo = (By.ID, 'nav-logo')

    deleteButton = (By.CLASS_NAME, 'a-color-link')
    quantityDropdownbutton = (By.ID, 'quantity')




    def searchItem(self,sample):
        searchSample = sample
        searchField = self.wait_variable.until(expect.element_to_be_clickable(self.searchField))
        searchField.send_keys(searchSample)
    def clickSearchButton(self):
        searchButton = self.wait_variable.until(expect.element_to_be_clickable(self.searchButton))
        searchButton.click()

    def addFirstItem(self):
        firstItem = self.wait_variable.until(expect.element_to_be_clickable(self.firstItem))
        firstItem.click()

    def addItemToCart(self):
        addToCart = self.wait_variable.until(expect.element_to_be_clickable(self.addToCartButton))
        addToCart.click()

    def navigateToCart(self):
        goTocart = self.wait_variable.until(expect.element_to_be_clickable(self.cart))
        goTocart.click()

    def selectItemAmount(self):
        quantityDropdownbutton = Select(self.wait_variable.until(expect.element_to_be_clickable(self.quantityDropdownbutton)))
        quantityDropdownbutton.select_by_value('5')

    def deleteItem(self):
        delete = self.wait_variable.until(expect.element_to_be_clickable(self.deleteButton))
        delete.click()


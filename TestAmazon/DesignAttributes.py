from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as expect
import time
from selenium.webdriver.support.ui import Select
##font size,font family and font color of the upper elements, and elements in the cart

'''class Attributes():


    self.upperLeftLogo = (By.ID, 'nav-logo-sprites')

    self.globalLocationTag = (By.ID, 'nav-global-location-popover-link')
    self.globalLocationTag_upperLetters = (By.ID, 'glow-ingress-line1')
    self.globalLocationTag_lowerLetters = (By.ID, 'glow-ingress-line2')

    self.categoryButton = (By.ID, 'nav-search-dropdown-card')

    self.searchBar = (By.ID, 'nav-search-bar-form')
    self.searchZoomButton = (By.ID, 'nav-search-submit-button')

    self.accountList = (By.ID, 'nav-link-accountList')
    self.accountList_upperFont = (By.ID, 'nav-link-accountList-nav-line-1')
    self.accountList_bottomFont = (By.CLASS_NAME, 'nav-line-2 ')

    self.returnsAndOrders = (By.ID, 'nav-orders')
    self.returnsAndOrders_topFont = (By.ID, 'nav-line-1')
    self.returnsAndOrders_bottomFont = (By.ID, 'nav-line-2')

    self.cart = (By.ID, 'nav-cart')
    self.cartLogo = (By.ID, 'nav-cart-icon nav-sprite')
    self.cartCount = (By.ID, 'nav-cart-count')
    self.cartFont = (By.CLASS_NAME, 'nav-line-2')

    self.mainNavigation = (By.ID, 'nav-main')

    self.flagLanguageIcon = (By.ID, 'icp-nav-flyout')
    self.flagLanguageIcon_flag = (By.CLASS_NAME, 'icp-nav-flag icp-nav-flag-us')

    self.productContainer = (By.CLASS_NAME, 'sc-list-item-content')
    self.productImage = (By.CLASS_NAME, 'sc-product-image')
    self.productNameFont = (By.CLASS_NAME, 'a-truncate-cut')

    def AttributeScan(self):


        upperLeftLogo = self.wait_variable.until(expect.element_to_be_clickable(self.upperLeftLogo))
        print(f"Navigation logo sizing:{upperLeftLogo.size}")
        hex = Color.from_string(upperLeftLogo.value_of_css_property('color')).hex
        print(f"Navigation logo color: {hex}")
        print("")

        globalLocationTag = self.wait_variable.until(expect.element_to_be_clickable(self.globalLocationTag))
        globalLocationTag_upperLetters = self.wait_variable.until((expect.element_to_be_clickable(self.globalLocationTag_upperLetters)))
        globalLocationTag_lowerLetters = self.wait_variable.until((expect.element_to_be_clickable(self.globalLocationTag_lowerLetters)))
        print(f"Global location tag sizing:{globalLocationTag.size}")
        print(f"Global location tag color: {hex}")
        print(f"Global location top letters font family: {globalLocationTag_upperLetters.value_of_css_property('font-family')}")
        print(f"Global location bottom letters font family: {globalLocationTag_lowerLetters.value_of_css_property('font-family')}")
        print(f"Global location top letters font size: {globalLocationTag_upperLetters.value_of_css_property('font-size')}")
        print(f"Global location bottom letters font size: {globalLocationTag_lowerLetters.value_of_css_property('font-size')}")
        topColor = Color.from_string(globalLocationTag_upperLetters.value_of_css_property('color')).hex
        bottomColor = Color.from_string(globalLocationTag_lowerLetters.value_of_css_property('color')).hex
        print(f"Global location top letters font color: {topColor}")
        print(f"Global location bottom letters font color: {bottomColor}")


        categoryButton = self.wait_variable.until(expect.element_to_be_clickable(self.categoryButton))
        print(f"Category dropdown sizing:{categoryButton.size}")
        print(f"Category dropdown font size: {categoryButton.value_of_css_property('font-weight')}")
        hex = Color.from_string(categoryButton.value_of_css_property('color')).hex
        print(f"Category button color {hex}")
        print("")

        searchBar = self.wait_variable.until(expect.element_to_be_clickable(self.searchBar))
        print(f"Search bar sizing:{searchBar.size}")
        hex = Color.from_string(searchBar.value_of_css_property('color')).hex
        print(f"Search color {hex}")
        print("")

        searchZoomButton = self.wait_variable.until(expect.element_to_be_clickable(self.searchZoomButton))
        print(f"Search button sizing:{searchZoomButton.size}")
        hex = Color.from_string(searchZoomButton.value_of_css_property('color')).hex
        print(f"Search button color {hex}")
        print("")

        accountList = self.wait_variable.until(expect.element_to_be_clickable(self.accountList))
        accountList_upperFont = self.wait_variable.until(expect.element_to_be_clickable(self.accountList_upperFont))
        accountList_bottomFont = self.wait_variable.until(expect.element_to_be_clickable(self.accountList_bottomFont))


        print(f"Account list top font size:{accountList_upperFont.size}")
        hex = Color.from_string(accountList_upperFont.value_of_css_property('color')).hex
        print(f"Account list top font color:{hex}")
        print(f"Account List top font family: {accountList_upperFont.value_of_css_property('font-family')}")


        print(f"Account list bottom font size:{accountList_bottomFont.size}")
        hex = Color.from_string(accountList_bottomFont.value_of_css_property('color')).hex
        print(f"Account list bottom font color:{hex}")
        print(f"Account List bottom font family: {accountList_bottomFont.value_of_css_property('font-family')}")
        print("")
        print(f"Account List overall size: {accountList.size}")
        print("")

        cart = self.wait_variable.until(expect.element_to_be_clickable(self.cart))
        cartFont = self.wait_variable.until(expect.element_to_be_clickable(self.cartFont))


        print(f"Cart sizing:{cart.size}")
        print(f"Cart font size:{cartFont.size}")
        hex = Color.from_string(cartFont.value_of_css_property('color')).hex
        print(f"Cart font color:{hex}")
        print(f"Cart font family: {cartFont.value_of_css_property('font-family')}")

        returnsAndOrders = self.wait_variable.until(expect.element_to_be_clickable(self.returnsAndOrders))
        print(f"Returns and orders dropdown sizing:{returnsAndOrders.size}")
        print(f"Returns and orders font size: {returnsAndOrders.value_of_css_property('font-weight')}")
        print(f"Returns and orders font family: {returnsAndOrders.value_of_css_property('font-family')} "
              f" Returns and orders padding: {returnsAndOrders.value_of_css_property('padding')}")
        hex = Color.from_string(returnsAndOrders.value_of_css_property('color')).hex
        print(f"Returns and orders color: {hex}")
        print("")


        mainNavigation = self.wait_variable.until(expect.element_to_be_clickable(self.mainNavigation))
        print(f"Main navigation size:{mainNavigation.size}")
        print("")


        flagLanguageIcon = self.wait_variable.until(expect.element_to_be_clickable(self.flagLanguageIcon))
        print(f"Language selection dropdown sizing:{flagLanguageIcon.size}")
        print(f"Language selection font size (if present): {flagLanguageIcon.value_of_css_property('font-weight')}")
        hex = Color.from_string(flagLanguageIcon.value_of_css_property('color')).hex
        print(f"Language Icon/Flag Color: {hex}")
        print("")


        productImage = self.wait_variable.until(expect.element_to_be_clickable(self.productImage))
        productContainer = self.wait_variable.until(expect.element_to_be_clickable(self.productContainer))
        productNameFont = self.wait_variable.until(expect.element_to_be_clickable(self.productNameFont))
        print(f"Product image size: {productImage.size}")
        print(f"Product container size: {productContainer.size}")

        print(f"Product name font size:{accountList_bottomFont.size}")
        hex = Color.from_string(accountList_bottomFont.value_of_css_property('color')).hex
        print(f"Product name font color:{hex}")
        print(f"Product name font family: {accountList_bottomFont.value_of_css_property('font-family')}")

        def highlight(element):
            driver = element._parent

            def apply_style(s):
                driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                      element, s)

            original_style = element.get_attribute('style')
            apply_style("background: yellow; border: 2px solid red;")
            time.sleep(3)
            apply_style(original_style)


        highlight(mainNavigation)
        highlight(upperLeftLogo)

        time.sleep(5)
'''





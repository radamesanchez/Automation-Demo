import pytest

from Pages.Base import Base
from Pages.Base import Search
from Pages.LoginPage import Login
from Pages.OrdersPage import Orders

searchSample = 'BLACK T-SHIRT'
url = "https://amazon.com"
chrome = Base(Base.chrome)
searchObject = Search()


def test_logIn():

    loginObject = Login(chrome)
    loginObject.driver.get(url)
    loginObject.driver.maximize_window()
    loginObject.clickLoginButton()
    loginObject.setUsernameField(loginObject.username)
    loginObject.click_continue_button()
    loginObject.setPasswordField(loginObject.password)
    loginObject.submitInformation()




def test_track_order_from_last_year():
    ordersTrackingObject = Orders(chrome)
    ordersTrackingObject.driver.get(url)
    ordersTrackingObject.navigateOrdersPage()
    ordersTrackingObject.selectLastYear()
    ordersTrackingObject.selectFirstOrder()
    ordersTrackingObject.trackFirstOrder()

def test_search_and_add_sample_element():
    ordersObject = Orders(chrome)
    ordersObject.driver.get(url)
    ordersObject.searchItem(searchSample)
    ordersObject.clickSearchButton()
    ordersObject.addFirstItem()
    ordersObject.addItemToCart()
    ordersObject.navigateToCart()
    ordersObject.deleteItem()






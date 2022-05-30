from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import Select
from Pages.Base import Base as b
from Pages.Base import Search as s


class Orders(s,b):
    ordersLink = (By.ID, 'nav-orders')
    OrdersYear = (By.CLASS_NAME, 'a-native-dropdown')
    firstOrderInvoice = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/div[3]/div[1]/div/div/div/div[2]/div[2]/ul/a[1]')
    OrderTracker = (By.ID, 'a-autoid-1-announce')

    def navigateOrdersPage(self):
        orders = self.wait_variable.until(expect.element_to_be_clickable(self.ordersLink))
        orders.click()

    def selectLastYear(self):
        yearSelect = Select(self.wait_variable.until(expect.element_to_be_clickable(self.OrdersYear)))
        yearSelect.select_by_value('year-2021')

    def selectFirstOrder(self):
        firstOrder = self.wait_variable.until(expect.element_to_be_clickable(self.firstOrderInvoice))
        firstOrder.click()

    def trackFirstOrder(self):
        firstOrderTracker = self.wait_variable.until(expect.element_to_be_clickable(self.OrderTracker))
        firstOrderTracker.click()

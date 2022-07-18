from Base import Base as b
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DonationsPage(b):
    donationPageURL = 'https://donate.wikimedia.org/w/index.php?title=Special:LandingPage&country=US&uselang=en&utm_medium=sidebar&utm_source=donate&utm_campaign=C13_en.wikipedia.org'
    donationAmountList = ('li')
    payByCardElement = (By.CLASS_NAME, 'payment-method-button')
    selectedAmount = (By.ID,'selected-amount')

    def assertDonationAmount(self,donationOption):
        self.navigate(self.donationPageURL)
        expectedAmount = self.selectFromList(listElementTagName=self.donationAmountList, valueToBeSelected= donationOption)
        self.click(expectedAmount)
        expectedAmountProperty =  self.extractProperty(expectedAmount,'innerText')
        self.click(self.payByCardElement)
        actualAmount = self.extractProperty(self.selectedAmount,'innerText')
        self.assertElementByContent(expectedAmountProperty,actualAmount)
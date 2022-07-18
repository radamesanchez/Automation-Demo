from selenium.webdriver.common.by import By
from Base import Base as b

class PreferencesPage(b):
    homepageDateElement = (By.XPATH,'/html/body/div/div/div[1]/div[3]/main/div[2]/div[4]/div[1]/div[2]/div[2]/div[2]/p/b/a')
    preferencesPageURL = b.url + '/wiki/Special:Preferences#mw-prefsection-rendering'
    serverDateElement = (By.XPATH,'/html/body/div[1]/div/div[1]/div[3]/main/div[2]/div[4]/div[3]/form/div/div[1]/div/div[2]/div/div[2]/fieldset/div/div/div[3]/fieldset/div/div/div/div/div/div/div/div[2]/div/span[2]/label')
    confirmationMessage = 'The Server date matches On This Day date'

    def verifyDateInServer(self):
        self.driver.maximize_window()
        self.navigate(b.url)
        homepageDate = self.extractProperty(self.homepageDateElement, 'textContent')
        self.navigate(self.preferencesPageURL)
        serverDate = self.extractProperty(self.serverDateElement, 'textContent')

        if serverDate.__contains__(homepageDate):
            print(self.confirmationMessage)


from selenium.webdriver.common.by import By
from Base import Base as b
from Base import Search as search

##Check to see if the page naviagted to the right url after clicking the log in button
##Try a bad login and make a checker to see if an alert popped up
class Login(b):
    logInBtn = (By.ID,'pt-login')
    usernameField = (By.ID,'wpName1')
    passwordField = (By.ID, 'wpPassword1')
    continueLogInBtn = (By.ID, 'wpLoginAttempt')
    uri = b.url + 'w/index.php?title=Special:UserLogin&returnto=Main+Page'
    badLoginPopupWindow = '/html/body/div[3]/div[3]/div[4]/div[1]/div[2]/form/div[1]'
    logOutURL = b.url + '/w/index.php?title=Special:UserLogout&returnto=Special%3AWatchlist'
    submitLogOutBtn = (By.ID, 'ooui-php-2')

    def clickLoginBtn(self):
        self.click(self.logInBtn)

    def setUsername(self,username):
        self.click(self.usernameField)
        self.sendKeys(self.usernameField, username)

    def setPassword(self,password):
        self.click(self.passwordField)
        self.sendKeys(self.passwordField, password)

    def clickContinueBtn(self):
        self.click(self.continueLogInBtn)

    def loginAs(self, username, password):
        self.navigate(self.uri)
        self.setUsername(username)
        self.setPassword(password)
        self.clickContinueBtn()

    def logOut(self):
        self.navigate(self.logOutURL)
        self.click(self.submitLogOutBtn)

    def badLogin(self,username,password):
        self.navigate(self.uri)
        self.setUsername(username)
        self.setPassword(password)
        self.clickContinueBtn()
        self.presenceOfPopupWindow(By.XPATH,self.badLoginPopupWindow)




from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as expect
from Pages.Base import Base as b
from Pages.Base import Search as search


class Login(b):
    ##For the login
    username = 'radamesac.24@gmail.com'
    password = 'R030898S.'
    signIn = (By.XPATH, '/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]')
    inputUsername = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]')
    continueSignIn = (By.XPATH, '//*[@id="continue"]')
    passwordInput = (By.XPATH, '//*[@id="ap_password"]')
    submit = (By.ID, 'signInSubmit')

    def clickLoginButton (self):

        signInbutton = self.wait_variable.until(expect.element_to_be_clickable(self.signIn))
        signInbutton.click()

    def setUsernameField(self,username):
        inputUser = self.wait_variable.until(expect.element_to_be_clickable(self.inputUsername))
        inputUser.send_keys(self.username)

    def click_continue_button(self):
        continueButton =  self.wait_variable.until(expect.element_to_be_clickable(self.continueSignIn))
        continueButton.click()

    def setPasswordField(self,password):
        passwordInput = self.wait_variable.until(expect.element_to_be_clickable(self.passwordInput))
        passwordInput.send_keys(self.password)

    def submitInformation(self):
        submitButton = self.wait_variable.until(expect.element_to_be_clickable(self.submit))
        submitButton.click()






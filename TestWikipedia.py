import time

import pytest
import json

import WatchlistPage
from Base import Base
from Base import Search
from LoginPage import Login
from WatchlistPage import Watchlist
from PreferencesPage import PreferencesPage
from DonationsPage import  DonationsPage


##Test to see if the page pops up a warning for a bad login

chrome = Base(Base.chromedriver)
searchPage = Search(chrome)

def test_correct_donation_amount():
    donationsPage = DonationsPage(chrome)
    donationsPage.assertDonationAmount(2)

def test_logIn():

    loginPage = Login(chrome)
    loginPage.driver.maximize_window()
    loginPage.loginAs(username = "Radames0308",password = "Testing0308.")

def test_add_article():
    watchlistPage = Watchlist(chrome)
    watchlistPage.addRandomArticleToWatchlist()

def test_assert_server_date():
    preferencesPage = PreferencesPage(chrome)
    preferencesPage.verifyDateInServer()

def test_log_out():
    loginPage = Login(chrome)
    loginPage.logOut()

def test_bad_login():
   badLogin = Login(chrome)
   badLogin.badLogin(username = 'notausername', password='notapassword')

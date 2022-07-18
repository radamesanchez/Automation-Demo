from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.ui import Select
from Base import Base as b
from Base import Search as s
from datetime import date


class Watchlist(s, b):
    articleTitle = (By.ID, 'firstHeading')
    addToWatchlistBtn = (By.ID, 'ca-watch')
    watchlistURL = b.url + '/wiki/Special:Watchlist'
    editWatchlistURL = b.url + '/wiki/Special:EditWatchlist'
    randomArticleURL = b.url + '/wiki/Special:Random'
    deleteBtn = (By.CLASS_NAME, 'a-color-link')
    linksList = ('a')

    # If we change this to selectYear and have it take a date object, it would keep the test relevant for years.
    # I'm not familiar with python but the test would be able to do something like selectYear(dateTime.Now.year)


    def addRandomArticleToWatchlist(self):
        self.driver.maximize_window()
        self.navigate(self.randomArticleURL)
        self.extractProperty(self.articleTitle, 'baseURI')
        self.click(self.addToWatchlistBtn)
        self.navigate(self.editWatchlistURL)
        self.driver.refresh()
        self.assertLinkInList(pageLink=self.extractedLink, listElementTagName=self.linksList, attribute= 'href')


package Pages;

import org.junit.Test;
import org.openqa.selenium.By;
import org.junit.Assert.*;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;


public class sideNavigationPages extends Base {
    By explore = (By.xpath("//a[contains(@title,'Explore')]"));
    By subscriptions = (By.xpath("//a[contains(@title,'Subscriptions')]"));
    By library = (By.xpath("//a[contains(@title,'Library')]"));
    By history = (By.xpath("//a[contains(@title,'History')]"));
    By shorts = (By.xpath("//a[contains(@title,'Shorts')]"));
    String current = chrome.getCurrentUrl();



    @Test
    public void exploreNavigationChecker() throws Exception {
        WebElement exploreNavigation = wait.until(ExpectedConditions.elementToBeClickable(explore));
        exploreNavigation.click();
        current = chrome.getCurrentUrl();
        try {
            if ((!current.equalsIgnoreCase("https://www.youtube.com/feed/explore"))) throw new AssertionError();
            else{System.out.print("Correct url for the Explore elements");}
        }
        catch(AssertionError assertionError){
            System.out.print("Incorrect url for the Explore element");
        }

    }

    public void subscriptionNavigationChecker() throws Exception {
        WebElement subscriptionsNavigation = wait.until(ExpectedConditions.elementToBeClickable(subscriptions));
        subscriptionsNavigation.click();
        current = chrome.getCurrentUrl();
        try {
            if ((!current.equalsIgnoreCase("https://www.youtube.com/feed/subscriptions"))) throw new AssertionError();
            else{System.out.print("Correct url for the Subscriptions element");}
        }
        catch(AssertionError assertionError){
            System.out.print("Incorrect url for the Subscriptions element");
        }
    }


    public void libraryNavigationChecker() throws Exception {
        WebElement libraryNavigation = wait.until(ExpectedConditions.elementToBeClickable((library)));
        libraryNavigation.click();
        current = chrome.getCurrentUrl();
        try {
            if ((!current.equalsIgnoreCase("https://www.youtube.com/feed/library"))) throw new AssertionError();
            else{System.out.print("Correct url for the Library element");}
        }
        catch(AssertionError assertionError){
            System.out.print("Incorrect url for the Library element");
        }
    }

    public void historyNavigationChecker() throws Exception {
        WebElement historyNavigation = wait.until(ExpectedConditions.elementToBeClickable((history)));
        historyNavigation.click();
        current = chrome.getCurrentUrl();
        try {
            if ((!current.equalsIgnoreCase("https://www.youtube.com/feed/history"))) throw new AssertionError();
            else{System.out.print("Correct url for the History element");}
        }
        catch(AssertionError assertionError){
            System.out.print("Incorrect url for the History element");
        }
    }
    public void shortsNavigationChecker() throws Exception {
        WebElement shortsNavigation = wait.until(ExpectedConditions.elementToBeClickable((shorts)));
        shortsNavigation.click();
        current = chrome.getCurrentUrl();
        try {
            if ((!current.equalsIgnoreCase("https://www.youtube.com/feed/shorts"))) throw new AssertionError();
            else{System.out.print("Correct url for the Shorts element");}
        }
        catch(AssertionError assertionError){
            System.out.print("Incorrect url for the Shorts element");
        }
    }


    }



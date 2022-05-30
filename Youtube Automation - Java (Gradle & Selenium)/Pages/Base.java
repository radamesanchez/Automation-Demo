package Pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Base {
    WebDriver chrome;
    WebDriverWait wait;


    //Sign variables
    By signIn = (By.id("buttons"));
    By inputContainer = (By.id("identifierId"));
    By next = (By.id("identifierNext"));
    //Search variables
    By searchButton = (By.id("search-icon-legacy"));
    By searchBoxContainer = (By.xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"));

    public Base() {

        System.setProperty("webdriver.chrome.driver", "C:\\Users\\radam\\OneDrive\\Desktop\\chromedriver.exe");
        ChromeOptions a = new ChromeOptions();
        String[] ss = {"1"};
        a.addArguments("permissions.default.microphone", ss[0]);
        chrome = new ChromeDriver();
        wait = new WebDriverWait(chrome, 11, 7000);
    }

    public void setUp() {

        chrome.get("https://www.youtube.com/");
        chrome.manage().window().maximize();
    }
    public void finalize_session(){
        chrome.quit();

    }

    public void initializeSignIn() {
        WebElement signInButton = wait.until(ExpectedConditions.elementToBeClickable(signIn));
        WebElement inputContainerBox = wait.until(ExpectedConditions.elementToBeClickable(inputContainer));
        signInButton.click();
        inputContainerBox.sendKeys("radamesac.24@gmail.com");
        WebElement nextButton = wait.until(ExpectedConditions.elementToBeClickable(next));
        nextButton.click();
    }

    public void searchElement(String elementToBeSearched) {
        WebElement searchBoxContainerVariable = wait.until(ExpectedConditions.elementToBeClickable(searchBoxContainer));
        WebElement searchButtonVariable = wait.until(ExpectedConditions.elementToBeClickable(searchButton));
        searchBoxContainerVariable.sendKeys(elementToBeSearched);
        searchButtonVariable.click();
    }
}


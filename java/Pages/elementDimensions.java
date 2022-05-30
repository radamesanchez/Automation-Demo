package Pages;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class elementDimensions extends Base {

    By micIcon = (By.id("voice-search-button"));
    By guideIcon =  (By.id("guide-icon"));
    By searchBoxContainer = (By.xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"));
    By searchButton = (By.id("search-icon-legacy"));


    public void guideIconFeatures() throws Exception {
        WebElement guideIconElement = wait.until(ExpectedConditions.elementToBeClickable(guideIcon));
        System.out.println("Mic icon dimensions: ");
        System.out.println("Width: " + (guideIconElement.getCssValue("width") + ", Height:" + guideIconElement.getCssValue("height")));

    }

      public void searchBarFeatures() throws Exception {
         WebElement searchBarContainerElement =  wait.until(ExpectedConditions.elementToBeClickable(searchBoxContainer));
            System.out.println("Search bar  dimensions: ");
            System.out.println("Width: " + (searchBarContainerElement.getCssValue("width") + ", Height:" + searchBarContainerElement.getCssValue("height")));
        }

    public void searchButtonFeatures() throws Exception {
        WebElement searchButtonElement = wait.until(ExpectedConditions.elementToBeClickable(searchButton));
        System.out.println("Search button dimensions: ");
        System.out.println("Width: " + (searchButtonElement.getCssValue("width") + ", Height:" + searchButtonElement.getCssValue("height")));
    }

    public void micIconFeatures() throws Exception{
        WebElement microphoneIconElement = wait.until(ExpectedConditions.elementToBeClickable(micIcon));
        System.out.println("Mic icon dimensions: ");
        System.out.println("Width: " + (microphoneIconElement.getCssValue("width") + ", Height:" + microphoneIconElement.getCssValue("height")));
    }
}

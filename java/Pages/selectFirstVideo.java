package Pages;
import org.junit.Test;
import Pages.Base;
import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class selectFirstVideo extends Base {
    By video_title = (By.id("video-title"));
    By search_input = (By.id("search-input"));


    public void select_first_video() throws Exception, TimeoutException {
        WebElement firstVideoElement = wait.until(ExpectedConditions.elementToBeClickable(video_title));
        WebElement searchInputElement = wait.until(ExpectedConditions.elementToBeClickable((search_input)));

        firstVideoElement.click();
        searchInputElement.click();

    }
}

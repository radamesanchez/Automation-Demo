import Pages.*;
import org.junit.Test;

public class test_youtube  {

    @Test
     public void test_uiElements() throws Exception {
        elementDimensions elementDimensionsObject = new elementDimensions();
        elementDimensionsObject.setUp();
        elementDimensionsObject.guideIconFeatures();
        elementDimensionsObject.micIconFeatures();
        elementDimensionsObject.searchBarFeatures();
        elementDimensionsObject.searchButtonFeatures();
        elementDimensionsObject.finalize_session();
        elementDimensionsObject.finalize_session();
    }

    @Test
    public void test_selectFirstVideo() throws Exception{
        selectFirstVideo selectFirstVideoObject = new selectFirstVideo();
        selectFirstVideoObject.setUp();
        selectFirstVideoObject.select_first_video();
        selectFirstVideoObject.finalize_session();
        selectFirstVideoObject.finalize_session();
    }

    @Test
    public void test_sideNavigationPages() throws Exception{
         sideNavigationPages sideNavigationPagesObject = new sideNavigationPages();
         sideNavigationPagesObject.setUp();
         sideNavigationPagesObject.exploreNavigationChecker();
         sideNavigationPagesObject.historyNavigationChecker();
         sideNavigationPagesObject.libraryNavigationChecker();
         sideNavigationPagesObject.subscriptionNavigationChecker();
         sideNavigationPagesObject.shortsNavigationChecker();
         sideNavigationPagesObject.finalize_session();
         Runtime.getRuntime().exec("taskkill /F /IM chrome.exe");
    }


    public static void main(String[] args) throws Exception {

    }
}


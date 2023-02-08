from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import re
import page as page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://ecutbildning.se/")
        # Take care of Cookies
        main_page = page.MainPage(self.driver)
        main_page.click_min_cookies()
    

    def test_1_our_course(self):
        main_page = page.MainPage(self.driver)

        main_page.click_our_courses()
        # Verify page title
        assert main_page.is_title_1_match(), "Page: Yh-utbildningar doesn't match"
        
        main_page.click_softwaretester()
        # Verify page title self.assert
        self.assertTrue(main_page.is_title_2_match(), "Page: Mjukvarutestare doesn't match")

        location_text = main_page.find_study_location()   
        # Verifify the course is available in Malmö
        assert location_text.find("Malmö") != -1, "Malmö not present"
        assert re.search("Malmö", location_text), "Malmö not present" # Via regex

        duration_text = main_page.find_duration()
        malmo_duration = re.search(r"\b\d+\.\d+\b(?= år \(Malmö\))|\b\d+\b(?= år \(Malmö\))", 
                                   duration_text)
        # Verifify course duration
        assert '2' == malmo_duration.group(0), "Course not 2 year"


    def test_2_malmoe_location(self):
        main_page = page.MainPage(self.driver)

        # Find search search field
        main_page.click_search_button()
        # Verify searchform found
        assert main_page.find_search_form(), "No searchform found"
        # Set search text
        main_page.search_text_element = "malmö"
        # Submit
        main_page.search_submit()
        #Verify search results
        search_results_page = page.SearchResultPage(self.driver)
        self.assertTrue(search_results_page.is_results_found(), "No results found.")
        self.assertNotIn("No results found", self.driver.page_source)
        
        # Find Malmö and click, wait for result header to be present
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(
            page.SearchResultsPageLocators.SEARCH_RETURN))
        search_results_page.find_malmoe_in_search_results()
        # Verify adress
        assert "Östra Kanalgatan 5" == main_page.get_adress(), "Östra Kanalgatan 5 not found"
        # Verify softwaretester is available
        assert main_page.find_softwaretester(), 'No element with "Mjukvarutestare"'


    def test_3_news_article(self):
        main_page = page.MainPage(self.driver)
        news_header = main_page.find_first_news_header()
        # Goto article
        main_page.click_on_news_header()
        article_header = main_page.read_header_in_article()
        self.assertIn(news_header, article_header, "News/Article header doesn't match")

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

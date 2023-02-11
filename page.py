from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    # This locator can be changed during tests
    # by adding new 'name' locator
    # ex: page.SearchTextElement.locator = 'q'
    locator = "s"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()
    main_page_title = "Yh-utbildningar inom IT och teknik | Yrkeshögskola | EC Utbildning"
    mvt_page_title = "Mjukvarutestare | Yh-utbildning inom IT och teknik | EC Utbildning"

    def is_title_1_match(self):
        return self.main_page_title in self.driver.title

    def is_title_2_match(self):
        return self.mvt_page_title in self.driver.title

    def is_title_3_match(self):
        return ""
    
    def find_search_form(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_FORM) # the * unpack the object
        return element
    
    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH) 
        element.click()

    def search_submit(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_SUBMIT)
        element.click()

    def click_min_cookies(self):
        element = self.driver.find_element(*MainPageLocators.MIN_COOKIES)
        element.click()

    def click_our_courses(self):
        element = self.driver.find_element(*MainPageLocators.OUR_COURSES)
        element.click()
    
    def click_softwaretester(self):
        element = self.driver.find_element(*MainPageLocators.SOFTWARETESTER)
        element.click()

    def find_study_location(self):
        element_text = self.driver.find_element(*MainPageLocators.STUDY_LOCATION)
        return element_text.text

    def find_duration(self):
        element_text = self.driver.find_element(*MainPageLocators.COURSE_DURATION)
        return element_text.text
    
    def get_adress(self):
        element = self.driver.find_element(*MainPageLocators.GET_ADRESS)
        return element.text
    
    def find_softwaretester(self):
        try:
            element = self.driver.find_element(*MainPageLocators.FIND_SOFTWARETESTER)
            return element
        except:
            return False
        
    def find_first_news_header(self):
        element = self.driver.find_element(*MainPageLocators.FIND_NEWS_HEADER)
        return element.text
    
    def click_on_news_header(self):
        element = self.driver.find_element(*MainPageLocators.CLICK_NEWS_HEADER)
        element.click()

    def read_header_in_article(self):
        element = self.driver.find_element(*SearchResultsPageLocators.READ_ARTICLE_HEADER)
        return element.text
    
class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source

    def find_malmoe_in_search_results(self):
        element = self.driver.find_element(*SearchResultsPageLocators.FIND_MALMOE)
        element.click()
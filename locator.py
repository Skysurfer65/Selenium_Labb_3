from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH = (By.LINK_TEXT, "Sök")
    MIN_COOKIES = (By.ID, "cc-b-custom")
    OUR_COURSES = (By.PARTIAL_LINK_TEXT, "Våra utbildningar")
    SOFTWARETESTER = (By.XPATH, '//*[@id="search-filter-results-37"]/div[1]/div[8]/a/div/div/div/h3')
    STUDY_LOCATION = (By.XPATH, '//*[@id="page"]/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div/div/p[8]/span[2]')
    COURSE_DURATION = (By.XPATH, '//*[@id="page"]/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div/div/p[4]/span[2]')
    SEARCH_FORM = (By.CLASS_NAME, "search-form-container")
    SEARCH_SUBMIT = (By.ID, "searchsubmit")
    GET_ADRESS = (By.XPATH, '//*[@id="page"]/div[3]/section/div[11]/div[1]/div/article/div[2]/div[1]/p[1]')
    FIND_SOFTWARETESTER = (By.XPATH, "//*[@title='Mjukvarutestare']")
    FIND_NEWS_HEADER = (By.XPATH, '//*[@id="page"]/div[2]/div[4]/div/div[1]/div[6]/div[1]/div/div/a/h3')
    CLICK_NEWS_HEADER = (By.XPATH, '//*[@id="page"]/div[2]/div[4]/div/div[1]/div[6]/div[1]/div/div/a/h3')
       
class SearchResultsPageLocators(object):
    SEARCH_RETURN = (By.TAG_NAME, 'h1')
    READ_ARTICLE_HEADER = (By.XPATH, '//*[@id="page"]/div[3]/div[1]/div/div/div/div/div[1]/h1')
    FIND_MALMOE = (By.LINK_TEXT, "Malmö")
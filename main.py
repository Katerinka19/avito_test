from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    link = "https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5.0)
    button = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button')
    ActionChains(browser).move_to_element(button).click(button).perform()
    browser.implicitly_wait(2.0)
    button = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/button')
    print("Is now favorite:", button.get_attribute("title") == "В избранном")
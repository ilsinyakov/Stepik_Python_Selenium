from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:    
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ищем элемент, содержащий значение num1    
    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    # Получаем из элемента текст и переводим его в число
    num1 = int(num1_element.text)
    
    # Ищем элемент, содержащий значение num2    
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    # Получаем из элемента текст и переводим его в число
    num2 = int(num2_element.text)
    
    # Считаем результат
    res = num1 + num2
    #  Выбираем результат в селекте
    select_res = Select(browser.find_element(By.TAG_NAME, "select"))
    select_res.select_by_value(f"{res}")
    
    # Нажимаем кнопку "Submit"
    browser.find_element(By.TAG_NAME, "button").click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
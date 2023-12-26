from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:    
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ищем элемент, содержащий значение х    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # вытаскиваем из элемента само значение
    x = x_element.text
    # Считаем ответ
    y = calc(x)
    
    # Вводим ответ в поле
    field_y = browser.find_element(By.CSS_SELECTOR, "#answer")
    field_y.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    
    # Отмечаем радиобаттон "robotsRule"
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    
    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:    
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # нажимаем кнопку "I want..."
    browser.find_element(By.CLASS_NAME, "btn").click()

    # нажимаем "Да" в окне confirm. Переключаем фокус на confirm-окно и применяем метод accept()
    browser.switch_to.alert.accept()    
    
    # Ищем элемент, содержащий значение х    
    x_element = browser.find_element(By.ID, "input_value")
    # вытаскиваем из элемента само значение
    x = x_element.text
    # Считаем ответ
    y = calc(x)
    
    # Вставляем ответ в поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    # нажимаем кнопку "Submit"
    browser.find_element(By.CLASS_NAME, "btn").click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
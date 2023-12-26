from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:    
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)    
    
    # ишем кнопку
    button = browser.find_element(By.ID, "book")
    # ждем, когда цена станет 100$
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # жмем кнопку
    button.click()    
    
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
    browser.find_element(By.ID, "solve").click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
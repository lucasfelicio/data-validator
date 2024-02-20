from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from time import sleep

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.set_page_load_timeout(3)

try:
    driver.get("http://localhost:8501")
    sleep(3)
    print("Acesso realizado com sucesso!")
except TimeoutException:
    print("Tempo de carregamento da página execedeu o limite!")
finally:
    driver.quit()
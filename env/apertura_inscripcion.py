from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import time


def bot_send_text(bot_message):
    
    bot_token = 'BOT_FATHER_TOKEN' 
    bot_chatID = 'BOT_CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response

flag = True
while flag:
    time.sleep(60)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'PATH\TO\chromedriver.exe', chrome_options=options)
    driver.get("https://vacunate.corrientes.gob.ar/vacunate/inscripcion")  #URL a analizar
    driver.find_element_by_xpath("//select[@name='residencia']/option[text()='Ciudad de Corrientes']").click()
    elem = driver.find_element_by_name('residencia')
    selector = Select(driver.find_element_by_name("motivo_id"))
    options = selector.options
    for index in range(0, len(options)-1):
        if "18" in options[index].text:
            valor = False
            mensaje = "Si hay vacuna para +18 años"
            bot_send_text(mensaje)
    driver.close()
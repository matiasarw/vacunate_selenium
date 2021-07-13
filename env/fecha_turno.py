from selenium import webdriver
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
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(r'PATH\TO\chromedriver.exe', chrome_options=options)
    driver.get("https://vacunate.corrientes.gob.ar/vacunate/verificar") #URL a analizar
    driver.find_element_by_xpath("//select[@name='sexo']/option[text()='Femenino']").click()
    inputElement = driver.find_element_by_id("dni")
    inputElement.send_keys('DNI_EJEMPLO') #Setear el DNI a consultar
    inputElement = driver.find_element_by_id("codigo")
    inputElement.send_keys('CODIGO_INSCRIPCION') #Setear el codigo de inscripcion
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    time.sleep(1)
    if (driver.page_source.find("Aún no se le ha asignado") == -1):
        mensaje = "Ya tenes turno!"
        bot_send_text(mensaje)    
    driver.close()
    time.sleep(100)

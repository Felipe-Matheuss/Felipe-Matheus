#BOT E AUTOMAÇÃO WEB:

#Boletim Climático: Enviado para e-mail da LocaWeb e WhatsApp Web.

import sys
import requests
import selenium
from selenium import webdriver
import pyautogui
from time import sleep
import urllib
import pandas as pd
import command
import pyttsx3
import pysoundcard

#Abrir o Navegador no site desejado:
navegador = webdriver.Chrome()
navegador.get('http://www.grupoolivaltenorio.com.br/')
navegador.find_element_by_xpath('//*[@id="menu"]/ul/li[10]').click()
sleep(2)

#Bot para acessar o e-mail:
pyautogui.typewrite('Seu e-mail da LocaWeb aqui')
pyautogui.press('tab')
pyautogui.typewrite("Sua senha aqui")
pyautogui.press('enter')
sleep(3)


#Trocar as janelas e conseguir manipulá-las com SELENIUM:
navegador.current_window_handle
winds = navegador.window_handles

def find_window(url: str):
    wids = navegador.window_handles
    for window in winds:
        navegador.switch_to.window(window)
        if url in navegador.current_url:
            break
find_window('webmail-seguro')

#API para achar o boletim climático:
API_KEY = '2a7214cf6b1b17869e5363486e015e5e'
cidade = 'Campo Alegre'
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric'

#Formulário para requisição:
requisição = requests.get(link)
boletim = requisição.json()
cidade = "Campo Alegre - Alagoas"
descrição = boletim["weather"][0]['description']
temperatura = boletim["main"]['temp']
vento = boletim["wind"]['speed']
print1 = cidade, ',\n'+ descrição, ',\n'f'{temperatura}ºC'+' e',f'{vento} m/s'
ptint2 = cidade,descrição,temperatura,'graus celsius e vento de',vento,'metros por segundo.'
#Criar um novo e-mail para enviar e copiar o texto de envio:
navegador.find_element_by_xpath('//*[@id="close-popover"]').click()
navegador.find_element_by_xpath('//*[@id="rcmbtn110"]').click()
sleep(4)
pyautogui.typewrite('Destinatário aqui')
pyautogui.press('tab')
pyautogui.typewrite('BOLETIM AGRICOLA - EMAIL AUTOMATICO')
pyautogui.press('tab')
pyautogui.typewrite(f'{cidade} / Mensagem automatica' + ', \n' + f'{temperatura} GRAUS CELSIUS' + ', \n' + f'{vento} metros por segundo.')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl', 'c')
navegador.find_element_by_xpath('//*[@id="rcmbtn108"]/span').click()

#Abrir o WhatsApp Web:
navegador.get('https://web.whatsapp.com/')

def find_window(url: str):
    wids = navegador.window_handles
    for window in winds:
        navegador.switch_to.window(window)
        if url in navegador.current_url:
            break
find_window('WhatsApp')
#Confirmação de que o WPP está realmente aberto e pronto para enviar mensagem:
while len(navegador.find_elements_by_id("side")) < 1:
    sleep(1)
#Encontrar o contato, colar a mensagem e enviá-la:
navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click()
pyautogui.typewrite('Contato Aqui')
pyautogui.press('enter')
navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#BOLETIM POR AUDIO:

#Criando arquivo de áudio:
audio = pyttsx3.init()
mensagem = audio.say(ptint2)
audio.save_to_file(ptint2,'Boletim.wav')
audio.runAndWait()

#Encontrar e enviar arquivo mp3:
navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div').click()
navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li'
                                '[4]/button').click()
sleep(1.5)
pyautogui.typewrite('C:\\Users\\usuario.aqui\\Pasta\\Pasta1')
pyautogui.press('enter')
sleep(1)
pyautogui.typewrite('Boletim.wav')
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')
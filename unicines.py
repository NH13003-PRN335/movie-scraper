from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
import pandas as pd
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
geckodriver_path = 'msedgedriver.exe' 
service = Service(executable_path=geckodriver_path)
browser = webdriver.Edge(service=service)
def agregar_datos(nombre_cine, titulo, idioma, formato, horarios):

  

  for hora in horarios:
    datos = {
      "Fecha": date.today(),
      "País": "honduras",
      "Cine": "unicines",
      "Nombre de cine": nombre_cine,
      "Titulo": titulo,
      "Idioma": idioma,
      "Formato": formato,
      "Hora": hora
    }
    horarios_pelicula.append(datos)
URL = 'https://www.unicines.com/'
horarios_pelicula = []
browser.get(URL)  
#menu=browser.find_element(By.XPATH,'/html/body/header/div[1]/div/div[1]/div')
#menu=browser.find_element(By.XPATH,'/html/body/header/div[1]/div/div[1]/div/div/ul/li[3]/ul/li[1]/a')
menu= WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(browser.find_element(By.XPATH,'/html/body/header/div[1]/div/div[1]/div/input')))
menu.click()
#cartelera=browser.find_element(By.XPATH,'/html/body/header/div[1]/div/div[1]/div/div/ul/li[3]/a') #/ul/[3] referencia a la posicion 3 en el sub menu
cartelera = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(browser.find_element(By.XPATH,'/html/body/header/div[1]/div/div[1]/div/div/ul/li[3]/a')))
cartelera.click() 
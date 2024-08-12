from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date
import pandas as pd
from selenium.webdriver.support.ui import Select
from time import sleep
geckodriver_path = 'msedgedriver.exe' 
service = Service(executable_path=geckodriver_path)
browser = webdriver.Edge(service=service)
def agregar_datos(nombre_cine, titulo, idioma, formato, horarios):
  for hora in horarios:
    datos = {
      "Fecha": date.today(),
      "País": "honduras",
      "Cine": "Metrocinemas",
      "Nombre de cine": nombre_cine,
      "Titulo": titulo,
      "Idioma": idioma,
      "Formato": formato,
      "Hora": hora
    }
    horarios_pelicula.append(datos)

URL = 'https://www.metrocinemas.hn/'
horarios_pelicula = []
browser.get(URL)
cartelera=browser.find_elements(By.XPATH,'//ul[@class="sub-menu"]/li/a')
links=[link.get_attribute("href") for link in cartelera]
for link in links:
  browser.get(link)
  nombre_cine=browser.find_element(By.XPATH,'/html/body/main/section[2]/div/div[1]/div/p[2]').text[2:]
  peliculas=browser.find_elements(By.XPATH,'//*[@id="cartelera"]/div/div[5]/*')
  for pelicula in peliculas:
    titulo=pelicula.find_element(By.XPATH,'.//div[@class="combopelititulo"]/h3').text
    idioma=pelicula.find_element(By.XPATH,'.//div[@class="combodetallepeli"]//div[2]//div[@class="detallespeli"]//div[1]/p').text
    horarios=pelicula.find_elements(By.XPATH,'.//div[@class="combodetallepeli"]//div[2]//div[@class="detallespeli"]//div[7]/ul/li/a')
    for horario in horarios:
      hora=horario.text[0:6]       
      formato=horario.text[7:-1]
      agregar_datos(nombre_cine, titulo, idioma, formato, horarios)
browser.quit
print(horarios_pelicula)
df=pd.DataFrame(horarios_pelicula)
df.to_excel('metrocinemas - '+str(date.today())+'.xlsx', index=False)
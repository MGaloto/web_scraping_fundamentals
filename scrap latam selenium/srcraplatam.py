import requests
from bs4 import BeautifulSoup as BS
import json
from selenium import webdriver
from prefect import task, Flow
from prefect.schedules import IntervalSchedule
from datetime import timedelta
from time import sleep
import pprint


options = webdriver.ChromeOptions()
options.add_argument("--incognito") # Abrimos Chrome utilizando Incognito.
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('chromedriver.exe', options = options)
url = 'https://www.latamairlines.com/ar/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Ida+y+Vuelta%22%2C%22value%22%3A%22RT%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22BUE_AR_CITY%22%2C%22name%22%3A%22null%22%2C%22city%22%3A%22Buenos+Aires%22%2C%22cityIsoCode%22%3A%22BUE%22%2C%22country%22%3A%22Argentina%22%2C%22iata%22%3A%22BUE%22%2C%22latitude%22%3A-34.603684%2C%22longitude%22%3A-58.381559%2C%22timezone%22%3A-3%2C%22tz%22%3A%22America%2FMendoza%22%2C%22type%22%3A%22CITY%22%2C%22countryAlpha2%22%3A%22AR%22%2C%22allAirportsText%22%3A%22xp_sales_web_searchbox_od_allAirports%22%2C%22airportIataCode%22%3A%22BUE%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22MAD_ES_AIRPORT%22%2C%22name%22%3A%22Barajas+Intl.%22%2C%22city%22%3A%22Madrid%22%2C%22cityIsoCode%22%3A%22MAD%22%2C%22country%22%3A%22Espa%C3%B1a%22%2C%22iata%22%3A%22MAD%22%2C%22latitude%22%3A40.471926%2C%22longitude%22%3A-3.56264%2C%22timezone%22%3A1%2C%22tz%22%3A%22Europe%2FMadrid%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22ES%22%2C%22allAirportsText%22%3Anull%2C%22airportIataCode%22%3A%22MAD%22%7D%2C%22dateGoSelected%22%3A%222022-03-10T15%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3A%222022-04-16T15%3A00%3A00.000Z%22%2C%22redemption%22%3Afalse%7D'
driver.get(url)


# Desarrollaremos el codigo que nos permita extraer los datos
# y se lo pase a load

@task
def extract():
    sleep(4) # Le doy tiempo a la pagina para luego capturar el html
    html = driver.execute_script('return document.documentElement.outerHTML')
    sleep(1)
    dom = BS(html, 'html.parser')
    links = dom.find('span', attrs={'class' : 'sc-iSDuPN caAPfe'})
    return links


@task
def load(links):
    print('\n',links.text,'\n')


schedule = IntervalSchedule(interval=timedelta(minutes=0.5))
'''
Este flow ejecuta la primer funcion load.
'''

with Flow('ETL', schedule) as flow:
    '''
    Guardamos el resultado de extract para pasarselo a load
    '''
    raw = extract()
    '''
    En load cargamos lo que pudimos extraer 
    para que nos muestre en pantalla la ejecucion
    '''
    load(raw) # 

'''
Con el siguiente comando ejecutamos el script flow
'''

flow.run()




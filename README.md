<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/200px-Python-logo-notext.svg.png" alt="react" width="50" height="50" />
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" alt="react" width="50" height="50" />
</p>

<br>
</br>



<h1 align="center">Web Scraping</h1>


<p align="center">
<img src="https://www.grazitti.com/wp-content/uploads/2019/08/ETL_Bannera.gif" alt="react" width="600" height="400" />
</p>



Las herramientas de web scraping son software, es decir, bots programados para examinar bases de datos y extraer información. Se utiliza una gran variedad de tipos de bot, muchos de ellos totalmente personalizables para:


<ui>
<li>
Reconocer estructuras de sitios HTML únicos.
</li>
<li>
Extraer y transformar contenidos.
</li>
<li>
Almacenar datos.
</li>
<li>
Extraer datos de las API.
</li>

</ui>

<br>
</br>

El siguiente trabajo consiste en utilizar las siguientes librerias para probar el potencial que tienen cada una a la hora de hacer Web Scraping:

<ui>
<li>
Selenium
</li>
<li>
Beautifoulsoup
</li>
<li>
Scrapy
</li>
<li>
Request
</li>
<li>
Json
</li>
<li>
Prefect
</li>

</ui>


# Prefect
<p align="center">
<img src="https://miro.medium.com/max/1080/1*cZJP7K9tvqci40jRMzTmZQ.jpeg" alt="react" width="600" height="400" />
</p>

Prefect es un sistema de gestión de flujo de trabajo basado en Python (los ETL son un ejemplo de caso de uso). Los usuarios organizan las Tareas en Flujos, definen dependencias, horarios, etc., y Prefect se encarga del resto.

El siguiente script nos muestra el flujo por el que pasan los datos desde su extraccion a la carga en una base de datos. Con @task le damos la orden de avanzar una vez terminada la ejecucion de una funcion.

```
from prefect import task

@task
def extract():
    """Get a list of data"""
    return [1, 2, 3]

@task
def transform(data):
    """Multiply the input by 10"""
    return [i * 10 for i in data]

@task
def load(data):
    """Print the data to indicate it was received"""
    print("Here's your data: {}".format(data))

with Flow('ETL Caso') as flow:
    pass


flow.run()

```
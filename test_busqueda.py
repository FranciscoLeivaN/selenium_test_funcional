from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuración del driver Chrome con Service (recomendado en Selenium 4+)
driver = webdriver.Chrome()

driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")

buscador.send_keys(Keys.RETURN)

# Aumentar el tiempo de espera para asegurar que los resultados cargan
time.sleep(5) #Por defecto, estaba en 2 segundos, ahora se ha aumentado a 5 segundos

# Validar que exista algún resultado - Usar un selector más general
# DuckDuckGo puede haber cambiado sus clases CSS
resultados = driver.find_elements(By.CSS_SELECTOR, "article")
if len(resultados) == 0:
    # Intentar con otro selector si el primero no funciona
    resultados = driver.find_elements(By.CSS_SELECTOR, ".result, .web-result")
    
assert len(resultados) > 0, "No se encontraron resultados."

print (f"Se encontraron {len(resultados)} resultados.")

print(" Prueba funcional completada con éxito")
driver.quit()

import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()

driver = selenium.webdriver.Chrome()

driver.maximize_window()
driver.get('https://krunker.io/?game=SV:tcjwe')
time.sleep(3)

terminos=driver.find_element(By.XPATH,'//button[contains(text(),"I Accept")]')
terminos.click()
time.sleep(3)

login=driver.find_element(By.XPATH,'//div[contains(text(),"Login or Register")]')
login.click()
time.sleep(3)

expert=driver.find_element(By.XPATH,'//div[contains(text(),"Expert Mode")]')
expert.click()
time.sleep(3)

host=driver.find_element(By.XPATH,'//div[contains(text(),"Server Finder")]')
host.click()
time.sleep(3)

Public=driver.find_element(By.XPATH,'/html/body/div[4]/div[5]/div[9]/div/div[3]/div/div[3]')
Public.click()
time.sleep(5)

unirse=driver.find_element(By.XPATH,'/html/body/div[4]/div[5]/div[9]/div/div[3]/div/div[4]/div[1]/div[1]/div')
unirse.click()
time.sleep(5)

url=driver.current_url
##copiar=driver.find_element(By.XPATH,'/html/body/div[4]/div[5]/div[7]/div[1]/div[4]/div[2]/div[4]')
##copiar.click()
##time.sleep(50)
#Crea otra pestaña
driver.execute_script("window.open('', '_blank');")

#se para en la segunda pestaña
driver.switch_to.window(driver.window_handles[1])

# Abre la página de inicio de sesión de Instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# Encuentra el campo de nombre de usuario
username_field = driver.find_element(By.NAME, "username")

#nombre de usuario
username_field.send_keys("cristiancalle517@gmail.com")
time.sleep(2)
# Encuentra el campo de contraseña
password_field = driver.find_element(By.NAME, "password")

# Introduce la contraseña
password_field.send_keys("lili224ana")
time.sleep(2)

# Hace clic en el botón de inicio de sesión
login_button = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button/div")
login_button.click()

# Espera a que la página se cargue
time.sleep(3)

#Hace click en el boton mensajes
messenger_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a")
messenger_button.click()

# Espera a que la página se cargue
time.sleep(3)

#Hace click en el boton ahora no
nonas_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
nonas_button.click()

# Espera a que la página se cargue
time.sleep(2)

#hace click en el lapiz
busca_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[1]/div[2]/div/div")
busca_button.click()

# Espera a que la página se cargue
time.sleep(3)

#encuentra la barra de busqueda para encontrar un perfil
cajaBuscar_field = driver.find_element(By.NAME, "queryBox")
time.sleep(2)

#inserta el nombre del perfil
cajaBuscar_field.send_keys("@santiagocn__")
time.sleep(2)

#hace click en la persona especificada
persona_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div")
persona_button.click()
time.sleep(2)

#hace click en el boton chat
chat_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div")
chat_button.click()
time.sleep(2)

#busca la barra para escribir el mensaje
escribeCaja_field = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]")

#inserta un mensaje
escribeCaja_field.send_keys(url)
time.sleep(2)

#envia el mensaje
envia_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")
envia_button.click()
time.sleep(5)

#inserta un mensaje
escribeCaja_field.send_keys("Jugamos???")
time.sleep(5)

#envia el mensaje
envia_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")
envia_button.click()
time.sleep(5)

print("Proceso ejecutado con exito")

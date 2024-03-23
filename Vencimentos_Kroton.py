import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome()
driver.get("https://login.kroton.com.br/")
driver.set_window_size(1936, 1066)

# Lembre de alterar o login e a senha
usuario = driver.find_element(By.ID, "username")
usuario.click()
usuario.send_keys("seu login")

senha = driver.find_element(By.ID, "password")
senha.send_keys("sua senha")

login_botao = driver.find_element(By.CSS_SELECTOR, ".btn")
login_botao.click()

time.sleep(5)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Estudar")))
except TimeoutException:
    print("Página de 'Estudar' não carregada a tempo.")

driver.find_element(By.LINK_TEXT, "Estudar").click()

time.sleep(10)

try:
    new_window = WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[new_window])
except TimeoutException:
    print("Nova janela não aberta a tempo.")

time.sleep(10)

try:
    total_itens = len(driver.find_elements(By.CSS_SELECTOR, "#navbar-content-aluno-pda > ul > li"))
except NoSuchElementException:
    print("Nenhum item no cronograma encontrado.")

time.sleep(10)

for i in range(1, total_itens + 1):
    nome_selector = f"#navbar-content-aluno-pda > ul > li:nth-child({i}) > table > tbody > tr > td.atividadesCronogramaTableNome"
    datas_selector = f"#navbar-content-aluno-pda > ul > li:nth-child({i}) > table > tbody > tr > td.atividadesCronogramaTableDatas"
    
    try:
        nome_atividade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, nome_selector))).text
        datas_vencimento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, datas_selector))).text
        
        print("Atividade:", nome_atividade)
        print("Datas de vencimento:", datas_vencimento)
        print("-" * 30)
    
    except NoSuchElementException:
        print(f"Elemento não encontrado para o item {i}.")
    
    except TimeoutException:
        print(f"Tempo esgotado para o item {i}.")

driver.quit()

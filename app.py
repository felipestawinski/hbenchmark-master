from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
try:
    # Initialize AI client
    #ai_client = QuestionToAI()
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--reduce-security-for-testing')
    options.set_capability("acceptInsecureCerts", True)

    service = Service()
    #service.creation_flags = 0x08000000  # Prevents command window from appearing

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(60)
    driver.get("https://humanbenchmark.com/tests/aim")
    sleep(1)
    for i in range(30):
        #elem = driver.find_element(By.CSS_SELECTOR, f'div[data-aim-target="true"]')
        element = driver.find_element(By.CSS_SELECTOR, "div.css-17nnhwz.e6yfngs4")
        element.click()

except Exception as e:
    print(e)
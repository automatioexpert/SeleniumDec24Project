from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.way2automation.com/way2auto_jquery/registration.php#load_box")
driver.find_element(By.CSS_SELECTOR, "p>label+input[name='name']").send_keys("User789923")
driver.find_element(By.XPATH, "//p/label[contains(text(),'Last Name:')]/following-sibling::input").send_keys("LastName349347")
driver.find_element(By.CSS_SELECTOR, "input[name='m_status']").click()
driver.find_element(By.XPATH, "(//input[@type='checkbox' and @name='hobby'])[2]").click()

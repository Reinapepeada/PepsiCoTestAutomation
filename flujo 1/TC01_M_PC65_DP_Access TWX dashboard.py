import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
# Open the browser
driver = webdriver.Chrome()
# "+"09384038"+":"+"ARbg95917284."+"@"+"
# try:
    # Open the URL
driver.get("https://meswebgsftmexicali.azure.intra.pepsico.com/Thingworx/Runtime/index.html#master=PepsiCo_Master&mashup=MES_Dashboard&__applyThemeName=PepsiCo%20Default%20Theme&_refreshTS=1670527225809")

time.sleep(15)
    # # Wait for the page to load
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login")))
    # time.sleep(15)
    # Click on the login button
wait=WebDriverWait.until(driver,10)
alert=wait.until(ExpectedConditions.alertIsPresent)
alert= driver.switch_to.alert
alert.authenticateUsing("09384038","ARbg9597284.")
    # driver.switch_to.alert.send_keys("09384038")
    # driver.switch_to.alert.send_keys("ARbg9597284.")
driver.switch_to.alert.accept()

  

# except NoSuchElementException as err:
#     message = 'Exception: ' + str(err.__class__) + str(err.msg)
#     driver.execute_script(
#         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
# except Exception as err:
#     message = 'Exception: ' + str(err.__class__) + str(err.msg)
#     driver.execute_script(
#         'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')

# finally:
#     driver.quit()

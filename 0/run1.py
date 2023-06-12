from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time
import subprocess
import os

opt=Options()
#clear chome


#use powershell to bring up chrome
powershell_script=f"{os.path.dirname(os.path.abspath(__file__))}\cleanchrome.ps1"
#subprocess.run(['powershell.exe', '-File', pspath])
result = subprocess.run(["powershell", "-File", powershell_script], capture_output=True, text=True)

# 檢查執行結果
if result.returncode == 0:
    print("PowerShell文件成功執行！")
    print("輸出結果：", result.stdout)
else:
    print("PowerShell文件執行失敗！")
    print("錯誤信息：", result.stderr)

#opt.add_argument("--headless")
opt.add_experimental_option("debuggerAddress","127.0.0.1:8989")
driver=webdriver.Chrome(options=opt)
driver.implicitly_wait(30)
driver.minimize_window()
driver.get("https://www.hermes.com/us/en/category/women/bags-and-small-leather-goods/small-leather-goods/#|")




#scrape data


#time.sleep(random.randint(30, 60))

""" link=driver.find_element(By.XPATH,"//a/div/span[text()='H Beaute powder bag']")
link.click()
time.sleep(random.randint(30, 60))
add=driver.find_element(By.XPATH,"//button[@name='add-to-cart']")
add.click()
time.sleep(random.randint(30, 60))
view=driver.find_element(By.XPATH,"//button[@name='view-cart']")
view.click()
ttime.sleep(random.randint(30, 60))
checkout=driver.find_element(By.XPATH,"//button[@data-testid='Checkout']")
checkout.click()
time.sleep(random.randint(30, 60))
email=driver.find_element(By.XPATH,"//input[@name='email']")
email.send_keys("chenshouhsien@gmail.com")
time.sleep(random.randint(30, 60))
con=driver.find_element(By.XPATH,"//button[@data-testid='Continue']")
con.click()
time.sleep(random.randint(10, 30)) """
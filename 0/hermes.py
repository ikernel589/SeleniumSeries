from constants import Const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
from selenium.webdriver.chrome.options import Options

class Hermes(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chrome\chromedriver.exe",
                 teardown=False):
        const=Const()
        self.country=const.country
        self.items=const.items
        self.driver_path = const.driver_path
        
        self.BASE_URL=const.BASE_URL

        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        #super(Hermes, self).__init__()
        #self.implicitly_wait(15)
        #self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def initchrome(self,country,port):
        powershell_script=f"{os.path.dirname(os.path.abspath(__file__))}\cleanchrome.ps1"
        result = subprocess.run(["powershell", "-File", powershell_script, country,str(port)], capture_output=True, text=True)

        # 檢查執行結果
        if result.returncode == 0:
            print("PowerShell文件成功執行！")
            print("輸出結果：", result.stdout)
        else:
            print("PowerShell文件執行失敗！")
            print("錯誤信息：", result.stderr)
        
    def checkdrops(self,country="us"):
        port=int(self.country[country.upper()]['port'])+9000
        self.initchrome(country,port)
        
        opt=Options()
        opt.add_experimental_option("debuggerAddress",f"127.0.0.1:{port}")
        self.driver=webdriver.Chrome(options=opt)
        #minimize window?
        url=self.BASE_URL.replace("code",country)
        
        self.driver.get(url)
    
         
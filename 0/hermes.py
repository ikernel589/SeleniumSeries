from constants import Const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import apprise
import html
from datetime import datetime
import pytz
import apprise
import os

class Hermes():
    def __init__(self, country="us",driver_path=r"C:\chrome\chromedriver.exe",
                 teardown=False):
        self.const=Const()
        self.country=country
        self.driver_path=driver_path
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
            
    def send_email_notification(self,email_address, subject, message):
        # Create an Apprise instance
        
        url=f"mailto://ac4swa:rnpfantphqawepem@gmail.com?mode=ssl&smtp=smtp.gmail.com&from=Hermes bag drops alert!&to={email_address}"
        # Add the email notification service
        apobj = apprise.Apprise(url)
        apobj.add("mailto://" + email_address)

        # Send the notification
        apobj.notify(
            body=message,
            title=subject,
            body_format=apprise.NotifyFormat.HTML
        )
    def printdata(self):
        alert("aa")
        
        
    def checkdrops(self):
        pacific = pytz.timezone('US/Pacific')
        now = datetime.now(pacific).strftime("%Y-%m-%d_%H-%M-%S")
        port=int(self.const.country[self.country.upper()]['port'])+9000
        
        opt=Options()
        try:
            opt.add_experimental_option("debuggerAddress",f"127.0.0.1:{port}")
        except Exception as e:
            port=int(self.country[country.upper()]['port'])+9000
            opt.add_experimental_option("debuggerAddress",f"127.0.0.1:{port}")
            
        self.driver=webdriver.Chrome(options=opt)
        #minimize window?
        url=self.const.BASE_URL1.replace("code",self.country)
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(url)
        get_url = self.driver.current_url
        wait.until(EC.url_to_be(url))
        if get_url == url:
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source,features="html.parser")
        table = PrettyTable()
        table.field_names=["Name","Color","Price","Image"]

        divs=soup.find_all(class_="product-item")
        for div in divs:
            href=div.find('a')['href']
            pname=div.find('span', class_='product-item-name').text
            price=div.find('h-price').text.replace("\n","").strip()
            color=div.find('span', text='Color').parent.text.replace("\xa0","").replace(",Color:","").strip()
            pimage=div.find('img')['src']
            if "data:image" in pimage:
                pimage=div.find('img')['data-src']
            table.add_row([pname,color,price,html.escape(f"<a href='https://www.hermes.com{href}'><img height='100' width='100' src='https:{pimage}' alt='{pname}'></a>"),])
           
        table.align["Name"] = "l"
        table.align["Color"] = "c"
        table.align["Price"] = "r"
        table.align["Image"] = "r"
        table.sortby = "Name"

        css_style = '''
        <style>
            table {
                border-collapse: collapse;
            }
            th, td {
                padding: 8px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #dddddd;
            }
        </style>
        '''
        strhtml=f"{css_style}{table.get_html_string()}"
        #strhtml=html.escape(strhtml)
        strhtml=strhtml.replace("&amp;lt;","<").replace("&amp;gt;",">").replace("&amp;","&").replace("&#x27;","'").replace("&amp;","&") 
        self.send_email_notification("chenshouhsien@gmail.com",f"Hermes bag dropped in {self.country}!",strhtml)
        filename = f"{self.const.output_path}\{self.country}\\found-{now}.html"
        with open(filename, 'w') as file:
            file.write(strhtml)
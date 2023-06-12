Remove-Item -Path "c:\chrome\data\*" -Force -Recurse

$ChromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
#$Url = "https://www.hermes.com/us/en/category/women/bags-and-small-leather-goods/small-leather-goods/"
$Parameters = "--remote-debugging-port=8989", "--user-data-dir=C:\chrome\data"

Start-Process -FilePath $ChromePath -ArgumentList $Parameters
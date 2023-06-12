$country=$args[0]
if(-not $country){$country="us"}

$port=$args[1]
if (-not $port){$port="8989"}

$datapath="c:\chrome\data\$country"
if (-not (Test-Path $datapath)) {
    New-Item -ItemType Directory -Path $datapath | Out-Null
}else{
    Remove-Item -Path "$datapath\*" -Force -Recurse
}
$ChromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$Parameters = "--remote-debugging-port=$port", "--user-data-dir=$datapath"

Start-Process -FilePath $ChromePath -ArgumentList $Parameters
import requests
from pyfiglet import Figlet
from clint.textui import colored

banner = Figlet(font='slant')
print(colored.red(banner.renderText("NSlookup")))

url = "github.com"

api = "http://api.hackertarget.com/dnslookup/?q="

data = requests.get(api+url).text

print(colored.green(data))

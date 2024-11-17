import requests
url="https://azedine1981.github.io/anoual.github.io/"
reponse=requests.get(url)
print(reponse.text)

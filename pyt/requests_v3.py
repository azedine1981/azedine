import requests
url='www.men.gov.ma'
reponse=requests.get(url)
print(reponse.text)

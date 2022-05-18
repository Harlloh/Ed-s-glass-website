import requests
website=input('Enter the web adress: ')

r=requests.get(website,'html phraser')
print(r.text)

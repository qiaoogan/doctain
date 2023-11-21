import requests

url = "https://api.crossref.org/works/10.1037/0003-066X.59.1.29/agency"
response = requests.get(url)
print(response.json())
print(response.status_code)
print(response.headers)
print(response.request.url)
print(response.request.headers)
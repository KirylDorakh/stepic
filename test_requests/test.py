import requests

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}

r = requests.get(url, params=par)

print(r.url)
import re
import requests

url = input("Введите адрес сайта: ")
#url = "http://www.columbia.edu/~fdc/sample.html"
response = requests.get(url)
text = response.text

pattern = r'<h3[^>]*>(.*?)</h3>'
result = re.findall(pattern, text)
print(result)
import requests

city = input("Enter City Name: ")
print(city)

print("Displaying Weather Report for: " + city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)
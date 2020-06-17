import requests
a = raw_input("enter your target ip : ")
res = requests.get('https://ipinfo.io/')
data = res.json()


print(res.text)
city = data['city']
print(city)


lattude = data['loc'].split('.')
latitude = location[0]
longitude = location[1]

print("latitude :", latitude)
print("longtitude :", longitude)
print("city :", city)

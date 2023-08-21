from datetime import datetime
import mail
import requests

mylat =  'your latitude as a float'
mylong = 'your longitude as a float'
areasize = 5

latlen = [mylat-areasize,mylat+areasize]
longlen = [mylong-areasize, mylong+areasize]

location = {
    'lat':mylat,
    'lng':mylong,
    'formatted':0,
}


# Fetch iss data

iss = requests.get('http://api.open-notify.org/iss-now.json')
print(iss.status_code)
data = iss.json()['iss_position']
print(data)

# Fetch sunrise data

srss = requests.get('https://api.sunrise-sunset.org/json', params= location)


data_2 =srss.json()['results']
sunrise = data_2['sunrise'].split('T')[1].split('+')[0][0:2]
sunset = data_2['sunset'].split('T')[1].split('+')[0][0:2]
print(sunrise)
print(sunset)

dt = datetime.now().hour
print(dt)

if float(data['latitude'])> latlen[0] and float(data['latitude'])< latlen[1] and float(data['longitude'])> longlen[0] and float(data['longitude'])< longlen[1]:

    if dt > sunset or dt < sunrise:
        mail.conntomail()


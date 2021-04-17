from dotenv import load_dotenv
import os
import requests
load_dotenv()

MAPS_API_KEY = os.getenv('MAPS_API_KEY')

print(MAPS_API_KEY)
address = 'cra 76 # 57 z 96 sur bogota'
address = address.replace(' ', '%20')
res = requests.get(
    'https://maps.googleapis.com/maps/api/geocode/json',
    params={
        'key': MAPS_API_KEY,
        'address': address,
    }
)

decoded_res = res.json()
print(decoded_res['results'][0]['geometry']['location'])

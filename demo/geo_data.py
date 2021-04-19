from dotenv import load_dotenv
import os
import googlemaps

load_dotenv()


class LatLong():
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng


class GeoLocation:
    def __init__(self):
        self.MAPS_API_KEY = os.getenv('MAPS_API_KEY')
        self.client = googlemaps.Client(key=self.MAPS_API_KEY)

    def get_cords(self, direction: str) -> LatLong:
        res = self.client.geocode(direction)[0]['geometry']['location']
        latLong = LatLong(float(res['lat']), float(res['lng']))
        return latLong


if __name__ == '__main__':
    geo = GeoLocation()
    address = 'cra 76 # 57 r 96 sur bogota'
    geocode_res = geo.get_cords(address)
    print(geocode_res.lat)
    print(geocode_res.lng)

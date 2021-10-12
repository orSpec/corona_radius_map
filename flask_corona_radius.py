from flask import Flask, request, render_template, send_file
import folium
from geopy.geocoders import Nominatim

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        result = request.form['number']

        location = geocode(result)
        print(location)
        if location != None:
            createRadiusMap(location)
            latitude = location.latitude
            longitude = location.longitude
            coords = (latitude,longitude)
        else:
            coords = None
    else:
        result = None
        coords = None

    return render_template('corona_radius.html', result=result, coords=coords)

@app.route("/maps/map_radius.html")
def map():
    return send_file("maps/map_radius.html")

def geocode(location):
    geolocator = Nominatim(user_agent="radius")
    location = geolocator.geocode(location)
    return location

def createRadiusMap(location):

    if location != None:
        latitude = location.latitude
        longitude = location.longitude
        location = (latitude, longitude)

        folium_map = folium.Map(location=location, zoom_start=10)
        folium.Circle(location, radius=15000).add_to(folium_map)
        folium_map.save("./maps/map_radius.html")

if __name__ == '__main__':
    app.run()
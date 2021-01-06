
# Corona-Radius-Karte
Quick and Dirty-Implementierung einer Website, die für einen beliebigen Ort einen 15km Radius auf einer Karte darstellt. Die [Website](https://corona-radius-map.herokuapp.com/) ist mithilfe Heroku deployed. Hintergrund ist die beabsichtigte Einführung einer Bewegungseinschränkung in einem Radius von 15 km um den Wohnort aufgrund hoher Corona-Inzidenzen.

<a href="https://corona-radius-map.herokuapp.com/">
<img src="https://user-images.githubusercontent.com/59450716/103778479-94cd4700-5032-11eb-9ffd-626e51425481.png" width="1600">
</a>

### Module / Technologien
 - [Heroku](https://heroku.com) zum Deployment der Python-App
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/) als Webframework
 - [Folium](https://python-visualization.github.io/folium/) zur Kartendarstellung
 - [GeoPy](https://geopy.readthedocs.io/en/stable/) zum Geokodieren der Adressinformation

### Issues
[#1](https://github.com/orSpec/corona_radius_map/issues/1): Folium-Karte wird nicht aktualisiert.


import numpy as np
import pandas as pd
import folium


def maker_in_map(map, lat, lon, target_names):
    for y, x, n in zip(lat, lon, target_names):
        folium.Marker(location=[y, x],
                      popup=n,
                      icon=folium.Icon(color='red', icon='star')).add_to(map)


if __name__ == "__main__":
    travel_office_file = '부산관광안내소정보.csv'
    travel_office = pd.read_csv(travel_office_file)

    latitudes = travel_office['위도']
    longitudes = travel_office['경도']
    names = travel_office['이름']
    print(names[5])

    office_map = folium.Map(
        location=[35.15799988296419, 129.0600760132606], zoom_start=11)

    maker_in_map(office_map, latitudes, longitudes, names)

    office_map.save('office_makers.html')

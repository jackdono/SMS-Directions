from warnings import catch_warnings
from geopy.geocoders import Nominatim
import openrouteservice
from openrouteservice.directions import directions

geolocator = Nominatim(user_agent="none")

def getroute(start_addr, end_addr):

    start_loc = geolocator.geocode(str(start_addr))
    end_loc = geolocator.geocode(str(end_addr))

    # Attempt to resolve coordinates and route
    try:
        coords = ((start_loc.longitude, start_loc.latitude),(end_loc.longitude, end_loc.latitude))
        client = openrouteservice.Client(key='API_KEY')
        routes = directions(client, coords)
        route_found = True
    except:
        # Route not found or addresses invalid
        route_found = False



    if route_found:
        # Segments (nested dict inside 'routes') contains steps, waypoint etc.
        # Get total distance and time
        segments_dict = (routes.get('routes')[0]).get('segments')[0]
        dist_total = round(segments_dict.get('distance')/1000, 1)
        time_total = round(segments_dict.get('duration')/60, 1)


        route_string = str(dist_total) + ' km, ' + str(time_total) + ' min (driving)\n'


        # Steps - each step is its own list element, stored as a dictionary with distances, times, instructions etc.
        steps_list = segments_dict.get('steps')

        for i in range(len(steps_list)):
            step = steps_list[i]
            instruction = step.get('instruction')
            distance = str(round(step.get('distance')/1000, 2)) + ' km'
            route_string += instruction + ', go ' + distance + '\n\n'

    elif not route_found:
        route_string += 'No route was found. Double check the addresses.'
    
    return route_string
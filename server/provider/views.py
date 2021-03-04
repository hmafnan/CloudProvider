import math
import requests
from distutils.util import strtobool

from django.http import JsonResponse


def clouds(request):
    result = []
    api_url = 'https://api.aiven.io/v1/clouds'
    provider = request.GET.get('provider', 'all')
    nearest = strtobool(request.GET.get('nearest', 'false'))
    current_coords = (float(request.GET.get('latitude')), float(request.GET.get('longitude')))

    try:
        response = requests.get(api_url).json()['clouds']
    except Exception as err:
        return JsonResponse(result, safe=False)

    if provider in ('aws', 'google'):
        response = [d for d in response if d['cloud_name'].startswith(provider)]
    for data in response:
        result.append({
            'cloud_description': data['cloud_description'],
            'cloud_name': data['cloud_name'],
            'geo_region': data['geo_region'],
            'distance': haversine(
                current_coords,
                (float(data['geo_latitude']), float(data['geo_longitude'])))
        })

    result = get_nearest(nearest, result)
    return JsonResponse(result, safe=False)


def get_nearest(nearest, data):
    """Filter by nearest distance and return top 5
    :param nearest: Boolean
    :param data: List of dictionaries
    :returns: Top 5 nearest results
    """
    if nearest:
        data = sorted(data, key=lambda k: k['distance'])
        data = data[:5]
    return data


def haversine(coord1, coord2):
    """Implementation for calculating haversine distance
    between two points on a sphere

    Copied from: https://janakiev.com/blog/gps-points-distance-python/
    
    :param coord1: Tuple containing latitude/longitude
    :param coord2: Tuple containing latitude/longitude
    :returns: Distance between two points in km
    """
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


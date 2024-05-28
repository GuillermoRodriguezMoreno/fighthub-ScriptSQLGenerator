import random


def generate_random_lat_andalucia():
    # Límites aproximados de latitud y longitud de Andalucía
    lat_min, lat_max = 36.0, 38.7
    latitude = random.uniform(lat_min, lat_max)
    return latitude


def generate_random_long_andalucia():
    lon_min, lon_max = -7.5, -1.5
    longitude = random.uniform(lon_min, lon_max)
    return longitude

from typing import NamedTuple
from math import sqrt


Coordenadas = NamedTuple('Coordenadas', [('latitud',float), ('longitud', float)])

def calcular_distancia(Coordenada1:Coordenadas,Coordenada2:Coordenadas)-> float:
    dist = sqrt((Coordenada2.latitud - Coordenada1.latitud)**2 + ((Coordenada2.longitud - Coordenada1.longitud)**2))
    return dist

def calcular_media_coordenadas(coords:list[Coordenadas])-> Coordenadas:
    lat = 0
    lon = 0
    for c in coords:
        lat += c.latitud
        lon += c.longitud
    return Coordenadas(lat/len(coords),lon/len(coords))








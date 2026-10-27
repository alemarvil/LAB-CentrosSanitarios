from typing import NamedTuple,List
import csv
from coordenadas import *
from mapas import *

CentroSanitario = NamedTuple('CentroSanitario',
                             [('nombre',str),
                              ('localidad',str), 
                              ('ubicacion',Coordenadas),
                              ('estado',str),
                              ('num_camas', int), 
                              ('acceso_discapacitados', bool), 
                              ('tiene_uci',bool)
                              ])

def leer_centros (ruta:str)->List[CentroSanitario]:
    centros = []
    with open (ruta,encoding = 'utf-8') as f:
        lector = csv.reader(f,delimiter= ';')
        next(lector)
        for fila in lector:
            nombre = fila[0].strip()
            localidad = fila[1].strip()
            latitud = float(fila[2].replace(';',','))
            longitud = float(fila[3].replace(';',','))
            ubicacion = Coordenadas(latitud,longitud)
            estado = fila[4].strip()
            num_camas = int(fila[5].strip())
            acceso_discapacitados = True if fila[6] == "true" else False #cuidado que hay que parsear esto porque si no pone false si el campo esta vacío
            tiene_uci = True if fila[7] == "true" else False

            registro = CentroSanitario(nombre,localidad,ubicacion,estado,num_camas,acceso_discapacitados,tiene_uci)

            centros.append(registro)
        return centros


def calcular_total_camas_centros_accesibles(centros:List[CentroSanitario])-> int:
    sum = 0
    for c in centros:
        if c.acceso_discapacitados:
            sum += c.num_camas
    return sum

def obtener_centros_con_uci_cercanos_a(centros:List[CentroSanitario], coordenadas:Coordenadas,distancia_max:float)-> List[(str, str, Coordenadas)]:
    centros_cercanos = []
    for c in centros:
        if calcular_distancia(coordenadas,c.ubicacion) <= distancia_max and c.tiene_uci:
            centros_cercanos.append((c.nombre,c.localidad,c.ubicacion))
    return centros_cercanos


def generar_mapa(centros_loc:List[tuple[str,str,Coordenadas]],ruta_html:str):
    coordenadas = []

    for c in centros_loc:
        coordenadas.append(c[2])

    centro = calcular_media_coordenadas(coordenadas)

    mapa = crea_mapa(centro)

    for nombre, localidad, ubicacion in centros_loc:
        etiqueta = f"{nombre} ({localidad})"
        agrega_marcador(mapa, ubicacion, etiqueta, etiqueta)

    guarda_mapa(mapa, ruta_html)

    

        

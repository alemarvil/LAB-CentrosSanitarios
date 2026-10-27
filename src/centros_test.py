from centros import *
from coordenadas import *

def test_generar_mapa():
    
    a = leer_centros("data/centrosSanitarios.csv")
    
    punto_referencia = Coordenadas(36.5, -6.2)
    umbral = 0.3
    
    centros_cercanos = obtener_centros_con_uci_cercanos_a(a, punto_referencia, umbral)
    print(f"Centros encontrados: {len(centros_cercanos)}")
    
    ruta_salida = "doc/mapa_centros.html"
    generar_mapa(centros_cercanos, ruta_salida)
    print(f"Mapa generado con éxito en: {ruta_salida}")




if __name__ == "__main__":
    a = leer_centros('data\centrosSanitarios.csv')
    print (a)

    test_generar_mapa()

import os

def scan_networks():
    #Ejecutar el comando para escanear redes WiFi

    networks = os.popen("iwlist wlan0 scanning | grep 'ESSID'").read()

    # mostrar las redes encontradas

    print("Redes WiFi encontradas: ")
    print(networks)


scan_networks()
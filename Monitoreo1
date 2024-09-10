from scapy.all import sniff, IP, TCP
from datetime import datetime

# Importamos os para asegurarnos de que este código funcione en cualquier sistema operativo

import os

# Aquí nos aseguraremos de que la carpeta logs se cree en el directorio que estamos ejecutando
# este código y donde se almacenarán los logs sospechosos

if not os.path.exists("logs"):
    os.makedirs("losgs")

# Diccionario para rastrear intentos de conexión a puertos

port_scans = {}

# Función para escribir los logs en un archivo

def log_scan(src_ip):
    log_file = "logs/port_scan_log.txt" # Ruta del archivo de log
    with open(log_file, 'a') as f: # Abrimos el archivo en modo append para añdir info
        log_entry = f"{datetime.now()} Posible escaneo de puertos detectado desde {src_ip}\n"
        f.write(log_entry) # Escribimos la entrada (f) en el archivo log_entry
        
# Función para detectar escaneos de puertos

def detect_port_scan(packet):
    if packet.haslayer(TCP): # Solo analizamos paquetes TCP
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport


        # Contamos cuantos puertos diferentes ha intentado escanear una ip
        if src_ip in port_scans:
            port_scans[src_ip].add(dst_port)

        else:
            port_scans[src_ip] = {dst_port}

        # Si detectamos que una IP ha intentado conectar a muchos puertos en poco tiempo

        if len(port_scans[src_ip]) > 10: # Umbral arbitrario de 10 puertos
            print (f"Posible escaneo de puertos detectado desde {src_ip}")

# Captura de paquetes con filtro para TCP
sniff(filter="tcp", prn=detect_port_scan, store=0)

# by r3d



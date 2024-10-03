import speedtest

def wifi_scan():

    networks = os.popen("iwlist wlan0 scanning | grep'ESSID'").read()

def speed_test():
    st = speed_test.Speedtest()
    print("Seleccionando el mejor servidor...")

    st.get_best_server()
    print("Midiendo velocidad de descarga...")

    download_speed = st.download() / 1_000_000
    print (f"Velocidad de descargar: {download_speed:.2f} Mbps")

    print ("Midiendo velocidad de  subida...")

    upload_speed = st.upload() /1_000_000
    print(f"Velocidad de subida: {upload_speed:.2f} Mbps")

    # Ejecutamos funciones

    wifi_scan()
    speed_test()
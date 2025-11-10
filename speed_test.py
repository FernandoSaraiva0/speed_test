from tqdm import tqdm
import time
import speedtest

st = speedtest.Speedtest()

# Seleciona o melhor servidor com barra de progresso
def select_best_server():
    print("Selecionando o melhor servidor...")
    with tqdm(total=100, bar_format='{l_bar}{bar}| {elapsed}') as pbar:
        import threading
        result = [None]

        def run_test():
            result[0] = st.get_best_server()

        thread = threading.Thread(target=run_test)
        thread.start()

        while thread.is_alive():
            pbar.update(1)
            time.sleep(0.1)

        thread.join()
        pbar.n = 100
        pbar.refresh()

    return result[0]
best_server = select_best_server()
print(f"Melhor servidor selecionado: {best_server['sponsor']} em {best_server['name']}, {best_server['country']}")

#Função para converter bytes para megabits
import math
def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, i)
    size = round(size_bytes / power, 2)
    return f"{size} Mbps"

# Realiza o teste de download
print("Captando velocidade de Download...")
with tqdm(total=100, bar_format='{l_bar}{bar}| {elapsed}') as pbar:
    import threading
    result = [None]

    def run_test():
        result[0] = st.download()

    thread = threading.Thread(target=run_test)
    thread.start()

    while thread.is_alive():
        pbar.update(1)
        time.sleep(0.1)

    thread.join()
    pbar.n = 100
    pbar.refresh()

download_speed = result[0]

# Realiza o teste de upload
print("Captando velocidade de Upload...")
with tqdm(total=100, bar_format='{l_bar}{bar}| {elapsed}') as pbar:
    import threading
    result = [None]

    def run_test():
        result[0] = st.upload()

    thread = threading.Thread(target=run_test)
    thread.start()

    while thread.is_alive():
        pbar.update(1)
        time.sleep(0.1)

    thread.join()
    pbar.n = 100
    pbar.refresh()

upload_speed = result[0]

# Obtém o ping

print("Captando ping da rede...")
with tqdm(total=100, bar_format='{l_bar}{bar}| {elapsed}') as pbar:
    import threading
    result = [None]

    def run_test():
        result[0] = st.results.ping

    thread = threading.Thread(target=run_test)
    thread.start()

    while thread.is_alive():
        pbar.update(1)
        time.sleep(0.1)

    thread.join()
    pbar.n = 100
    pbar.refresh()

ping = result[0]
ping = st.results.ping

print(f"Ping: {ping:.2f} ms")
print(f"Velocidade de Download:", bytes_to_mb(download_speed))
print(f"Velocidade de Upload: {bytes_to_mb(upload_speed)}")

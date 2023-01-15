import tkinter as tk
from speedtest import Speedtest

def test_speed():
    st = Speedtest()
    st.get_best_server()
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping
    download_speed_mbps = round(download_speed / (10**6), 2)
    upload_speed_mbps = round(upload_speed / (10**6), 2)

    download_label.config(text=f"Download Speed: {download_speed_mbps} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed_mbps} Mbps")
    ping_label.config(text=f"Ping: {ping} ms")

root = tk.Tk()
root.title("Internet Speed Meter")
root.geometry("400x200")

download_label = tk.Label(root, text="Download Speed: ", font=("Helvetica", 18))
download_label.pack()

upload_label = tk.Label(root, text="Upload Speed: ", font=("Helvetica", 18))
upload_label.pack()

ping_label = tk.Label(root, text="Ping: ", font=("Helvetica", 18))
ping_label.pack()

test_button = tk.Button(root, text="Test Speed", font=("Helvetica", 18), command=test_speed)
test_button.pack()

root.mainloop()

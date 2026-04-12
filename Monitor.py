import psutil
import time
import os
def MonitoramentoDeSistema():
    cpu = psutil.cpu_percent(interval=None, percpu=False)
    ram = psutil.virtual_memory().percent
    Disk = psutil.disk_usage(path='/').percent
    Swap = psutil.swap_memory().percent
    os.system("clear")
    
    print(f"""
=== Monitor do Sistema ===
    
    CPU: {cpu}%
    Memória RAM: {ram}%
    Uso do Disco: {Disk}%
    Swap: {Swap}%
    
=========================
""")
    
while True:
    MonitoramentoDeSistema()
    time.sleep(1)

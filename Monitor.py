import psutil
import time
import os
from notifypy import Notify
def MonitoramentoDeSistema():
    cpu = psutil.cpu_percent(interval=None, percpu=False)
    ram = psutil.virtual_memory().percent
    Disk = psutil.disk_usage(path='/').percent
    Swap = psutil.swap_memory().percent
    os.system("clear")
    

    notification = Notify()
    if (cpu <= 10):
        usocpu = "Consumo baixo"
    elif (cpu <= 30):
        usocpu = "Consumo moderado"
    elif (cpu <= 70):
        usocpu = "Consumo intermediário"
    elif (cpu <= 90):
        usocpu = "Consumo alto"
        notification = Notify()
        notification.title ='Consumo de CPU alto'
        notification.message = f'O consumo de seu processador está em {cpu}%'
        notification.icon = 'icon/icone.webp'
        notification.duration = 0.5
        notification.send()
        
    else:
        usocpu = "Consumo muito alto"
        
        notification.title = 'Consumo de CPU MUITO ALTO'
        notification.message = f'O consumo de seu processador está em {cpu}%'
        notification.icon = 'icon/icone.webp'
        notification.duration = 0.5
        notification.send()

        
    if(ram < 35):
        usoram  = "Baixo"
    elif(ram > 35 and ram <= 40):
        usoram = "Normal"
    elif(ram > 40 and ram <= 79):
        usoram = "Moderado"
    else:
        usoram = "Alto"
    

    print(f"""
        === Monitor do Sistema ===
            
        CPU: {cpu}% [{usocpu}]
        Memória RAM: {ram}% [{usoram}]
        Uso do Disco: {Disk}%
        Swap: {Swap}%
            
        =========================
    """)    
    
    

 
while True:
    
    MonitoramentoDeSistema()
    time.sleep(1)

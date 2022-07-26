#!/bin/python3
#---- Script creado por Herr Stiefel
#---- Obtencion de comandos en switch mediante python

import time, logging, getpass
from alive_progress import alive_bar
from datetime import date
from netmiko import ConnectHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('alive_progress')

today = date.today()
print("... Bienvenido al respaldo automatico de Routers Cisco  ...")
print("... Por favor verifica que la conexion sea mediante SSH ...")
target = input("IP address: ") # Se solicita al usuario ingresar la direccion IP
print("SSH Login")
user = input("User: ") # se solicita usuario con el que se puede ingresar al dispositivo
passw = getpass.getpass() #Solicita password para entrar al dispositivo sin mostrar los caracteres

iou1 = {
'device_type': 'cisco_ios',
'ip': target,
'username': user,
'password': passw,
}

device = ConnectHandler(**iou1) # Conexion al dispositivo

output0 = device.send_command("show run | include hostname")

comandos = ["show running-config",
"show version",
"show inventory",
"show module",
"show interfaces status",
"show interfaces",
"show interfaces | incl error",
"show interfaces | incl broadcast",
"show interfaces description",
"show ip interface brief",
"show vlan",
"show arp",
"show mac address-table",
"show ip route",
"show ip protocols",
"show ip bgp",
"show ip bgp neighbors",
"show ip bgp summary",
"show ip eigrp neighbors",
"show ip ospf neighbors",
"show ip ospf database",
"show ip cef",
"show cdp neighbors",
"show cdp neighbors detail",
"show lldp neighbors",
"show lldp neighbors detail",
"show logging",
"show startup-config"]

ciclos = (len(comandos))
# print (ciclos) 
# print (comandos)

save_file = open((output0[9::])+"-backup-"+str(today)+".txt","w")

with alive_bar(ciclos) as bar:
    for i in range(ciclos):
        print (comandos[(i)])
        showprint = (comandos[(i)])
        output = device.send_command(comandos[(i)])
        save_file.write("\n\n\n ----------------------------------------------------- \n")
        save_file.write("\n *          "+showprint.upper()+"        * \n")
        save_file.write("\n --------------------------------------------------------- \n")
        save_file.write(output)
        time.sleep(0.01)
        bar()

save_file.close() # Se guarda el documento en la misma ruta donde se ejecuta el programa
device.disconnect() # desconexion del dispositivo

# Mis Archivos de respaldo

Estos proyectos son creados en python 3, y es necesario contar  con las librerias que solicita al inicio de cada proyecto.

```
import time, logging, getpass
from alive_progress import alive_bar
from datetime import date
from netmiko import ConnectHandler
```

Las librerias que se mencionan se pueden instalar en la terminal con los siguientes comandos, pero para eso debe de estar habilitada la opcion de pip
y en caso de ser necesario, se deberan de correr los comandos en siendo usuario root o anteponiendo el comando "sudo"
```
python3 -m pip install --upgrade pip
pip3 install alive_progress
pip3 install netmiko

```
